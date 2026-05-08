# Professional Portfolio Website - Marine Science & Engineering

A modern, responsive Django-based portfolio website designed specifically for Fisheries & Marine Science and Engineering students. Features a clean UI, dynamic content management, and deployment-ready configuration.

## 🌊 Features

### Core Features

- ✨ Modern, responsive design optimized for all devices
- 🌙 Dark/Light mode toggle with localStorage persistence
- 🎨 Beautiful gradient hero section with typing animation
- 📊 Skills section with animated progress bars
- 🚀 Dynamic project showcase with admin management
- 📝 Research & publications tracking
- 🏆 Certifications and credentials display
- 📧 Working contact form with database storage
- 🔗 Social media integration
- ♿ Accessibility optimized

### Technical Features

- Django admin panel for content management
- SQLite database (easily upgradeable to PostgreSQL)
- RESTful API endpoints for skills and projects
- Smooth scroll animations with AOS
- Form validation and error handling
- SEO optimized structure
- Mobile-first responsive design
- Performance optimized

### Color Scheme

- Ocean Blue: `#0066cc`
- Dark Navy: `#1e3c72`
- Cyan Accent: `#00d4ff`
- Light Background: `#f8f9fa`

## 📋 Prerequisites

- Python 3.8+
- pip (Python package manager)
- Virtual environment tool (venv)

## 🚀 Installation & Setup

### Step 1: Clone/Download the Project

```bash
cd your-portfolio-directory
```

### Step 2: Create Virtual Environment

```bash
# Windows
python -m venv venv
venv\Scripts\activate

# macOS/Linux
python3 -m venv venv
source venv/bin/activate
```

### Step 3: Install Dependencies

```bash
pip install -r requirements.txt
```

### Step 4: Navigate to Project Directory

```bash
cd portfolio_project
```

### Step 5: Create Database

```bash
python manage.py migrate
```

### Step 6: Create Superuser (Admin Account)

```bash
python manage.py createsuperuser
# Follow the prompts to create your admin account
```

### Step 7: Collect Static Files (Optional for Development)

```bash
python manage.py collectstatic --noinput
```

### Step 8: Run Development Server

```bash
python manage.py runserver
```

The website will be available at: `http://127.0.0.1:8000/`

## 📱 Access Admin Panel

1. Navigate to: `http://127.0.0.1:8000/admin/`
2. Login with your superuser credentials
3. Add/edit your portfolio content:
   - Projects
   - Skills
   - Education
   - Research & Publications
   - Certifications
   - Contact Messages

## 📁 Project Structure

```
portfolio_project/
├── manage.py
├── requirements.txt
├── portfolio_config/
│   ├── __init__.py
│   ├── settings.py
│   ├── urls.py
│   ├── wsgi.py
│   └── asgi.py
├── portfolio/
│   ├── migrations/
│   ├── static/
│   │   ├── css/
│   │   │   ├── style.css (Main stylesheet)
│   │   │   └── responsive.css (Mobile responsive)
│   │   ├── js/
│   │   │   └── main.js (Interactive features)
│   │   └── images/
│   ├── templates/
│   │   ├── base.html (Base template)
│   │   └── portfolio/
│   │       ├── home.html
│   │       ├── about.html
│   │       ├── skills.html
│   │       ├── projects.html
│   │       ├── project_detail.html
│   │       ├── research.html
│   │       ├── certifications.html
│   │       └── contact.html
│   ├── admin.py (Admin configuration)
│   ├── apps.py
│   ├── forms.py (Contact form)
│   ├── models.py (Database models)
│   ├── urls.py (URL routing)
│   └── views.py (View functions)
```

## 🗄️ Database Models

### Project

- title, description, technologies
- image, github_link, live_demo_link
- featured status, timestamps

### Skill

- name, category, proficiency (0-100)
- icon for display

### Education

- institution, degree, field_of_study
- start_date, end_date, CGPA, description

### Research

- title, type (research/publication/conference/fieldwork)
- description, authors, journal_name
- publication_date, URL, image

### Certification

- name, issuer, dates (issue/expiry)
- credential_url, credential_id, image

### ContactMessage

- name, email, phone, subject, message
- read status, timestamp

## 🛠️ Customization

### Update Personal Information

1. Edit in Django Admin or directly in templates
2. Key files to update:
   - `portfolio/templates/portfolio/home.html` - Hero section
   - `portfolio/templates/portfolio/about.html` - About Me content
   - `portfolio/templates/base.html` - Footer contact info

### Add Your Profile Image

1. Create `portfolio/static/images/` directory
2. Add your profile image: `profile.jpg`
3. Update `home.html` to use your image

### Change Color Scheme

Edit CSS variables in `portfolio/static/css/style.css`:

```css
:root {
  --primary-color: #0066cc;
  --secondary-color: #1e3c72;
  --cyan: #00d4ff;
  /* ... other colors */
}
```

### Enable Email Sending

Update `portfolio_config/settings.py`:

```python
EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_HOST = 'your-email-provider.com'
EMAIL_PORT = 587
EMAIL_USE_TLS = True
EMAIL_HOST_USER = 'your-email@example.com'
EMAIL_HOST_PASSWORD = 'your-password'
```

## 🌐 Deployment

### Option 1: Render.com

1. Push code to GitHub
2. Connect GitHub repository to Render
3. Create new Web Service
4. Set build command: `pip install -r requirements.txt && python manage.py migrate && python manage.py collectstatic --noinput`
5. Set start command: `gunicorn portfolio_config.wsgi:application`
6. Add environment variables:
   - `SECRET_KEY`: Generate new key
   - `DEBUG`: False
   - `DATABASE_URL`: (if using PostgreSQL)

### Option 2: Railway

1. Push code to GitHub
2. Import GitHub repository to Railway
3. Add environment variables
4. Deploy

### Option 3: PythonAnywhere

1. Upload files to PythonAnywhere
2. Create virtual environment
3. Configure web app settings
4. Update WSGI file
5. Reload web app

### Pre-Deployment Checklist

- [ ] Change `SECRET_KEY` in settings.py
- [ ] Set `DEBUG = False`
- [ ] Update `ALLOWED_HOSTS`
- [ ] Configure database
- [ ] Set up email configuration
- [ ] Collect static files
- [ ] Create backup of database

## 📧 Contact Form

The contact form stores messages in the database. To view submitted messages:

1. Go to Django Admin
2. Click "Contact Messages"
3. View, mark as read, or delete messages

## 🔒 Security

- CSRF protection enabled
- SQL injection prevention
- XSS protection
- Secure password hashing
- Consider enabling HTTPS in production

## 📝 Adding Content

### Add a Project

1. Go to Admin: `/admin/`
2. Click "Projects"
3. Click "Add Project"
4. Fill in details and upload image
5. Save

### Add Skills

1. Admin → Skills
2. Add skill with proficiency level (0-100)
3. Choose category and icon

### Add Research

1. Admin → Research Items
2. Select type (research/publication/conference/fieldwork)
3. Add details
4. Save

## 🐛 Troubleshooting

### Port Already in Use

```bash
# Use different port
python manage.py runserver 8001
```

### Database Errors

```bash
# Reset database
rm db.sqlite3
python manage.py migrate
python manage.py createsuperuser
```

### Static Files Not Loading

```bash
python manage.py collectstatic --clear --noinput
```

### Images Not Showing

- Ensure `MEDIA_ROOT` directory exists
- Check file permissions
- Verify image path in admin

## 🎨 Customization Tips

1. **Change Font**: Update `@import` in CSS
2. **Add Sections**: Create new template and URL
3. **Modify Colors**: Edit CSS variables
4. **Add Features**: Create new models and views

## 📚 Technologies Used

- **Backend**: Django 4.2
- **Frontend**: HTML5, CSS3, Bootstrap 5, JavaScript
- **Database**: SQLite (Production: PostgreSQL)
- **Animations**: AOS, Typed.js
- **Icons**: Font Awesome 6.4
- **Fonts**: Google Fonts (Poppins, Roboto)

## 📄 License

This project is open source and available for personal use.

## 🤝 Support

For issues or questions:

1. Check existing documentation
2. Review Django documentation: https://docs.djangoproject.com/
3. Check Bootstrap documentation: https://getbootstrap.com/docs/

## 🎯 Next Steps

1. Customize personal information
2. Add your projects
3. Upload skills and certifications
4. Add profile image
5. Test on mobile devices
6. Deploy to chosen platform

## 📈 SEO Tips

1. Update meta descriptions
2. Add proper page titles
3. Use semantic HTML
4. Optimize images
5. Add structured data (Schema.org)
6. Create sitemap.xml
7. Submit to Google Search Console

## 🚀 Performance Tips

1. Optimize images (compress)
2. Enable caching
3. Minify CSS/JS
4. Use CDN for assets
5. Enable GZIP compression
6. Lazy load images

---

**Happy Building! 🌊🚀**

For the latest version and updates, visit: `https://github.com/yourusername/your-portfolio`
