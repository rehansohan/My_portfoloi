# Deployment Guide

## Overview

This guide covers deployment options for your Django portfolio website. Choose the platform that best suits your needs.

## Deployment Platforms

### 1. Render.com (Recommended for Beginners)

**Pros:** Easy setup, free tier available, free SSL

**Steps:**

1. Create account at https://render.com
2. Push your code to GitHub
3. Click "New +" and select "Web Service"
4. Connect your GitHub repository
5. Configure settings:
   ```
   Name: portfolio-website
   Environment: Python 3
   Build Command: pip install -r requirements.txt && python manage.py migrate && python manage.py collectstatic --noinput
   Start Command: gunicorn portfolio_config.wsgi:application
   ```
6. Add Environment Variables:
   - `SECRET_KEY`: Generate new key (python -c 'from django.core.management.utils import get_random_secret_key; print(get_random_secret_key())')
   - `DEBUG`: false
   - `ALLOWED_HOSTS`: your-domain.render.com
7. Click "Create Web Service"
8. Wait for deployment to complete

**Cost:** Free tier available (limited)

---

### 2. Railway.app (Great for Students)

**Pros:** Generous free tier, simple interface, good performance

**Steps:**

1. Go to https://railway.app
2. Sign up with GitHub
3. Create new project
4. Import from GitHub
5. Configure:
   ```
   PORT: 8000 (Railway sets this automatically)
   Python version: 3.11
   ```
6. Add Environment Variables in project settings
7. Deploy

**Cost:** $5 free credit monthly, pay-as-you-go after that

---

### 3. PythonAnywhere

**Pros:** No DevOps knowledge needed, good for beginners

**Steps:**

1. Create account at https://www.pythonanywhere.com
2. Upload files via web interface or Git
3. Create virtual environment:
   ```
   mkvirtualenv --python=/usr/bin/python3.9 mysite
   pip install -r requirements.txt
   ```
4. Set up Django app in Web tab
5. Configure WSGI file
6. Reload web app

**Cost:** Free tier available (limited), paid plans start at $5/month

---

### 4. Heroku (Legacy Option)

**Note:** Heroku free tier is being phased out. Consider Render or Railway instead.

---

## Pre-Deployment Checklist

- [ ] Change `SECRET_KEY` in settings.py

  ```python
  python -c 'from django.core.management.utils import get_random_secret_key; print(get_random_secret_key())'
  ```

- [ ] Set `DEBUG = False`

  ```python
  DEBUG = False
  ```

- [ ] Update `ALLOWED_HOSTS`

  ```python
  ALLOWED_HOSTS = ['yourdomain.com', 'www.yourdomain.com']
  ```

- [ ] Configure static files

  ```python
  STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')
  STATIC_URL = '/static/'
  ```

- [ ] Test locally with `DEBUG = False`

  ```bash
  python manage.py runserver --settings=portfolio_config.settings
  ```

- [ ] Create `.env` file (keep secrets local)

  ```
  SECRET_KEY=your-key
  DEBUG=False
  ALLOWED_HOSTS=yourdomain.com
  ```

- [ ] Collect static files

  ```bash
  python manage.py collectstatic --noinput
  ```

- [ ] Create `Procfile` (included)
  ```
  web: gunicorn portfolio_config.wsgi:application
  release: python manage.py migrate
  ```

---

## Environment Variables

Create `.env` file locally (not pushed to GitHub):

```
SECRET_KEY=your-super-secret-key
DEBUG=False
ALLOWED_HOSTS=yourdomain.com,www.yourdomain.com
DATABASE_URL=your-database-url
EMAIL_HOST_USER=your-email@gmail.com
EMAIL_HOST_PASSWORD=your-app-password
```

---

## Database for Production

### Option 1: Use Render PostgreSQL

1. In Render, create new PostgreSQL database
2. Copy connection string
3. Add to environment variables:
   ```
   DATABASE_URL=postgresql://user:password@host:5432/dbname
   ```

### Option 2: Use Railway PostgreSQL

1. Create PostgreSQL plugin in Railway
2. Railway automatically sets DATABASE_URL
3. No additional configuration needed

### Option 3: Keep SQLite (Not Recommended)

SQLite works but has limitations. Consider PostgreSQL for production.

---

## Static Files & Media

### Using Render/Railway

Static files are collected during build process. Make sure:

1. `STATIC_ROOT` is set correctly
2. Run `collectstatic` in build command
3. Serve from platform's built-in static file support

### Using AWS S3 (Optional)

For better performance, use AWS S3:

1. Create S3 bucket
2. Install `django-storages`
3. Configure in settings.py:

   ```python
   INSTALLED_APPS += ['storages']

   AWS_STORAGE_BUCKET_NAME = 'your-bucket'
   AWS_S3_REGION_NAME = 'us-east-1'
   STATIC_URL = f'https://{AWS_STORAGE_BUCKET_NAME}.s3.amazonaws.com/static/'
   ```

---

## SSL/HTTPS

Most platforms provide free SSL:

- **Render**: Automatic
- **Railway**: Automatic
- **PythonAnywhere**: Free with verified domain

Update settings.py for production:

```python
if not DEBUG:
    SECURE_SSL_REDIRECT = True
    SESSION_COOKIE_SECURE = True
    CSRF_COOKIE_SECURE = True
```

---

## Email Configuration (Optional)

For sending emails from contact form:

```python
EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_HOST = 'smtp.gmail.com'
EMAIL_PORT = 587
EMAIL_USE_TLS = True
EMAIL_HOST_USER = 'your-email@gmail.com'
EMAIL_HOST_PASSWORD = 'your-app-password'  # Not your regular password!
```

To get Gmail app password:

1. Enable 2-factor authentication
2. Go to https://myaccount.google.com/apppasswords
3. Generate app password
4. Use in EMAIL_HOST_PASSWORD

---

## Domain Setup

### Point Domain to Render

1. Get Render domain from project settings
2. In domain registrar, update DNS records:
   ```
   CNAME: yourdomain.com -> your-app.render.com
   ```
3. Wait for DNS to propagate (up to 48 hours)
4. Enable auto-renewal of certificates

### Point Domain to Railway

1. Get Railway domain
2. Update DNS records
3. Configure in Railway project settings

---

## Monitoring & Logs

### Render Logs

```
In Render dashboard → Logs tab
```

### Railway Logs

```
In Railway app → Deployments → Logs
```

### Common Issues

**502 Bad Gateway**

- Check application logs
- Verify start command
- Check if app crashes on startup

**Static files not loading**

- Run `collectstatic` command
- Check `STATIC_ROOT` setting
- Verify file permissions

**Database connection error**

- Check `DATABASE_URL` format
- Verify database is running
- Check credentials

---

## Deployment Commands Reference

```bash
# Collect static files
python manage.py collectstatic --noinput

# Create database backup
python manage.py dumpdata > backup.json

# Apply migrations
python manage.py migrate

# Create superuser on production
python manage.py createsuperuser

# Check for issues
python manage.py check --deploy
```

---

## Security Checklist

- [ ] `SECRET_KEY` changed
- [ ] `DEBUG = False`
- [ ] `ALLOWED_HOSTS` configured
- [ ] HTTPS enabled
- [ ] Database credentials secured
- [ ] Email credentials use app password
- [ ] No sensitive data in code
- [ ] Static files collected
- [ ] CSRF protection enabled
- [ ] Session security configured

---

## Custom Domain

1. Purchase domain from registrar (GoDaddy, Namecheap, etc.)
2. Update DNS records to point to your hosting
3. Wait for DNS propagation
4. Add custom domain in platform settings
5. Update `ALLOWED_HOSTS` in Django

---

## Getting Help

- **Render Support**: https://support.render.com
- **Railway Help**: https://docs.railway.app
- **PythonAnywhere Help**: https://www.pythonanywhere.com/help/
- **Django Docs**: https://docs.djangoproject.com/

---

## After Deployment

1. Test all functionality
2. Check admin panel access
3. Test contact form
4. Verify images load
5. Test on mobile
6. Monitor logs for errors
7. Set up error monitoring (Sentry.io)
8. Configure email alerts

---

**Good luck with your deployment! 🚀**
