#!/bin/bash
# OAuth Security Dashboard - Startup Script

echo "Starting OAuth Security Dashboard..."
echo "Make sure you have configured your .env file in the app/ directory"
echo ""

cd app
python run.py
