# Troubleshooting Guide

## 🆘 Common Issues and Solutions

### ❌ Virtual Environment Issues

#### Problem: "venv command not found"

**Solution (Windows):**

```bash
python -m venv venv
venv\Scripts\activate
```

**Solution (Mac/Linux):**

```bash
python3 -m venv venv
source venv/bin/activate
```

---

#### Problem: "virtualenv not recognized"

**Solution:**

```bash
# First, ensure venv is installed
python -m ensurepip --upgrade

# Then create virtual environment
python -m venv venv
```

---

### ❌ Dependency Installation Issues

#### Problem: "pip install failed" or "No module named X"

**Solution:**

```bash
# Upgrade pip first
pip install --upgrade pip

# Clear pip cache
pip cache purge

# Try installing again
pip install -r requirements.txt
```

---

#### Problem: "Permission denied" during pip install

**Solution (Mac/Linux):**

```bash
pip install --user -r requirements.txt
# OR use sudo (not recommended)
sudo pip install -r requirements.txt
```

**Solution (Windows):**

```bash
# Run Command Prompt as Administrator
pip install -r requirements.txt
```

---

### ❌ Database Issues

#### Problem: "No such table: portfolio_project"

**Solution:**

```bash
# Run migrations
python manage.py migrate

# Check migration status
python manage.py showmigrations
```

---

#### Problem: "Database is locked" (SQLite)

**Solution:**

```bash
# Remove database and start fresh
rm db.sqlite3

# Create new database
python manage.py migrate

# Create superuser again
python manage.py createsuperuser
```

**Alternative:**
Use PostgreSQL for production instead of SQLite.

---

#### Problem: "IntegrityError" or "Database error"

**Solution:**

```bash
# Check for data corruption
python manage.py check

# Clear and rebuild
python manage.py flush
python manage.py migrate
python manage.py createsuperuser
```

---

### ❌ Server Issues

#### Problem: "Port 8000 already in use"

**Solution:**

```bash
# Use different port
python manage.py runserver 8001

# Or kill process using port 8000
# Windows:
netstat -ano | findstr :8000
taskkill /PID <PID> /F

# Mac/Linux:
lsof -i :8000
kill -9 <PID>
```

---

#### Problem: "Address already in use"

**Solution:**

```bash
# Wait a few seconds and try again
# OR use different port
python manage.py runserver 127.0.0.1:8001
```

---

#### Problem: "Connection refused" when accessing localhost

**Solution:**

1. Check if Django server is running
2. Ensure correct URL: http://127.0.0.1:8000/ (not localhost)
3. Check firewall settings
4. Try: python manage.py runserver 0.0.0.0:8000

---

### ❌ Admin Panel Issues

#### Problem: "Can't log in to admin panel"

**Solution:**

```bash
# Reset superuser
python manage.py changepassword <username>

# Or create new superuser
python manage.py createsuperuser
```

---

#### Problem: "Admin page shows 'Page not found'"

**Solution:**

1. Check URL: http://localhost:8000/admin/
2. Verify you've run migrations
3. Check urls.py configuration

---

#### Problem: "Static files not loading in admin"

**Solution:**

```bash
# Collect static files
python manage.py collectstatic --noinput

# Clear browser cache
# Ctrl+Shift+Delete in Chrome/Firefox
```

---

### ❌ Static Files Issues

#### Problem: "CSS/JavaScript not loading" or "Images not showing"

**Solution:**

```bash
# Collect static files
python manage.py collectstatic --clear --noinput

# Check STATIC_URL in settings.py
# Should be: /static/

# Verify files in portfolio/static/ directory
```

---

#### Problem: "404 error for static files"

**Solution:**

1. Check `DEBUG` setting in settings.py:

   ```python
   DEBUG = True  # For development
   ```

2. Verify STATIC_ROOT and STATIC_URL in settings.py

3. Run collectstatic:
   ```bash
   python manage.py collectstatic --noinput
   ```

---

### ❌ Template Issues

#### Problem: "TemplateDoesNotExist" error

**Solution:**

1. Check template file exists in correct location:

   ```
   portfolio/templates/portfolio/home.html
   ```

2. Verify TEMPLATES setting in settings.py:

   ```python
   'DIRS': [os.path.join(BASE_DIR, 'portfolio', 'templates')],
   ```

3. Check for typos in template path

---

#### Problem: "Invalid block tag" in template

**Solution:**

1. Check template syntax
2. Ensure proper Django template tags
3. Match opening and closing tags:
   ```django
   {% block content %}...{% endblock %}
   ```

---

### ❌ Form Issues

#### Problem: "CSRF token missing" error

**Solution:**

1. Include CSRF token in form:

   ```django
   <form method="POST">
       {% csrf_token %}
       ...
   </form>
   ```

2. Or in views.py, ensure CSRF middleware is enabled

---

#### Problem: "Form validation failed"

**Solution:**

1. Check form.is_valid()
2. View error messages: form.errors
3. Verify all required fields filled
4. Check email format for email fields

---

### ❌ Image Issues

#### Problem: "Images not displaying"

**Solution:**

1. Check MEDIA_URL and MEDIA_ROOT in settings.py
2. Ensure media directory exists: `mkdir media`
3. Check file permissions
4. Verify image format (JPG, PNG, WebP)
5. Try uploading again

---

#### Problem: "Pillow not installed" or "PIL error"

**Solution:**

```bash
pip install Pillow
pip install --upgrade Pillow
```

---

### ❌ Model Issues

#### Problem: "No migrations for app 'portfolio'"

**Solution:**

```bash
# Create migrations
python manage.py makemigrations

# Apply migrations
python manage.py migrate

# Check migration status
python manage.py showmigrations
```

---

#### Problem: "Column does not exist" database error

**Solution:**

1. Run migrations:

   ```bash
   python manage.py migrate
   ```

2. Or reset database:
   ```bash
   rm db.sqlite3
   python manage.py migrate
   python manage.py createsuperuser
   ```

---

### ❌ Python/Environment Issues

#### Problem: "ModuleNotFoundError: No module named 'django'"

**Solution:**

1. Activate virtual environment:

   ```bash
   # Windows
   venv\Scripts\activate
   # Mac/Linux
   source venv/bin/activate
   ```

2. Install requirements:
   ```bash
   pip install -r requirements.txt
   ```

---

#### Problem: "Command 'python' not found"

**Solution:**

Use `python3` instead of `python`:

```bash
python3 manage.py runserver
```

Or add Python to PATH (Windows)

---

### ❌ Deployment Issues

#### Problem: "DEBUG = True in production"

**Solution:**

Set in settings.py for production:

```python
DEBUG = False
ALLOWED_HOSTS = ['yourdomain.com', 'www.yourdomain.com']
```

---

#### Problem: "Secret key exposed" warning

**Solution:**

Generate new SECRET_KEY:

```python
from django.core.management.utils import get_random_secret_key
print(get_random_secret_key())
```

---

#### Problem: "Static files not found on Render/Railway"

**Solution:**

In Procfile, ensure static collection:

```
web: gunicorn portfolio_config.wsgi:application
release: python manage.py migrate && python manage.py collectstatic --noinput
```

---

### ❌ Email/Contact Form Issues

#### Problem: "Contact form not sending emails"

**Solution:**

1. Check EMAIL_BACKEND in settings.py
2. For testing, use:
   ```python
   EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'
   ```
3. Messages appear in console
4. For production, configure SMTP

---

#### Problem: "Gmail SMTP authentication failed"

**Solution:**

1. Use Gmail App Password (not regular password)
2. Enable 2-factor authentication first
3. Get app password from: https://myaccount.google.com/apppasswords
4. Update settings:
   ```python
   EMAIL_HOST_USER = 'your-email@gmail.com'
   EMAIL_HOST_PASSWORD = 'app-password-here'  # 16 characters
   ```

---

### ❌ Browser/Client Issues

#### Problem: "Page looks weird" or "Styling broken"

**Solution:**

1. Clear browser cache:
   - Chrome/Firefox: Ctrl+Shift+Delete
   - Safari: Cmd+Shift+Delete
2. Hard refresh: Ctrl+F5
3. Try different browser
4. Check browser console for errors (F12)

---

#### Problem: "Responsive design not working on mobile"

**Solution:**

1. Check viewport meta tag in base.html:

   ```html
   <meta name="viewport" content="width=device-width, initial-scale=1.0" />
   ```

2. Clear browser cache
3. Test with device's actual resolution
4. Check CSS media queries

---

## 🔧 Debugging Tips

### Enable Django Debug Mode

```python
# In settings.py
DEBUG = True
```

Then check console output and error pages for details.

### Use Django Shell

```bash
python manage.py shell

# Check database
from portfolio.models import Project
Project.objects.all()
```

### View Logs

```bash
# Check Django logs (if configured)
# Windows: Check console output
# Mac/Linux: tail -f logs/django.log
```

### Use Print Statements

```python
# In views.py
print(f"Debug: {variable_name}")
```

Check console output for debugging.

---

## 📞 Getting Help

1. **Check this guide** first
2. **Google the error message**
3. **Check Django documentation**: https://docs.djangoproject.com/
4. **Stack Overflow**: Tag your question with 'django'
5. **Ask in Django community**: https://www.djangoproject.com/community/

---

## ✅ Preventive Maintenance

### Regular Backups

```bash
python manage.py dumpdata > backup_$(date +%Y%m%d).json
```

### Monitor Logs

Check console output regularly for warnings

### Update Dependencies

```bash
pip install --upgrade pip
pip install -r requirements.txt --upgrade
```

### Test Functionality

Regularly test all pages and features

---

**Still stuck? Try searching for your exact error message on Stack Overflow or Django forums!** 🔍

**Happy troubleshooting! 🚀**
