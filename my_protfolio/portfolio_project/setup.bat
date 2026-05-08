@echo off
REM Setup script for Portfolio Website (Windows)
REM Run this script to quickly set up the Django project

echo.
echo 🌊 Portfolio Website Setup Script (Windows)
echo ==========================================
echo.

REM Check Python version
python --version
if %errorlevel% neq 0 (
    echo ❌ Python is not installed or not in PATH
    pause
    exit /b 1
)

echo ✓ Python found

REM Create virtual environment
echo.
echo 📦 Creating virtual environment...
python -m venv venv

if %errorlevel% neq 0 (
    echo ❌ Failed to create virtual environment
    pause
    exit /b 1
)

REM Activate virtual environment
echo 🔄 Activating virtual environment...
call venv\Scripts\activate.bat

REM Install dependencies
echo.
echo 📥 Installing dependencies...
pip install -r requirements.txt

if %errorlevel% neq 0 (
    echo ❌ Failed to install dependencies
    pause
    exit /b 1
)

REM Navigate to project directory
cd portfolio_project

REM Create database
echo.
echo 🗄️  Creating database...
python manage.py migrate

if %errorlevel% neq 0 (
    echo ⚠️  Warning: Migration issues (usually safe to continue)
)

REM Create superuser
echo.
echo 👤 Creating superuser account...
echo You will be prompted to enter admin credentials.
python manage.py createsuperuser

REM Collect static files
echo.
echo 📁 Collecting static files...
python manage.py collectstatic --noinput

REM Summary
echo.
echo ==========================================
echo ✅ Setup Complete!
echo ==========================================
echo.
echo Next steps:
echo 1. Virtual environment is already activated
echo 2. Start development server:
echo    python manage.py runserver
echo 3. Access your portfolio:
echo    http://localhost:8000/
echo 4. Access admin panel:
echo    http://localhost:8000/admin/
echo.
echo 🌊 Happy building!
echo.
pause
