// Track video loading states
const videoLoadState = new Map();

// Preload video and track state
function preloadVideo(video) {
    if (!video || videoLoadState.get(video) === 'loaded') return Promise.resolve();
    
    const src = video.dataset.src || video.src;
    if (!src) return Promise.resolve();
    
    videoLoadState.set(video, 'loading');
    
    return new Promise((resolve) => {
        if (video.src && video.readyState >= 3) {
            videoLoadState.set(video, 'loaded');
            resolve();
            return;
        }
        
        if (video.dataset.src && !video.src) {
            video.src = video.dataset.src;
        }
        
        const onCanPlay = () => {
            videoLoadState.set(video, 'loaded');
            video.removeEventListener('canplaythrough', onCanPlay);
            video.removeEventListener('error', onError);
            resolve();
        };
        
        const onError = () => {
            videoLoadState.set(video, 'error');
            video.removeEventListener('canplaythrough', onCanPlay);
            video.removeEventListener('error', onError);
            resolve();
        };
        
        video.addEventListener('canplaythrough', onCanPlay, { once: true });
        video.addEventListener('error', onError, { once: true });
        video.load();
    });
}

// Toggle accordion open/close and handle video playback
function toggleAccordion(element) {
    const isActive = element.classList.contains('active');
    
    if (isActive) {
        element.classList.remove('active');
        const video = element.querySelector('video');
        if (video) {
            video.pause();
            video.currentTime = 0;
        }
    } else {
        element.classList.add('active');
        const video = element.querySelector('video');
        if (video) {
            if (video.dataset.src && !video.src) {
                video.src = video.dataset.src;
            }
            
            if (videoLoadState.get(video) === 'loaded') {
                video.play().catch(() => {});
            } else {
                preloadVideo(video).then(() => {
                    if (element.classList.contains('active')) {
                        video.play().catch(() => {});
                    }
                });
            }
        }
    }
}

document.addEventListener('DOMContentLoaded', () => {
    
    // Check network speed
    const getConnectionSpeed = () => {
        if ('connection' in navigator) {
            return navigator.connection.effectiveType || '4g';
        }
        return '4g';
    };
    
    const isSlowConnection = () => {
        const speed = getConnectionSpeed();
        return speed === '2g' || speed === 'slow-2g';
    };
    
    // Theme toggle
    const themeToggleBtn = document.getElementById('theme-toggle');
    const themeIcon = themeToggleBtn.querySelector('i');
    const body = document.body;

    const currentTheme = localStorage.getItem('theme');
    if (currentTheme === 'light') {
        body.classList.add('light-mode');
        themeIcon.classList.replace('fa-sun', 'fa-moon');
    }

    themeToggleBtn.addEventListener('click', () => {
        body.classList.toggle('light-mode');
        if (body.classList.contains('light-mode')) {
            themeIcon.classList.replace('fa-sun', 'fa-moon');
            localStorage.setItem('theme', 'light');
        } else {
            themeIcon.classList.replace('fa-moon', 'fa-sun');
            localStorage.setItem('theme', 'dark');
        }
    });

    // Card reveal animations
    const cards = document.querySelectorAll('.bento-card');
    const observerOptions = { threshold: 0.1 };

    const observer = new IntersectionObserver((entries) => {
        entries.forEach((entry, index) => {
            if (entry.isIntersecting) {
                setTimeout(() => {
                    entry.target.style.opacity = '1';
                    entry.target.style.transform = 'translateY(0)';
                }, index * 120);
                observer.unobserve(entry.target);
            }
        });
    }, observerOptions);

    cards.forEach(card => {
        card.style.opacity = '0';
        card.style.transform = 'translateY(30px)';
        observer.observe(card);
    });

    // Video preloading
    const lazyVideos = document.querySelectorAll('video.lazy-video, video[data-src]');
    
    const markVideoLoaded = (video) => {
        const container = video.closest('.project-preview');
        if (container) {
            container.classList.add('loaded');
        }
    };
    
    const preloadAllVideos = () => {
        const videos = document.querySelectorAll('video[data-src], video.lazy-video');
        
        // Sequential loading for slow connections
        const loadVideoSequentially = (index) => {
            if (index >= videos.length) return;
            
            const video = videos[index];
            if (video.dataset.src && !video.src) {
                video.src = video.dataset.src;
            }
            video.preload = 'auto';
            
            video.addEventListener('canplaythrough', () => {
                markVideoLoaded(video);
                if (isSlowConnection()) {
                    loadVideoSequentially(index + 1);
                }
            }, { once: true });
            
            video.addEventListener('loadeddata', () => markVideoLoaded(video), { once: true });
            video.load();
        };
        
        if (isSlowConnection()) {
            loadVideoSequentially(0);
        } else {
            videos.forEach(video => {
                if (video.dataset.src && !video.src) {
                    video.src = video.dataset.src;
                }
                video.preload = 'auto';
                
                video.addEventListener('canplaythrough', () => markVideoLoaded(video), { once: true });
                video.addEventListener('loadeddata', () => markVideoLoaded(video), { once: true });
                
                video.load();
            });
        }
    };
    
    // Start preloading
    if (isSlowConnection()) {
        if ('requestIdleCallback' in window) {
            requestIdleCallback(preloadAllVideos, { timeout: 3000 });
        } else {
            setTimeout(preloadAllVideos, 500);
        }
    } else {
        setTimeout(preloadAllVideos, 50);
    }
    
    // Video hover play/pause
    const timelineItems = document.querySelectorAll('.timeline-item');
    
    timelineItems.forEach(item => {
        const video = item.querySelector('video');
        if (video) {
            video.pause();
            
            item.addEventListener('mouseenter', () => {
                if (video.dataset.src && !video.src) {
                    video.src = video.dataset.src;
                }
                video.play().catch(() => {});
            });
            
            item.addEventListener('mouseleave', () => {
                if (!item.classList.contains('active')) {
                    video.pause();
                    video.currentTime = 0;
                }
            });
        }
    });

    // Scroll spy - highlight active nav link
    const sections = document.querySelectorAll('section[id], header[id], footer[id]');
    const navLinks = document.querySelectorAll('.pill-nav-link');
    
    const navSectionMap = {
        'profile': 'Home',
        'about': 'About', 
        'projects': 'Projects',
        'contact': 'Contact'
    };

    const updateActiveNav = () => {
        const scrollPosition = window.scrollY;
        const windowHeight = window.innerHeight;
        const documentHeight = document.documentElement.scrollHeight;
        const headerOffset = windowHeight * 0.3;
        
        let activeSection = 'profile';
        
        sections.forEach(section => {
            const sectionTop = section.offsetTop;
            const sectionHeight = section.offsetHeight;
            const sectionBottom = sectionTop + sectionHeight;
            
            if (scrollPosition + headerOffset >= sectionTop) {
                const sectionId = section.getAttribute('id');
                if (navSectionMap[sectionId]) {
                    activeSection = sectionId;
                }
            }
        });

        if (scrollPosition < 50) {
            activeSection = 'profile';
        }
        
        if (scrollPosition + windowHeight >= documentHeight - 100) {
            activeSection = 'contact';
        }

        navLinks.forEach(link => {
            link.classList.remove('active');
            const href = link.getAttribute('href');
            if (href === `#${activeSection}`) {
                link.classList.add('active');
            }
        });
    };

    let ticking = false;
    window.addEventListener('scroll', () => {
        if (!ticking) {
            requestAnimationFrame(() => {
                updateActiveNav();
                ticking = false;
            });
            ticking = true;
        }
    });
    
    updateActiveNav();

    // Hide nav on scroll down, show on scroll up
    const navContainer = document.querySelector('.nav-container');
    let lastScrollY = window.scrollY;
    let isNavHidden = false;
    
    const handleNavVisibility = () => {
        const currentScrollY = window.scrollY;
        const scrollDelta = currentScrollY - lastScrollY;
        
        if (currentScrollY < 60) {
            navContainer.classList.remove('nav-hidden');
            isNavHidden = false;
            lastScrollY = currentScrollY;
            return;
        }
        
        if (scrollDelta > 8 && !isNavHidden) {
            navContainer.classList.add('nav-hidden');
            isNavHidden = true;
        }
        
        if (scrollDelta < -8 && isNavHidden) {
            navContainer.classList.remove('nav-hidden');
            isNavHidden = false;
        }
        
        lastScrollY = currentScrollY;
    };
    
    window.addEventListener('scroll', handleNavVisibility, { passive: true });

    // Debug: log video load status
    setTimeout(() => {
        const videos = document.querySelectorAll('video');
        let loaded = 0;
        videos.forEach(v => { if (v.readyState >= 3) loaded++; });
        console.log(`Videos: ${loaded}/${videos.length}`);
    }, 3000);

    console.log('Ready');
});