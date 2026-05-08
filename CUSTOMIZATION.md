# 🎨 Customization Guide

## Quick Personalization Steps

Follow these steps to make the portfolio truly yours!

---

## 📝 Step 1: Update Your Basic Information

### Edit Home Page (`portfolio/templates/portfolio/home.html`)

Find and update:

```html
<!-- Update your name -->
<h1 class="name">Your Name Here</h1>

<!-- Update your title/profession -->
<p class="title">Marine Science Engineer</p>

<!-- Update your bio -->
<p class="bio">
  Passionate about marine conservation and sustainable fisheries...
</p>

<!-- Update your location and contact -->
<p>📍 Location: Your City, Country</p>
<p>📧 Email: your.email@example.com</p>
```

### Edit About Page (`portfolio/templates/portfolio/about.html`)

Update:

```html
<!-- Update biography -->
<p>Born and raised in...</p>

<!-- Update interests -->
<li>Marine Conservation</li>
<li>Sustainable Fisheries</li>
<li>Your Interest</li>

<!-- Update career goals -->
<p>My goal is to...</p>
```

### Edit Contact Page (`portfolio/templates/portfolio/contact.html`)

Update contact information:

```html
<!-- Email -->
<a href="mailto:your-email@example.com">your-email@example.com</a>

<!-- Phone -->
<a href="tel:+1234567890">+1 (234) 567-890</a>

<!-- Location -->
<p>Your City, Country</p>

<!-- Social Links -->
<a href="https://github.com/yourname">GitHub</a>
<a href="https://linkedin.com/in/yourname">LinkedIn</a>
```

---

## 🎨 Step 2: Customize Colors

### Edit `portfolio/static/css/style.css`

Find the `:root` section (top of file) and update:

```css
:root {
  /* Primary Colors - Change these! */
  --primary-color: #0066cc; /* Main brand color */
  --secondary-color: #1e3c72; /* Dark backgrounds */
  --cyan: #00d4ff; /* Accent color */

  /* Marine Theme Colors */
  --ocean-dark: #004d7a;
  --ocean-light: #1ba0c8;
  --sand: #f4e4c1;
  --marine-green: #2d8659;

  /* Neutral Colors */
  --text-light: #333; /* Light mode text */
  --bg-light: #f8f9fa; /* Light mode background */
  --border-light: #ddd;

  /* Dark Mode Colors */
  --text-dark: #fff; /* Dark mode text */
  --bg-dark: #1a1a1a; /* Dark mode background */
  --card-dark: #2d2d2d;
}
```

### Color Ideas for Marine Theme:

```css
/* Option 1: Deep Ocean */
--primary-color: #004d99;
--secondary-color: #003d7a;
--cyan: #00d9ff;

/* Option 2: Teal Water */
--primary-color: #0088aa;
--secondary-color: #004d77;
--cyan: #00d4ff;

/* Option 3: Sunset Sea */
--primary-color: #d4622d;
--secondary-color: #8b4513;
--cyan: #ff9800;
```

---

## 🖼️ Step 3: Add Your Profile Picture

1. **Prepare image:**
   - Size: 300x300px (minimum)
   - Format: JPG or PNG
   - File size: Under 500KB

2. **Place image:**
   - Save as: `portfolio/static/images/profile.jpg`

3. **Update templates:**

   In `home.html`:

   ```html
   <img
     src="{% static 'images/profile.jpg' %}"
     alt="Profile"
     class="profile-img"
   />
   ```

   In `about.html`:

   ```html
   <img
     src="{% static 'images/profile.jpg' %}"
     alt="Profile"
     class="profile-img"
   />
   ```

---

## 📄 Step 4: Add Content via Admin Panel

### 1. Start Server

```bash
python manage.py runserver
```

### 2. Access Admin

Go to: `http://localhost:8000/admin/`

### 3. Add Your Information

#### Add Education

- Click **Education**
- Click **Add Education**
- Fill in your school, degree, dates
- Save

#### Add Skills

- Click **Skills**
- Click **Add Skill**
- Add: Python, Django, MySQL, etc.
- Set proficiency (0-100)
- Save

#### Add Projects

- Click **Projects**
- Click **Add Project**
- Upload project image
- Add description and links
- Mark as featured if important
- Save

#### Add Research/Publications

- Click **Research Items**
- Click **Add Research Item**
- Select type (Research, Publication, etc.)
- Fill in details
- Save

#### Add Certifications

- Click **Certifications**
- Click **Add Certification**
- Add certificate details
- Save

---

## 🎯 Step 5: Customize Navigation Links

Edit `portfolio/templates/base.html`:

```html
<!-- Main Navigation -->
<nav class="navbar">
  <!-- Add your custom links here -->
  <a href="{% url 'home' %}">Home</a>
  <a href="{% url 'about' %}">About</a>
  <a href="{% url 'skills' %}">Skills</a>
  <a href="{% url 'projects' %}">Projects</a>
  <!-- Add custom links -->
  <a href="https://blog.yourdomain.com">Blog</a>
  <a href="https://cv.yourdomain.com">CV</a>
</nav>
```

---

## 🔤 Step 6: Update Footer

Edit footer in `portfolio/templates/base.html`:

```html
<footer>
  <!-- Update copyright -->
  <p>&copy; 2024 Your Name. All rights reserved.</p>

  <!-- Update social links -->
  <a href="https://github.com/yourname">GitHub</a>
  <a href="https://linkedin.com/in/yourname">LinkedIn</a>
  <a href="https://twitter.com/yourname">Twitter</a>
  <a href="https://instagram.com/yourname">Instagram</a>
</footer>
```

---

## 📱 Step 7: Customize Typography

Edit `style.css`:

```css
:root {
  /* Fonts */
  --font-main: "Poppins", sans-serif; /* Change main font */
  --font-heading: "Playfair Display", serif; /* Change heading font */
  --font-mono: "Courier New", monospace; /* Code font */

  /* Font Sizes */
  --fs-base: 16px;
  --fs-lg: 18px;
  --fs-xl: 24px;
  --fs-xxl: 32px;
  --fs-h1: 48px;
}
```

### Font Import (add to style.css top):

```css
@import url("https://fonts.googleapis.com/css2?family=Poppins:wght@400;600;700&family=Playfair+Display:wght@600;700&display=swap");
```

---

## 🌙 Step 8: Customize Dark Mode

The dark mode is automatic. Customize colors in `style.css`:

```css
body.dark-mode {
  background-color: #1a1a1a;
  color: #fff;
}

body.dark-mode .card {
  background-color: #2d2d2d;
}

body.dark-mode .navbar {
  background-color: #0a0a0a;
}
```

---

## ⚡ Step 9: Customize Animations

### Change animation speed in `main.js`:

```javascript
// AOS animation options
AOS.init({
  duration: 1000, // Change animation duration
  offset: 100, // Trigger distance
  easing: "ease-out", // Animation easing
});
```

### Or in `style.css`:

```css
@keyframes slideIn {
  from {
    opacity: 0;
    transform: translateX(-50px);
  }
  to {
    opacity: 1;
    transform: translateX(0);
  }
}

.hero-section {
  animation: slideIn 0.8s ease-out; /* Change duration here */
}
```

---

## 📧 Step 10: Setup Email (Optional)

### For Gmail:

1. Enable 2FA on Google account
2. Create App Password: https://myaccount.google.com/apppasswords
3. Create `.env` file:

```
EMAIL_HOST=smtp.gmail.com
EMAIL_PORT=587
EMAIL_HOST_USER=your-email@gmail.com
EMAIL_HOST_PASSWORD=your-app-password
```

### For other email providers, update `settings.py`:

```python
EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_HOST = 'smtp.yourmailprovider.com'
EMAIL_PORT = 587
EMAIL_USE_TLS = True
EMAIL_HOST_USER = 'your-email@example.com'
EMAIL_HOST_PASSWORD = 'your-password'
DEFAULT_FROM_EMAIL = 'your-email@example.com'
```

---

## 🔗 Step 11: Add Custom Pages

### Add a Blog Page

1. Create view in `views.py`:

```python
def blog(request):
    return render(request, 'portfolio/blog.html')
```

2. Add URL in `urls.py`:

```python
path('blog/', views.blog, name='blog'),
```

3. Create template `portfolio/templates/portfolio/blog.html`:

```html
{% extends 'base.html' %} {% block title %}Blog - My Portfolio{% endblock %} {%
block content %}
<section class="blog-section">
  <h1>Blog Posts</h1>
  <!-- Add blog content -->
</section>
{% endblock %}
```

4. Add link in `base.html` navigation

---

## 🎨 Step 12: Customize Component Styles

### Project Cards (`style.css`):

```css
.project-card {
  background: linear-gradient(135deg, #0066cc, #00d4ff);
  border-radius: 15px;
  box-shadow: 0 10px 30px rgba(0, 102, 204, 0.2);
  padding: 25px;
  transition: all 0.3s ease;
}

.project-card:hover {
  transform: translateY(-10px);
  box-shadow: 0 20px 40px rgba(0, 102, 204, 0.3);
}
```

### Buttons:

```css
.btn-primary {
  background-color: var(--primary-color);
  border-radius: 8px;
  padding: 12px 24px;
  transition: all 0.3s ease;
}

.btn-primary:hover {
  background-color: var(--secondary-color);
  transform: translateY(-2px);
  box-shadow: 0 5px 15px rgba(0, 102, 204, 0.3);
}
```

---

## 🎯 Step 13: SEO Customization

Update in `base.html`:

```html
<head>
  <!-- Update title -->
  <title>
    {% block title %}Your Name - Marine Science Portfolio{% endblock %}
  </title>

  <!-- Update description -->
  <meta
    name="description"
    content="Professional portfolio of [Your Name], Marine Science & Engineering student"
  />

  <!-- Update author -->
  <meta name="author" content="Your Name" />

  <!-- Open Graph (for social sharing) -->
  <meta property="og:title" content="Your Name - Portfolio" />
  <meta property="og:description" content="Your bio here" />
  <meta property="og:image" content="{% static 'images/profile.jpg' %}" />

  <!-- Twitter Card -->
  <meta name="twitter:card" content="summary" />
  <meta name="twitter:creator" content="@yourname" />
</head>
```

---

## 🔄 Step 14: Update Favicon

1. Create a favicon (32x32px PNG)
2. Save as: `portfolio/static/images/favicon.png`
3. Add to `base.html`:

```html
<link rel="icon" type="image/png" href="{% static 'images/favicon.png' %}" />
```

---

## 🚀 Step 15: Test Your Changes

After each customization:

1. **Refresh the page**: Ctrl+F5 (force refresh)
2. **Check all pages**: Home, About, Skills, Projects, etc.
3. **Test responsiveness**: Resize browser window
4. **Test dark mode**: Click theme toggle
5. **Test forms**: Submit contact form
6. **Check links**: Ensure all links work

---

## 🎨 Color Palette Ideas

### Option 1: Marine Blues

```
Primary: #0066cc (Bright Blue)
Secondary: #1e3c72 (Navy)
Accent: #00d4ff (Cyan)
```

### Option 2: Ocean Teals

```
Primary: #0f8b8d (Teal)
Secondary: #0a5359 (Dark Teal)
Accent: #2dd4bf (Light Cyan)
```

### Option 3: Deep Sea

```
Primary: #003f5c (Very Dark Blue)
Secondary: #004e89 (Dark Blue)
Accent: #1f77b4 (Azure)
```

### Option 4: Coral Reef

```
Primary: #d9725a (Coral)
Secondary: #8b4513 (Brown)
Accent: #20b2aa (Sea Green)
```

---

## 📸 Image Optimization

For best performance:

1. **Resize images**: Max 1200px width
2. **Compress**: Use TinyPNG or similar
3. **Optimize**: Use tools like ImageOptim
4. **Format**: JPG for photos, PNG for graphics
5. **Size**: Keep under 500KB per image

```bash
# On Mac/Linux using ImageMagick
convert image.jpg -resize 1200x800 -quality 80 image-optimized.jpg
```

---

## 🔐 Security Customizations

### Update SECRET_KEY:

```python
# settings.py
from django.core.management.utils import get_random_secret_key
SECRET_KEY = get_random_secret_key()
```

### Set DEBUG for production:

```python
DEBUG = False  # In production!
ALLOWED_HOSTS = ['yourdomain.com', 'www.yourdomain.com']
```

---

## 📋 Customization Checklist

- [ ] Updated name and bio
- [ ] Changed colors
- [ ] Added profile picture
- [ ] Updated contact information
- [ ] Added education entries
- [ ] Added skills
- [ ] Added projects
- [ ] Updated social links
- [ ] Customized navigation
- [ ] Updated footer
- [ ] Tested dark mode
- [ ] Tested responsive design
- [ ] Tested all forms
- [ ] Updated SEO information
- [ ] Added favicon

---

## 🆘 Common Customization Issues

### Images not showing?

- Check file path: `portfolio/static/images/filename.ext`
- Run `python manage.py collectstatic`
- Clear browser cache (Ctrl+Shift+Delete)

### Styles not updating?

- Clear browser cache
- Hard refresh (Ctrl+F5)
- Check for typos in CSS class names
- Ensure CSS file is loaded

### Changes not showing?

- Stop and restart server
- Reload page (not cached)
- Check file was saved
- Look for error messages in console

---

## 💡 Pro Tips

1. **Create backup** before major changes
2. **Test locally** before deploying
3. **Use browser DevTools** (F12) to test styles
4. **Version control** with Git
5. **Keep documentation** of changes
6. **Ask for feedback** from friends
7. **Monitor analytics** for popular pages

---

## 📚 Additional Resources

- Google Fonts: https://fonts.google.com/
- Color Palettes: https://coolors.co/
- Image Optimization: https://tinypng.com/
- CSS Generator: https://cssgenerator.org/
- Font Awesome Icons: https://fontawesome.com/icons

---

**Your portfolio is now fully customizable! Make it uniquely yours! 🌊✨**

**Happy customizing! 🎨**
