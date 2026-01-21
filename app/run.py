#!/usr/bin/env python3
"""OAuth Security Dashboard - Flask Application Entry Point"""

from app import create_app

if __name__ == "__main__":
    app = create_app()
    # Use localhost for development security
    app.run(debug=True, host="127.0.0.1", port=5001)
