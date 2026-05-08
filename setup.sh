#!/bin/bash
# Setup script for Portfolio Website
# Run this script to quickly set up the Django project

echo "🌊 Portfolio Website Setup Script"
echo "=================================="

# Check Python version
python_version=$(python --version 2>&1 | awk '{print $2}')
echo "✓ Python version: $python_version"

# Create virtual environment
echo ""
echo "📦 Creating virtual environment..."
python -m venv venv

# Activate virtual environment
echo "🔄 Activating virtual environment..."
source venv/bin/activate  # For macOS/Linux
# For Windows, use: venv\Scripts\activate

# Install dependencies
echo ""
echo "📥 Installing dependencies..."
pip install -r requirements.txt

# Navigate to project directory
cd portfolio_project

# Create database
echo ""
echo "🗄️  Creating database..."
python manage.py migrate

# Create superuser
echo ""
echo "👤 Creating superuser account..."
echo "You will be prompted to enter admin credentials."
python manage.py createsuperuser

# Collect static files
echo ""
echo "📁 Collecting static files..."
python manage.py collectstatic --noinput

# Summary
echo ""
echo "=================================="
echo "✅ Setup Complete!"
echo "=================================="
echo ""
echo "Next steps:"
echo "1. Activate virtual environment:"
echo "   source venv/bin/activate  (macOS/Linux)"
echo "   venv\Scripts\activate      (Windows)"
echo ""
echo "2. Start development server:"
echo "   cd portfolio_project"
echo "   python manage.py runserver"
echo ""
echo "3. Access your portfolio:"
echo "   http://localhost:8000/"
echo ""
echo "4. Access admin panel:"
echo "   http://localhost:8000/admin/"
echo ""
echo "🌊 Happy building!"
