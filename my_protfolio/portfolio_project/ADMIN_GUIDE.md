# Django Admin Panel Guide

## 🔐 Accessing the Admin Panel

1. Start the development server:

   ```bash
   python manage.py runserver
   ```

2. Go to: `http://localhost:8000/admin/`

3. Login with your superuser credentials (created during setup)

## 📊 Admin Dashboard Overview

The admin panel is organized by sections:

- **Projects** - Manage portfolio projects
- **Skills** - Manage your skills and proficiencies
- **Research** - Manage research items
- **Certifications** - Manage certifications and credentials
- **Contact Messages** - View contact form submissions
- **Education** - Manage education history

## 🚀 Adding Content

### 1. Adding a Project

1. Click **Projects** in the admin panel
2. Click **Add Project** (top right)
3. Fill in the form:
   ```
   Title: Project Name
   Description: Detailed project description
   Technologies: Python, Django, HTML, CSS (comma-separated)
   Image: Upload project screenshot/image
   GitHub Link: https://github.com/username/repo (optional)
   Live Demo Link: https://deployed-project.com (optional)
   Featured: Check if you want it on home page
   ```
4. Click **Save**

**Best Practices:**

- Use high-quality images (min 500px width)
- Write clear, engaging descriptions
- List all relevant technologies
- Include both GitHub and live demo links when possible
- Featured projects appear on home page (max 3)

### 2. Adding Skills

1. Click **Skills**
2. Click **Add Skill**
3. Fill in:
   ```
   Name: Python (or other skill)
   Category: Programming Languages
   Proficiency: 85 (0-100 scale)
   Icon: code (Font Awesome icon name, optional)
   ```
4. Click **Save**

**Categories:**

- Programming Languages
- Frameworks & Tools
- Data Analysis & Visualization
- Engineering Tools
- Soft Skills

**Proficiency Scale:**

- 0-30: Basic knowledge
- 30-60: Intermediate
- 60-80: Advanced
- 80-100: Expert

**Font Awesome Icons:** python, java, js-square, database, flask, django, etc.

### 3. Adding Education

1. Click **Education**
2. Click **Add Education**
3. Fill in:
   ```
   Institution: University Name
   Degree: Bachelor of Science
   Field of Study: Fisheries and Marine Science
   Start Date: 2020-01-15
   End Date: 2024-05-30 (leave blank if ongoing)
   CGPA: 3.8 (optional)
   Description: Course highlights, achievements
   ```
4. Click **Save**

### 4. Adding Research/Publications

1. Click **Research Items**
2. Click **Add Research Item**
3. Choose Research Type:
   - Research Topic
   - Publication
   - Conference Presentation
   - Fieldwork
4. Fill in fields relevant to type:
   ```
   Title: Research or publication title
   Description: Details about the research
   Authors: Your Name, Co-Author (if applicable)
   Journal Name: Journal name (for publications)
   Publication Date: Date of publication
   URL: Link to publication (optional)
   Image: Related image (optional)
   ```
5. Click **Save**

### 5. Adding Certifications

1. Click **Certifications**
2. Click **Add Certification**
3. Fill in:
   ```
   Name: Certification Name
   Issuer: Organization name
   Issue Date: When you got it
   Expiry Date: When it expires (leave blank if no expiry)
   Credential ID: Certificate ID (optional)
   Credential URL: Link to verify (optional)
   Image: Certificate image (optional)
   ```
4. Click **Save**

### 6. Viewing Contact Messages

1. Click **Contact Messages**
2. View submitted messages
3. Click on a message to see full details
4. Use Actions dropdown to:
   - Mark as read/unread
   - Delete messages
5. Sort by date or read status

## 🎯 Best Practices

### Project Management

- ✅ Update projects quarterly
- ✅ Include detailed descriptions
- ✅ Use professional images
- ✅ Keep GitHub links up-to-date
- ✅ Archive completed projects

### Skills Management

- ✅ Be honest about proficiency levels
- ✅ Update regularly as you learn
- ✅ Group related skills
- ✅ Use consistent naming

### Research Management

- ✅ Include links to full papers
- ✅ Add publication dates
- ✅ Credit co-authors
- ✅ Include methodology if relevant

### Contact Message Management

- ✅ Respond promptly to messages
- ✅ Mark as read when replied
- ✅ Archive old conversations
- ✅ Look for patterns in inquiries

## 🔍 Editing Content

### To Edit Any Item:

1. Click on the item in the admin list
2. Make changes in the form
3. Click **Save**
4. Or click **Save and continue editing** to keep editing

### To Delete Any Item:

1. Click on the item
2. Scroll down and click **Delete** button
3. Confirm deletion

## 📋 Bulk Actions

For Projects, Skills, etc., you can:

1. Check boxes next to items
2. Select action from dropdown (e.g., Delete)
3. Click **Go**

## 🔐 Admin User Management

### Creating Additional Admin Users:

1. Go to **Users** section (if available)
2. Click **Add User**
3. Enter username and password
4. Click **Save**
5. Give appropriate permissions

### Changing Your Password:

1. Click your username (top right)
2. Click **Change password**
3. Enter old password
4. Enter new password (twice)
5. Click **Change password**

## 🗄️ Database Operations

### Backup Your Data:

```bash
# Export data to JSON file
python manage.py dumpdata > backup.json

# Export specific app data
python manage.py dumpdata portfolio > portfolio_backup.json
```

### Restore Backup:

```bash
# Restore from JSON file
python manage.py loaddata backup.json
```

## 🔍 Searching and Filtering

### Most Admin Pages Support:

**Search:**

- Click search box
- Type keywords (searches in relevant fields)
- Press Enter

**Filtering:**

- Use filters in right sidebar
- Filter by date, category, status, etc.
- Click to apply filter

**Sorting:**

- Click column headers to sort
- Click again to reverse sort

## 📊 Tips & Tricks

### Image Upload

- Maximum file size: Usually unlimited
- Recommended formats: JPG, PNG, WebP
- Optimal size: 800x600px or larger
- Include compression for faster loading

### Date Fields

- Click calendar icon for date picker
- Format: YYYY-MM-DD
- Can type dates directly

### Text Fields

- Use markdown formatting in description fields
- Leave blank for optional fields
- Use line breaks for readability

### URL Fields

- Include full URL: https://example.com
- Test links before saving
- Update dead links regularly

## 🚨 Common Issues

### "Permission Denied" Error

- You don't have permission for this action
- Contact admin to grant permissions

### Images Not Showing

- Check file permissions
- Ensure file was uploaded properly
- Try uploading again

### Page Layouts Look Strange

- Clear browser cache (Ctrl+Shift+Del)
- Refresh page (Ctrl+F5)
- Try different browser

### Changes Not Saving

- Check for error messages
- Ensure all required fields are filled
- Try logging in again

## 🔒 Security Tips

- ✅ Change your password regularly
- ✅ Don't share login credentials
- ✅ Log out when finished
- ✅ Use strong passwords
- ✅ Monitor login activity
- ✅ Backup data regularly

## 📱 Admin on Mobile

The admin panel is mobile-responsive but works best on desktop. On mobile:

- Use landscape orientation for better view
- Tap carefully with large inputs
- Consider using desktop for complex edits

## 🆘 Getting Help

### Need Help?

1. Check Django Admin Documentation
2. Review field descriptions (hover for info)
3. Check README.md in project
4. See error messages for specific issues

### Common Questions

**Q: How many projects should I display?**
A: 3-5 featured projects, up to 15-20 total

**Q: How often should I update content?**
A: Add new projects quarterly, skills monthly

**Q: Can I schedule posts?**
A: Not in default Django admin (can be added with plugins)

**Q: How do I make the admin look different?**
A: Install django-admin-interface or similar package

## ⚙️ Advanced Admin Features

### Customizing Admin Display

To customize how items appear in the admin list, the `admin.py` is configured with:

- List display fields
- Search fields
- Filter options
- Read-only fields
- Fieldsets for organization

These are already configured for optimal usability.

### Admin Actions

Available actions in the admin:

- **Delete selected** - Delete multiple items
- **Mark as read** - For contact messages
- **Mark as featured** - For projects

---

**You're now ready to manage your portfolio!**

For more information, visit: https://docs.djangoproject.com/admin/

**Happy managing! 📊**
