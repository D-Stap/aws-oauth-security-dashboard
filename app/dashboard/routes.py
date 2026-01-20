import jwt
from flask import Blueprint, render_template, session, redirect, url_for, jsonify
from functools import wraps
import config

dashboard_bp = Blueprint('dashboard', __name__)

def login_required(f):
    """Decorator to require authentication."""
    @wraps(f)
    def decorated_function(*args, **kwargs):
        if 'user' not in session:
            return redirect(url_for('auth.login'))
        return f(*args, **kwargs)
    return decorated_function

@dashboard_bp.route('/')
@login_required
def index():
    """Main dashboard page."""
    user = session.get('user', {})
    tokens = session.get('tokens', {})
    
    # Decode JWT for display purposes
    id_token_decoded = None
    if tokens.get('id_token'):
        try:
            # Decode without verification for display only
            id_token_decoded = jwt.decode(tokens['id_token'], options={"verify_signature": False})
        except Exception:
            id_token_decoded = None
    
    return render_template('dashboard/index.html', 
                         user=user, 
                         tokens=tokens,
                         id_token_decoded=id_token_decoded)

@dashboard_bp.route('/profile')
@login_required
def profile():
    """User profile page."""
    user = session.get('user', {})
    return render_template('dashboard/profile.html', user=user)

@dashboard_bp.route('/tokens')
@login_required
def tokens():
    """Token information page."""
    tokens = session.get('tokens', {})
    
    # Decode tokens for display
    decoded_tokens = {}
    for token_type in ['access_token', 'id_token']:
        if tokens.get(token_type):
            try:
                decoded_tokens[token_type] = jwt.decode(
                    tokens[token_type], 
                    options={"verify_signature": False}
                )
            except Exception as e:
                decoded_tokens[token_type] = f"Error decoding: {str(e)}"
    
    return render_template('dashboard/tokens.html', 
                         tokens=tokens,
                         decoded_tokens=decoded_tokens)

@dashboard_bp.route('/api/user')
@login_required
def api_user():
    """API endpoint returning user info."""
    return jsonify(session.get('user', {}))

@dashboard_bp.route('/security')
@login_required
def security():
    """Security analysis page."""
    user = session.get('user', {})
    tokens = session.get('tokens', {})
    
    # Mock session info for security demonstration
    session_info = {
        'oauth_state_cleared': True,
        'code_verifier_cleared': True,
        'secure_cookies': 'HttpOnly, Secure, SameSite',
        'session_timeout': '12 hours'
    }
    
    # Extract user groups from tokens for RBAC demo
    user_groups = []
    if tokens.get('id_token'):
        try:
            decoded = jwt.decode(tokens['id_token'], options={"verify_signature": False})
            user_groups = decoded.get('cognito:groups', [])
        except:
            pass
    
    return render_template('dashboard/security.html', 
                         user=user,
                         tokens=tokens,
                         session_info=session_info,
                         user_groups=user_groups)

@dashboard_bp.route('/docs')
@login_required
def docs():
    """Documentation page."""
    return render_template('dashboard/docs.html')