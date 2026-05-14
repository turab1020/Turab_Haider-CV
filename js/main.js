// ── Bold Portfolio JS ──
// Video bento grid: lazy load + hover play

const videoState = new WeakMap();

function loadVideo(video) {
    const s = videoState.get(video);
    if (s === 'loaded') return Promise.resolve();
    if (s === 'loading') return new Promise(r => video.addEventListener('canplay', r, { once: true }));

    const src = video.dataset.src;
    if (!src) return Promise.resolve();
    videoState.set(video, 'loading');

    return new Promise((resolve) => {
        video.addEventListener('canplay', () => {
            videoState.set(video, 'loaded');
            resolve();
        }, { once: true });
        video.addEventListener('error', () => {
            videoState.set(video, 'error');
            resolve();
        }, { once: true });
        video.src = src;
        video.load();
    });
}

document.addEventListener('DOMContentLoaded', () => {

    // ── Theme toggle ──
    const themeBtn = document.getElementById('theme-toggle');
    const themeIcon = themeBtn.querySelector('i');
    if (localStorage.getItem('theme') === 'light') {
        document.body.classList.add('light-mode');
        themeIcon.classList.replace('fa-sun', 'fa-moon');
    }
    themeBtn.addEventListener('click', () => {
        document.body.classList.toggle('light-mode');
        const isLight = document.body.classList.contains('light-mode');
        themeIcon.classList.replace(isLight ? 'fa-sun' : 'fa-moon', isLight ? 'fa-moon' : 'fa-sun');
        localStorage.setItem('theme', isLight ? 'light' : 'dark');
    });

    // ── Card reveal on scroll ──
    const revealEls = document.querySelectorAll('.card, .project-card');
    const revealObs = new IntersectionObserver((entries) => {
        entries.forEach((e, i) => {
            if (e.isIntersecting) {
                setTimeout(() => e.target.classList.add('visible'), i * 80);
                revealObs.unobserve(e.target);
            }
        });
    }, { threshold: 0.06, rootMargin: '0px 0px -30px 0px' });
    revealEls.forEach(el => revealObs.observe(el));

    const isTouch = window.matchMedia('(hover:none) and (pointer:coarse)').matches;

    // ── Lazy video metadata via IntersectionObserver ──
    const vidObs = new IntersectionObserver((entries) => {
        entries.forEach(e => {
            if (e.isIntersecting) {
                const v = e.target;
                if (v.dataset.src && !v.src) {
                    v.preload = 'metadata';
                    v.src = v.dataset.src;
                }
                if (isTouch) {
                    loadVideo(v).then(() => v.play().catch(() => {}));
                } else {
                    vidObs.unobserve(v);
                }
            } else {
                const v = e.target;
                if (isTouch && !v.paused) {
                    v.pause();
                }
            }
        });
    }, { rootMargin: '300px 0px' });
    document.querySelectorAll('video[data-src]').forEach(v => vidObs.observe(v));

    // ── Project card video: hover play (desktop) / tap toggle (mobile) ──
    const projectCards = document.querySelectorAll('.project-card');

    projectCards.forEach(card => {
        const video = card.querySelector('video');
        if (!video) return;

        if (isTouch) {
            card.addEventListener('click', (e) => {
                // Don't intercept link clicks
                if (e.target.closest('a')) return;
                const wasActive = card.classList.contains('touch-active');
                // Close others
                projectCards.forEach(c => {
                    c.classList.remove('touch-active');
                });
                if (!wasActive) {
                    card.classList.add('touch-active');
                }
            });
        } else {
            card.addEventListener('mouseenter', () => {
                loadVideo(video).then(() => video.play().catch(() => {}));
            });
            card.addEventListener('mouseleave', () => {
                video.pause();
                video.currentTime = 0;
            });
        }
    });

    // ── Scroll spy ──
    const sections = document.querySelectorAll('#hero, #about, #projects, #contact');
    const navLinks = document.querySelectorAll('.nav-link');

    const updateNav = () => {
        const y = window.scrollY;
        const wh = window.innerHeight;
        const dh = document.documentElement.scrollHeight;
        let active = 'hero';

        sections.forEach(s => {
            if (y + wh * 0.35 >= s.offsetTop) {
                active = s.id;
            }
        });
        if (y < 50) active = 'hero';
        if (y + wh >= dh - 80) active = 'contact';

        navLinks.forEach(l => {
            l.classList.toggle('active', l.dataset.section === active);
        });
    };

    // ── Nav hide on scroll ──
    const navBar = document.querySelector('.nav-bar');
    let lastY = window.scrollY, navHidden = false;

    let scrollTick = false;
    window.addEventListener('scroll', () => {
        if (!scrollTick) {
            requestAnimationFrame(() => {
                updateNav();
                const curY = window.scrollY;
                const delta = curY - lastY;
                if (curY < 60) {
                    navBar.classList.remove('hidden');
                    navHidden = false;
                } else if (delta > 8 && !navHidden) {
                    navBar.classList.add('hidden');
                    navHidden = true;
                } else if (delta < -8 && navHidden) {
                    navBar.classList.remove('hidden');
                    navHidden = false;
                }
                lastY = curY;
                scrollTick = false;
            });
            scrollTick = true;
        }
    }, { passive: true });

    updateNav();
    console.log('Portfolio ready');
});