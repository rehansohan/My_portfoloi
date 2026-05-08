from django.db import models
from django.core.validators import URLValidator
from django.utils import timezone

class Project(models.Model):
    """Model for portfolio projects"""
    title = models.CharField(max_length=200)
    description = models.TextField()
    technologies = models.CharField(max_length=500, help_text="Comma-separated list of technologies")
    image = models.ImageField(upload_to='projects/', blank=True, null=True)
    github_link = models.URLField(blank=True, null=True)
    live_demo_link = models.URLField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    featured = models.BooleanField(default=False)
    
    class Meta:
        ordering = ['-created_at']
        verbose_name_plural = "Projects"
    
    def __str__(self):
        return self.title


class Research(models.Model):
    """Model for research items and publications"""
    RESEARCH_TYPE_CHOICES = [
        ('research', 'Research Topic'),
        ('publication', 'Publication'),
        ('conference', 'Conference Presentation'),
        ('fieldwork', 'Fieldwork'),
    ]
    
    title = models.CharField(max_length=300)
    research_type = models.CharField(max_length=20, choices=RESEARCH_TYPE_CHOICES, default='research')
    description = models.TextField()
    authors = models.CharField(max_length=500, blank=True, help_text="Comma-separated author names")
    journal_name = models.CharField(max_length=300, blank=True)
    publication_date = models.DateField(blank=True, null=True)
    url = models.URLField(blank=True, null=True)
    image = models.ImageField(upload_to='research/', blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    
    class Meta:
        ordering = ['-publication_date', '-created_at']
        verbose_name_plural = "Research Items"
    
    def __str__(self):
        return self.title


class Certification(models.Model):
    """Model for certifications and credentials"""
    name = models.CharField(max_length=300)
    issuer = models.CharField(max_length=200)
    issue_date = models.DateField()
    expiry_date = models.DateField(blank=True, null=True)
    credential_url = models.URLField(blank=True, null=True)
    credential_id = models.CharField(max_length=500, blank=True)
    image = models.ImageField(upload_to='certifications/', blank=True, null=True)
    
    class Meta:
        ordering = ['-issue_date']
    
    def __str__(self):
        return self.name


class ContactMessage(models.Model):
    """Model for contact form submissions"""
    name = models.CharField(max_length=200)
    email = models.EmailField()
    phone = models.CharField(max_length=20, blank=True)
    subject = models.CharField(max_length=300)
    message = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    is_read = models.BooleanField(default=False)
    
    class Meta:
        ordering = ['-created_at']
    
    def __str__(self):
        return f"{self.name} - {self.subject}"


class Skill(models.Model):
    """Model for skills with proficiency levels"""
    SKILL_CATEGORY_CHOICES = [
        ('programming', 'Programming Languages'),
        ('framework', 'Frameworks & Tools'),
        ('data', 'Data Analysis & Visualization'),
        ('engineering', 'Engineering Tools'),
        ('soft', 'Soft Skills'),
    ]
    
    name = models.CharField(max_length=100)
    category = models.CharField(max_length=20, choices=SKILL_CATEGORY_CHOICES)
    proficiency = models.IntegerField(default=70, help_text="Proficiency level 0-100")
    icon = models.CharField(max_length=100, blank=True, help_text="Font Awesome icon name")
    
    class Meta:
        ordering = ['category', '-proficiency']
    
    def __str__(self):
        return f"{self.name} ({self.get_category_display()})"


class Education(models.Model):
    """Model for education information"""
    institution = models.CharField(max_length=300)
    degree = models.CharField(max_length=200)
    field_of_study = models.CharField(max_length=300)
    start_date = models.DateField()
    end_date = models.DateField(blank=True, null=True)
    description = models.TextField(blank=True)
    cgpa = models.FloatField(blank=True, null=True)
    
    class Meta:
        ordering = ['-start_date']
        verbose_name_plural = "Education"
    
    def __str__(self):
        return f"{self.degree} from {self.institution}"


class Profile(models.Model):
    """Model for portfolio profile/about information"""
    full_name = models.CharField(max_length=200)
    tagline = models.CharField(max_length=500, help_text="Your professional tagline/title")
    bio_short = models.TextField(help_text="Short introduction for hero section")
    bio_long = models.TextField(help_text="Detailed about section")
    profile_image = models.ImageField(upload_to='profile/', blank=True, null=True)
    projects_count = models.IntegerField(default=0)
    research_count = models.IntegerField(default=0)
    animation_strings = models.TextField(
        default="Fisheries & Marine Science Enthusiast|Engineering Solutions Developer|Ocean Conservation Advocate|Data Analysis Specialist|Passionate About Sustainable Fisheries",
        help_text="Typing animation strings separated by | (pipe character)"
    )
    email = models.EmailField(blank=True)
    phone = models.CharField(max_length=20, blank=True)
    location = models.CharField(max_length=200, blank=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    class Meta:
        verbose_name_plural = "Profile"
    
    def __str__(self):
        return self.full_name or "Profile"
