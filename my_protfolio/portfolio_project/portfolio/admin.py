from django.contrib import admin
from .models import Project, Research, Certification, ContactMessage, Skill, Education, Profile


@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    list_display = ('full_name', 'updated_at')
    fieldsets = (
        ('Personal Information', {
            'fields': ('full_name', 'tagline', 'email', 'phone', 'location')
        }),
        ('Bio & Description', {
            'fields': ('bio_short', 'bio_long')
        }),
        ('Image', {
            'fields': ('profile_image',)
        }),
        ('Typing Animation Strings', {
            'fields': ('animation_strings',),
            'description': 'Enter animation strings separated by | (pipe). Example: String1|String2|String3'
        }),
        ('Statistics', {
            'fields': ('projects_count', 'research_count'),
            'description': 'Update these numbers to display on your profile'
        }),
        ('Metadata', {
            'fields': ('updated_at',),
            'classes': ('collapse',)
        }),
    )
    readonly_fields = ('updated_at',)


@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):
    list_display = ('title', 'featured', 'created_at', 'updated_at')
    list_filter = ('featured', 'created_at')
    search_fields = ('title', 'description', 'technologies')
    readonly_fields = ('created_at', 'updated_at')
    fieldsets = (
        ('Project Information', {
            'fields': ('title', 'description', 'technologies', 'featured')
        }),
        ('Media', {
            'fields': ('image',)
        }),
        ('Links', {
            'fields': ('github_link', 'live_demo_link')
        }),
        ('Timestamps', {
            'fields': ('created_at', 'updated_at'),
            'classes': ('collapse',)
        }),
    )


@admin.register(Research)
class ResearchAdmin(admin.ModelAdmin):
    list_display = ('title', 'research_type', 'publication_date', 'created_at')
    list_filter = ('research_type', 'publication_date')
    search_fields = ('title', 'description', 'authors', 'journal_name')
    readonly_fields = ('created_at',)
    fieldsets = (
        ('Research Information', {
            'fields': ('title', 'research_type', 'description')
        }),
        ('Publication Details', {
            'fields': ('authors', 'journal_name', 'publication_date', 'url')
        }),
        ('Media', {
            'fields': ('image',)
        }),
        ('Metadata', {
            'fields': ('created_at',),
            'classes': ('collapse',)
        }),
    )


@admin.register(Certification)
class CertificationAdmin(admin.ModelAdmin):
    list_display = ('name', 'issuer', 'issue_date', 'expiry_date')
    list_filter = ('issuer', 'issue_date')
    search_fields = ('name', 'issuer', 'credential_id')
    fieldsets = (
        ('Certification Information', {
            'fields': ('name', 'issuer', 'credential_id')
        }),
        ('Dates', {
            'fields': ('issue_date', 'expiry_date')
        }),
        ('Links & Media', {
            'fields': ('credential_url', 'image')
        }),
    )


@admin.register(ContactMessage)
class ContactMessageAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'subject', 'created_at', 'is_read')
    list_filter = ('is_read', 'created_at')
    search_fields = ('name', 'email', 'subject', 'message')
    readonly_fields = ('created_at', 'name', 'email', 'subject', 'message')
    actions = ['mark_as_read', 'mark_as_unread']
    
    def mark_as_read(self, request, queryset):
        queryset.update(is_read=True)
        self.message_user(request, 'Selected messages marked as read.')
    mark_as_read.short_description = 'Mark selected messages as read'
    
    def mark_as_unread(self, request, queryset):
        queryset.update(is_read=False)
        self.message_user(request, 'Selected messages marked as unread.')
    mark_as_unread.short_description = 'Mark selected messages as unread'


@admin.register(Skill)
class SkillAdmin(admin.ModelAdmin):
    list_display = ('name', 'category', 'proficiency')
    list_filter = ('category', 'proficiency')
    search_fields = ('name',)
    fieldsets = (
        ('Skill Information', {
            'fields': ('name', 'category', 'proficiency')
        }),
        ('Display', {
            'fields': ('icon',)
        }),
    )


@admin.register(Education)
class EducationAdmin(admin.ModelAdmin):
    list_display = ('degree', 'institution', 'start_date', 'end_date', 'cgpa')
    list_filter = ('institution', 'start_date')
    search_fields = ('degree', 'institution', 'field_of_study')
    fieldsets = (
        ('Education Information', {
            'fields': ('institution', 'degree', 'field_of_study', 'cgpa')
        }),
        ('Timeline', {
            'fields': ('start_date', 'end_date')
        }),
        ('Description', {
            'fields': ('description',)
        }),
    )
