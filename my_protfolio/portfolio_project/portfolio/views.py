from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from django.http import JsonResponse
from .models import Project, Research, Certification, ContactMessage, Skill, Education, Profile
from .forms import ContactForm


def home(request):
    """Home page view"""
    profile = Profile.objects.first()
    featured_projects = Project.objects.filter(featured=True)[:3]
    context = {
        'profile': profile,
        'featured_projects': featured_projects,
        'page_title': 'Home',
    }
    return render(request, 'portfolio/home.html', context)


def about(request):
    """About page view"""
    profile = Profile.objects.first()
    education = Education.objects.all()
    context = {
        'profile': profile,
        'education': education,
        'page_title': 'About Me',
    }
    return render(request, 'portfolio/about.html', context)


def skills(request):
    """Skills page view"""
    programming_skills = Skill.objects.filter(category='programming').order_by('-proficiency')
    framework_skills = Skill.objects.filter(category='framework').order_by('-proficiency')
    data_skills = Skill.objects.filter(category='data').order_by('-proficiency')
    engineering_skills = Skill.objects.filter(category='engineering').order_by('-proficiency')
    soft_skills = Skill.objects.filter(category='soft').order_by('-proficiency')
    
    context = {
        'programming_skills': programming_skills,
        'framework_skills': framework_skills,
        'data_skills': data_skills,
        'engineering_skills': engineering_skills,
        'soft_skills': soft_skills,
        'page_title': 'Skills',
    }
    return render(request, 'portfolio/skills.html', context)


def projects(request):
    """Projects page view"""
    all_projects = Project.objects.all()
    context = {
        'projects': all_projects,
        'page_title': 'Projects',
    }
    return render(request, 'portfolio/projects.html', context)


def project_detail(request, pk):
    """Project detail page"""
    project = get_object_or_404(Project, pk=pk)
    related_projects = Project.objects.exclude(pk=pk)[:3]
    context = {
        'project': project,
        'related_projects': related_projects,
        'page_title': project.title,
    }
    return render(request, 'portfolio/project_detail.html', context)


def research(request):
    """Research and publications page view"""
    research_topics = Research.objects.filter(research_type='research')
    publications = Research.objects.filter(research_type='publication')
    conferences = Research.objects.filter(research_type='conference')
    fieldwork = Research.objects.filter(research_type='fieldwork')
    
    context = {
        'research_topics': research_topics,
        'publications': publications,
        'conferences': conferences,
        'fieldwork': fieldwork,
        'page_title': 'Research & Publications',
    }
    return render(request, 'portfolio/research.html', context)


def certifications(request):
    """Certifications page view"""
    all_certifications = Certification.objects.all()
    context = {
        'certifications': all_certifications,
        'page_title': 'Certifications',
    }
    return render(request, 'portfolio/certifications.html', context)


def contact(request):
    """Contact page with form handling"""
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Your message has been sent successfully! I will get back to you soon.')
            return redirect('contact')
        else:
            messages.error(request, 'There was an error sending your message. Please try again.')
    else:
        form = ContactForm()
    
    context = {
        'form': form,
        'page_title': 'Contact',
    }
    return render(request, 'portfolio/contact.html', context)


def download_cv(request):
    """Download CV file"""
    # This will serve the CV file from static/files/CV.pdf
    from django.http import FileResponse
    import os
    
    cv_path = os.path.join('portfolio/static/files', 'CV.pdf')
    if os.path.exists(cv_path):
        return FileResponse(open(cv_path, 'rb'), content_type='application/pdf')
    else:
        messages.error(request, 'CV file not found.')
        return redirect('home')


def api_skills(request):
    """API endpoint to get skills as JSON"""
    skills = Skill.objects.values('name', 'category', 'proficiency', 'icon')
    return JsonResponse(list(skills), safe=False)


def api_projects(request):
    """API endpoint to get projects as JSON"""
    projects = Project.objects.values('id', 'title', 'description', 'technologies', 'featured')
    return JsonResponse(list(projects), safe=False)
