import base64
import hashlib
import secrets
import urllib.parse


def generate_pkce_pair():
    """Generate PKCE code verifier and challenge."""
    # Generate code verifier (43-128 characters)
    verifier_bytes = base64.urlsafe_b64encode(secrets.token_bytes(32))
    code_verifier = verifier_bytes.decode("utf-8").rstrip("=")

    # Generate code challenge (SHA256 hash of verifier)
    code_challenge = (
        base64.urlsafe_b64encode(hashlib.sha256(code_verifier.encode("utf-8")).digest())
        .decode("utf-8")
        .rstrip("=")
    )

    return code_verifier, code_challenge


def generate_state():
    """Generate random state parameter for CSRF protection."""
    return secrets.token_urlsafe(32)


def build_auth_url(client_id, domain, redirect_uri, state, code_challenge):
    """Build Cognito authorization URL."""
    params = {
        "response_type": "code",
        "client_id": client_id,
        "redirect_uri": redirect_uri,
        "scope": "openid email profile",
        "state": state,
        "code_challenge": code_challenge,
        "code_challenge_method": "S256",
    }

    query_string = urllib.parse.urlencode(params)
    return f"{domain}/oauth2/authorize?{query_string}"
