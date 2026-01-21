import config
import requests
from flask import Blueprint, current_app, flash, redirect, request, session, url_for

from .pkce import build_auth_url, generate_pkce_pair, generate_state

auth_bp = Blueprint("auth", __name__)


@auth_bp.route("/login")
def login():
    """Initiate OAuth2 login flow."""
    # Generate PKCE parameters
    code_verifier, code_challenge = generate_pkce_pair()
    state = generate_state()

    # Store in session for callback verification
    session["code_verifier"] = code_verifier
    session["oauth_state"] = state

    # Build authorization URL
    auth_url = build_auth_url(
        client_id=config.COGNITO_CLIENT_ID,
        domain=config.COGNITO_DOMAIN,
        redirect_uri=config.COGNITO_REDIRECT_URI,
        state=state,
        code_challenge=code_challenge,
    )

    return redirect(auth_url)


@auth_bp.route("/callback")
def callback():
    """Handle OAuth2 callback from Cognito."""
    # Verify state parameter (CSRF protection)
    if request.args.get("state") != session.get("oauth_state"):
        flash("Invalid state parameter. Possible CSRF attack.", "error")
        return redirect(url_for("home"))

    # Get authorization code
    code = request.args.get("code")
    if not code:
        error = request.args.get("error", "Unknown error")
        flash(f"Authorization failed: {error}", "error")
        return redirect(url_for("home"))

    # Exchange code for tokens
    try:
        tokens = exchange_code_for_tokens(code, session.get("code_verifier"))
        user_info = get_user_info(tokens["access_token"])

        # Store user info in session
        session["user"] = user_info
        session["tokens"] = tokens

        # Clean up OAuth session data
        session.pop("code_verifier", None)
        session.pop("oauth_state", None)

        flash("Successfully logged in!", "success")
        return redirect(url_for("dashboard.index"))

    except Exception as e:
        current_app.logger.error(f"Token exchange failed: {str(e)}")
        flash("Login failed. Please try again.", "error")
        return redirect(url_for("home"))


@auth_bp.route("/logout")
def logout():
    """Log out user and redirect to Cognito logout."""
    # Clear session
    session.clear()

    # Build Cognito logout URL
    logout_url = (
        f"{config.COGNITO_DOMAIN}/logout?"
        + f"client_id={config.COGNITO_CLIENT_ID}&"
        + f"logout_uri={config.COGNITO_LOGOUT_REDIRECT_URI}"
    )

    return redirect(logout_url)


@auth_bp.route("/test-error")
def test_error():
    """Test error handling for security demonstration."""
    error_type = request.args.get("type", "csrf")

    if error_type == "csrf":
        flash("CSRF Protection Test: Invalid state parameter detected", "error")
    elif error_type == "token":
        flash("Token Error Test: Invalid or expired token", "error")
    elif error_type == "expired":
        flash("Session Expiry Test: Session has expired", "error")
    else:
        flash("Unknown error type for testing", "error")

    return redirect(url_for("dashboard.security"))


def exchange_code_for_tokens(code, code_verifier):
    """Exchange authorization code for access tokens."""
    token_url = f"{config.COGNITO_DOMAIN}/oauth2/token"

    data = {
        "grant_type": "authorization_code",
        "client_id": config.COGNITO_CLIENT_ID,
        "code": code,
        "redirect_uri": config.COGNITO_REDIRECT_URI,
        "code_verifier": code_verifier,
    }

    headers = {"Content-Type": "application/x-www-form-urlencoded"}

    response = requests.post(token_url, data=data, headers=headers, timeout=10)
    response.raise_for_status()

    return response.json()


def get_user_info(access_token):
    """Get user information from Cognito."""
    userinfo_url = f"{config.COGNITO_DOMAIN}/oauth2/userInfo"

    headers = {"Authorization": f"Bearer {access_token}"}

    response = requests.get(userinfo_url, headers=headers, timeout=10)
    response.raise_for_status()

    return response.json()
