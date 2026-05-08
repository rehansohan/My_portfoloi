/* =================================================================================
   PORTFOLIO WEBSITE - MAIN JAVASCRIPT
   Interactive Features and Animations
================================================================================= */

document.addEventListener('DOMContentLoaded', function() {
    initializeAOS();
    setupNavbarScrolling();
    setupBackToTopButton();
    setupThemeToggle();
    setupSmoothScrolling();
    setupFormValidation();
    animateProgressBars();
});

/* ===== INITIALIZE AOS (Animate On Scroll) ===== */
function initializeAOS() {
    try {
        AOS.init({
            duration: 800,
            easing: 'ease-in-out',
            once: true,
            offset: 100
        });
    } catch (e) {
        console.log('AOS not available');
    }
}

/* ===== NAVBAR SCROLLING EFFECT ===== */
function setupNavbarScrolling() {
    const navbar = document.getElementById('navbar');
    const scrollThreshold = 50;

    window.addEventListener('scroll', function() {
        if (window.scrollY > scrollThreshold) {
            navbar.classList.add('scrolled');
        } else {
            navbar.classList.remove('scrolled');
        }
    });
}

/* ===== BACK TO TOP BUTTON ===== */
function setupBackToTopButton() {
    const backToTopBtn = document.getElementById('backToTop');
    const scrollThreshold = 300;

    window.addEventListener('scroll', function() {
        if (window.scrollY > scrollThreshold) {
            backToTopBtn.style.display = 'flex';
        } else {
            backToTopBtn.style.display = 'none';
        }
    });

    backToTopBtn.addEventListener('click', function() {
        window.scrollTo({
            top: 0,
            behavior: 'smooth'
        });
    });
}

/* ===== DARK/LIGHT MODE TOGGLE ===== */
function setupThemeToggle() {
    const themeToggle = document.getElementById('themeToggle');
    const htmlElement = document.documentElement;
    const body = document.body;

    // Check for saved theme preference or default to 'light'
    const currentTheme = localStorage.getItem('theme') || 'light';
    
    // Apply saved theme
    if (currentTheme === 'dark') {
        body.classList.add('dark-mode');
        updateThemeIcon('light');
    } else {
        body.classList.remove('dark-mode');
        updateThemeIcon('dark');
    }

    // Theme toggle click event
    themeToggle.addEventListener('click', function() {
        body.classList.toggle('dark-mode');
        
        const isDarkMode = body.classList.contains('dark-mode');
        localStorage.setItem('theme', isDarkMode ? 'dark' : 'light');
        
        updateThemeIcon(isDarkMode ? 'light' : 'dark');
    });

    function updateThemeIcon(mode) {
        const icon = themeToggle.querySelector('i');
        if (mode === 'dark') {
            icon.classList.remove('fa-sun');
            icon.classList.add('fa-moon');
        } else {
            icon.classList.remove('fa-moon');
            icon.classList.add('fa-sun');
        }
    }
}

/* ===== SMOOTH SCROLLING FOR ANCHOR LINKS ===== */
function setupSmoothScrolling() {
    const navLinks = document.querySelectorAll('a[href^="#"]');
    
    navLinks.forEach(link => {
        link.addEventListener('click', function(e) {
            e.preventDefault();
            
            const targetId = this.getAttribute('href');
            if (targetId === '#') return;
            
            const targetElement = document.querySelector(targetId);
            if (targetElement) {
                targetElement.scrollIntoView({
                    behavior: 'smooth',
                    block: 'start'
                });
            }
        });
    });
}

/* ===== FORM VALIDATION ===== */
function setupFormValidation() {
    const forms = document.querySelectorAll('form');
    
    forms.forEach(form => {
        form.addEventListener('submit', function(e) {
            if (!form.checkValidity() === false) {
                e.preventDefault();
                e.stopPropagation();
            }
            form.classList.add('was-validated');
        });
    });
}

/* ===== ANIMATE PROGRESS BARS ===== */
function animateProgressBars() {
    const progressBars = document.querySelectorAll('.progress-bar');
    
    // Intersection Observer for progress bar animation
    const observer = new IntersectionObserver((entries) => {
        entries.forEach(entry => {
            if (entry.isIntersecting) {
                const bar = entry.target;
                const percentage = bar.style.width;
                bar.style.width = '0%';
                
                setTimeout(() => {
                    bar.style.width = percentage;
                }, 100);
                
                observer.unobserve(bar);
            }
        });
    }, {
        threshold: 0.5
    });
    
    progressBars.forEach(bar => observer.observe(bar));
}

/* ===== NAVBAR ACTIVE LINK ===== */
document.addEventListener('DOMContentLoaded', function() {
    const navLinks = document.querySelectorAll('.nav-link');
    const currentLocation = location.pathname;
    
    navLinks.forEach(link => {
        const href = link.getAttribute('href');
        if (href === currentLocation || (href === '/' && currentLocation === '/')) {
            link.classList.add('active');
        } else {
            link.classList.remove('active');
        }
    });
});

/* ===== SCROLL SPY FOR NAVBAR ===== */
function setupScrollSpy() {
    const navLinks = document.querySelectorAll('.nav-link');
    
    window.addEventListener('scroll', function() {
        const scrollPosition = window.scrollY + 100;
        
        navLinks.forEach(link => {
            const section = document.querySelector(link.getAttribute('href'));
            
            if (section) {
                const sectionTop = section.offsetTop;
                const sectionBottom = sectionTop + section.offsetHeight;
                
                if (scrollPosition >= sectionTop && scrollPosition < sectionBottom) {
                    navLinks.forEach(l => l.classList.remove('active'));
                    link.classList.add('active');
                }
            }
        });
    });
}

/* ===== LAZY LOADING FOR IMAGES ===== */
function setupLazyLoading() {
    if ('IntersectionObserver' in window) {
        const images = document.querySelectorAll('img[data-src]');
        
        const imageObserver = new IntersectionObserver((entries, observer) => {
            entries.forEach(entry => {
                if (entry.isIntersecting) {
                    const img = entry.target;
                    img.src = img.dataset.src;
                    img.classList.add('loaded');
                    observer.unobserve(img);
                }
            });
        });
        
        images.forEach(img => imageObserver.observe(img));
    }
}

/* ===== COUNTER ANIMATION ===== */
function animateCounters() {
    const counters = document.querySelectorAll('.counter');
    
    const counterObserver = new IntersectionObserver((entries) => {
        entries.forEach(entry => {
            if (entry.isIntersecting) {
                const counter = entry.target;
                const target = parseInt(counter.textContent);
                const duration = 2000;
                const increment = target / (duration / 16);
                let current = 0;
                
                const timer = setInterval(() => {
                    current += increment;
                    if (current >= target) {
                        counter.textContent = target;
                        clearInterval(timer);
                    } else {
                        counter.textContent = Math.floor(current);
                    }
                }, 16);
                
                counterObserver.unobserve(counter);
            }
        });
    }, {
        threshold: 0.5
    });
    
    counters.forEach(counter => counterObserver.observe(counter));
}

/* ===== MOBILE MENU COLLAPSE ===== */
function setupMobileMenuCollapse() {
    const navLinks = document.querySelectorAll('.nav-link');
    const navbarCollapse = document.querySelector('.navbar-collapse');
    const navbarToggler = document.querySelector('.navbar-toggler');
    
    navLinks.forEach(link => {
        link.addEventListener('click', () => {
            if (navbarCollapse.classList.contains('show')) {
                navbarToggler.click();
            }
        });
    });
}

// Initialize mobile menu collapse when DOM is ready
document.addEventListener('DOMContentLoaded', setupMobileMenuCollapse);

/* ===== FORM SUBMISSION FEEDBACK ===== */
function setupFormFeedback() {
    const forms = document.querySelectorAll('form');
    
    forms.forEach(form => {
        form.addEventListener('submit', function(e) {
            const submitBtn = form.querySelector('button[type="submit"]');
            if (submitBtn) {
                const originalText = submitBtn.innerHTML;
                submitBtn.innerHTML = '<i class="fas fa-spinner fa-spin"></i> Sending...';
                submitBtn.disabled = true;
                
                // Re-enable after 3 seconds (in case of error)
                setTimeout(() => {
                    submitBtn.innerHTML = originalText;
                    submitBtn.disabled = false;
                }, 3000);
            }
        });
    });
}

document.addEventListener('DOMContentLoaded', setupFormFeedback);

/* ===== KEYBOARD SHORTCUTS ===== */
function setupKeyboardShortcuts() {
    document.addEventListener('keydown', function(event) {
        // Ctrl/Cmd + K to focus search (if search exists)
        if ((event.ctrlKey || event.metaKey) && event.key === 'k') {
            event.preventDefault();
            const searchInput = document.querySelector('[role="search"] input');
            if (searchInput) searchInput.focus();
        }
        
        // Home key to scroll to top
        if (event.key === 'Home') {
            window.scrollTo({ top: 0, behavior: 'smooth' });
        }
        
        // End key to scroll to bottom
        if (event.key === 'End') {
            window.scrollTo({ top: document.body.scrollHeight, behavior: 'smooth' });
        }
    });
}

document.addEventListener('DOMContentLoaded', setupKeyboardShortcuts);

/* ===== EXTERNAL LINKS ===== */
function setupExternalLinks() {
    const links = document.querySelectorAll('a[href^="http"]');
    
    links.forEach(link => {
        if (!link.hostname === window.location.hostname) {
            link.target = '_blank';
            link.rel = 'noopener noreferrer';
        }
    });
}

document.addEventListener('DOMContentLoaded', setupExternalLinks);

/* ===== ERROR HANDLING ===== */
window.addEventListener('error', function(event) {
    console.error('Error:', event.error);
    // You can send error reports to a logging service here
});

/* ===== UNHANDLED PROMISE REJECTION ===== */
window.addEventListener('unhandledrejection', function(event) {
    console.error('Unhandled promise rejection:', event.reason);
});

/* ===== PERFORMANCE MONITORING ===== */
function logPerformanceMetrics() {
    if (window.performance && window.performance.timing) {
        const perfData = window.performance.timing;
        const pageLoadTime = perfData.loadEventEnd - perfData.navigationStart;
        console.log('Page load time:', pageLoadTime + 'ms');
    }
}

window.addEventListener('load', logPerformanceMetrics);
