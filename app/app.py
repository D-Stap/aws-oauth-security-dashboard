from datetime import datetime

import config
from auth.routes import auth_bp
from dashboard.routes import dashboard_bp
from flask import Flask, jsonify, render_template, session


def create_app():
    app = Flask(__name__, template_folder="templates")

    # Configuration
    app.config["SECRET_KEY"] = config.SECRET_KEY
    app.config["DEBUG"] = config.DEBUG

    # Add custom template filter for timestamp conversion
    @app.template_filter("timestamp_to_date")
    def timestamp_to_date(timestamp):
        """Convert Unix timestamp to readable date."""
        try:
            dt = datetime.fromtimestamp(int(timestamp))
            return dt.strftime("%Y-%m-%d %H:%M:%S")
        except (ValueError, TypeError):
            return "Invalid timestamp"

    # Register blueprints
    app.register_blueprint(auth_bp, url_prefix="/auth")
    app.register_blueprint(dashboard_bp, url_prefix="/dashboard")

    # Home route
    @app.route("/")
    def home():
        return render_template("home.html", user=session.get("user"))

    # Health check
    @app.route("/health")
    def health():
        return jsonify({
            "status": "healthy", 
            "service": "oauth-security-dashboard"
        })

    return app


if __name__ == "__main__":
    app = create_app()
    # Use localhost for development security
    app.run(debug=config.DEBUG, host="127.0.0.1", port=5000)
