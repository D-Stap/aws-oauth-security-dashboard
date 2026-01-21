import os

from dotenv import load_dotenv

# Load environment variables
load_dotenv()

SECRET_KEY = os.getenv("FLASK_SECRET_KEY", "dev-key-change-me")
DEBUG = os.getenv("FLASK_DEBUG", "false").lower() == "true"

# AWS Cognito configuration
COGNITO_REGION = os.getenv("COGNITO_REGION")
COGNITO_USER_POOL_ID = os.getenv("COGNITO_USER_POOL_ID")
COGNITO_CLIENT_ID = os.getenv("COGNITO_CLIENT_ID")
COGNITO_DOMAIN = os.getenv("COGNITO_DOMAIN")
COGNITO_REDIRECT_URI = os.getenv("COGNITO_REDIRECT_URI")
COGNITO_LOGOUT_REDIRECT_URI = os.getenv("COGNITO_LOGOUT_REDIRECT_URI")
