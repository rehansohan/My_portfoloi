"""
Quick Start Guide for Portfolio Website

This file provides quick reference commands for development and deployment.
"""

# ===== DEVELOPMENT =====

# 1. Create virtual environment
# Windows: python -m venv venv && venv\Scripts\activate
# Mac/Linux: python3 -m venv venv && source venv/bin/activate

# 2. Install dependencies
# pip install -r requirements.txt

# 3. Run migrations
# python manage.py migrate

# 4. Create superuser
# python manage.py createsuperuser

# 5. Run development server
# python manage.py runserver

# 6. Access admin
# http://localhost:8000/admin

# ===== MAINTENANCE =====

# Collect static files
# python manage.py collectstatic

# Create backup
# python manage.py dumpdata > backup.json

# Restore from backup
# python manage.py loaddata backup.json

# Make migrations
# python manage.py makemigrations

# Check for issues
# python manage.py check

# ===== DEPLOYMENT =====

# Render.com:
# 1. Push to GitHub
# 2. Create account on render.com
# 3. Create new Web Service
# 4. Connect GitHub repo
# 5. Set environment variables
# 6. Deploy

# Railway:
# 1. Push to GitHub
# 2. Create account on railway.app
# 3. Create new project
# 4. Import GitHub repo
# 5. Set environment variables
# 6. Deploy

# PythonAnywhere:
# 1. Upload files via web interface
# 2. Create virtual environment
# 3. Configure web app
# 4. Update WSGI file
# 5. Reload

# ===== CUSTOMIZATION =====

# Update profile information:
# - Edit portfolio/models.py for database schema
# - Update portfolio/views.py for logic
# - Modify templates in portfolio/templates/

# Add new pages:
# 1. Create view in views.py
# 2. Create URL pattern in urls.py
# 3. Create template in templates/portfolio/
# 4. Add navigation link in base.html

# Change colors:
# - Edit :root variables in portfolio/static/css/style.css

# ===== TROUBLESHOOTING =====

# Port in use:
# python manage.py runserver 8001

# Database errors:
# rm db.sqlite3
# python manage.py migrate
# python manage.py createsuperuser

# Static files not loading:
# python manage.py collectstatic --clear --noinput

# ===== USEFUL LINKS =====

# Django Documentation: https://docs.djangoproject.com/
# Bootstrap: https://getbootstrap.com/
# Font Awesome: https://fontawesome.com/
# AOS (Animate On Scroll): https://michalsnik.github.io/aos/
# Render Docs: https://render.com/docs
# Railway Docs: https://docs.railway.app/

print(__doc__)
