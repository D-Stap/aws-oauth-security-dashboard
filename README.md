

[![Live Resume](https://img.shields.io/badge/Live%20Resume-grey?style=flat&labelColor=red&logo=readthedocs)](https://dafantestapletonresume.link)
[![LinkedIn](https://img.shields.io/badge/LinkedIn-grey?style=flat&labelColor=0A66C2&logo=linkedin&logoColor=white)](https://www.linkedin.com/in/dafante-stapleton/)
[![GitHub](https://img.shields.io/badge/Profile-grey?style=flat&labelColor=181717&logo=github&logoColor=white)](https://github.com/D-Stap)
[![Credly](https://img.shields.io/badge/Credly-grey?style=flat&labelColor=FF6B00&logo=credly&logoColor=white)](https://www.credly.com/users/dafante-stapleton)
[![Email](https://img.shields.io/badge/Email-grey?style=flat&labelColor=EA4335&logo=gmail&logoColor=white)](mailto:dafante.e.stapleton.com)


# OAuth Security Dashboard

A Flask application implementing secure OAuth2 + OIDC with AWS Cognito. This project features industry-standard authentication patterns, security controls, and web application security best practices.

## Demo

<!-- Replace with your actual video file -->
![OAuth Security Dashboard Demo](assets/DemoGif.gif)

*Complete OAuth2 authentication flow with security analysis and token management*

## Features

- **OAuth2 + OIDC Authentication**: Complete implementation using AWS Cognito
- **PKCE Security**: Protection against authorization code interception attacks
- **CSRF Protection**: State parameter validation prevents cross-site request forgery
- **JWT Token Handling**: Secure token validation and management
- **RBAC Implementation**: Role-based access control using Cognito groups
- **Security Analysis**: Real-time security status monitoring and threat mitigation
- **Production Ready**: Secure session handling, HTTPS enforcement, audit logging

## Architecture

```
Browser -> Flask App -> AWS Cognito -> Flask App -> Dashboard
```

The application implements the OAuth2 Authorization Code flow with PKCE:
1. **Authorization Request**: Secure redirect to Cognito with PKCE challenge
2. **User Authentication**: Cognito Hosted UI handles login
3. **Token Exchange**: Authorization code exchanged for JWT tokens
4. **Session Creation**: Secure session established with validated tokens

## Security Controls

- **PKCE (Proof Key for Code Exchange)**: Prevents authorization code interception
- **State Parameter Validation**: CSRF protection for OAuth flows
- **Secure Session Management**: HttpOnly, Secure, SameSite cookies
- **JWT Signature Validation**: Token integrity verification
- **Short Token Lifetimes**: Access tokens expire in 60 minutes
- **Automatic Token Refresh**: Seamless token renewal
- **Secure Error Handling**: No information leakage in error responses

## Project Structure

```
aws-oauth-security-dashboard/
  app/                          # Main application
    auth/                       # Authentication module
      routes.py                 # OAuth2 routes and handlers
      pkce.py                   # PKCE implementation
    dashboard/                  # Dashboard module
      routes.py                 # Dashboard routes
    templates/                  # Jinja2 templates
      base.html                 # Base template
      home.html                 # Landing page
      dashboard/                # Dashboard templates
    app.py                      # Flask application factory
    config.py                   # Configuration management
    .env                        # Environment variables (not in git)
    requirements.txt            # Python dependencies
  core-infra/                   # Terraform infrastructure
    terraform/                  # AWS Cognito setup
  README.md                     # This file
```

## Setup

### Prerequisites
- Python 3.8+
- AWS CLI configured
- AWS Cognito User Pool (see configuration below)

### Quick Start

1. **Clone and Navigate**
   ```bash
   git clone <repository-url>
   cd aws-oauth-security-dashboard
   ```

2. **Set Environment Variables**
   ```bash
   cp app/.env.template app/.env
   # Edit app/.env with your Cognito configuration
   ```

3. **Install Dependencies**
   ```bash
   pip install -r app/requirements.txt
   ```

4. **Run Application**
   ```bash
   ./run.sh
   # Or: cd app && python run.py
   ```

### AWS Cognito Configuration

The application requires an AWS Cognito User Pool with the following configuration:

**Required Environment Variables (app/.env):**
```env
# Flask Configuration
FLASK_SECRET_KEY=<generate-secure-key-here>
FLASK_DEBUG=true

# AWS Cognito Configuration
COGNITO_REGION=us-east-2
COGNITO_USER_POOL_ID=your-user-pool-id
COGNITO_CLIENT_ID=your-client-id
COGNITO_DOMAIN=https://your-domain.auth.region.amazoncognito.com
COGNITO_REDIRECT_URI=http://localhost:5001/auth/callback
COGNITO_LOGOUT_REDIRECT_URI=http://localhost:5001/
```

**Cognito App Client Settings:**
- OAuth Flows: Authorization Code with PKCE
- Scopes: `openid`, `email`, `profile`
- Callback URLs: `http://localhost:5001/auth/callback`
- Sign out URLs: `http://localhost:5001/`

**Generate Secure Flask Secret:**
```bash
python3 -c "import secrets; print('FLASK_SECRET_KEY=' + secrets.token_urlsafe(32))"
```

## Security Features

The application includes several pages covering security concepts:

- **Dashboard**: User information and authentication status
- **Security Analysis**: Real-time security controls and threat mitigation
- **Token Information**: JWT token contents and security properties
- **Documentation**: OAuth2 flow breakdown and threat model
- **Profile**: User information from Cognito

## Technologies

- **Backend**: Flask (Python)
- **Authentication**: AWS Cognito
- **Security**: OAuth2, OIDC, PKCE, JWT
- **Frontend**: Bootstrap 5, Font Awesome
- **Infrastructure**: Terraform (AWS)

## License

MIT License - see LICENSE file for details.
