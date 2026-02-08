# Personal CV Portfolio Website

A modern, responsive CV/Portfolio website built with HTML, CSS, and JavaScript. Features a clean glassmorphism design, animated mesh gradients, and a focus on clarity and performance.

## Student Information

- **Name:** Turab Haider
- **Roll Number:** 23L-0995
- **Course:** Web Programming
- **Institution:** FAST NUCES, Lahore

## Links

- **GitHub:** [github.com/turab1020/CV-Portfolio-Resume](https://github.com/turab1020/CV-Portfolio-Resume)
- **Live Demo:** [Turab Haider | CS Portfolio](https://turab-haider-cv.vercel.app)

## Features

### Main Sections
- Header with name, title, and profile photo
- About Me: concise professional summary
- Education: academic background
- Skills: key strengths and tech stack
- Experience/Projects: work history and project showcase with video previews
- Contact Information: phone, email, and social links
- Footer: copyright and resume download

### Additional Highlights
- Dark/Light mode toggle with persistent preference
- Downloadable PDF resume
- Smooth card and gradient animations
- Contact form (Formspree integration)
- Glassmorphism UI with backdrop blur
- Animated mesh gradient background
- Responsive design for all devices
- Bento grid layout with Flexbox
- Smooth scroll navigation with active state
- Project video previews (hover-to-play)
- Social links (GitHub, LinkedIn, Email)

### Performance and Optimization
- Video preloading with smart lazy loading
- Asset preload hints in HTML head
- Network-aware loading adapts to connection speed
- Service worker for offline caching and instant repeat visits
- Loading shimmer for video feedback
- GPU-accelerated animations

## Technologies Used

- HTML5 (semantic markup)
- CSS3 (Flexbox, variables, animations, media queries)
- JavaScript (DOM, localStorage, IntersectionObserver, Service Worker)
- Font Awesome (icons)
- Google Fonts (Inter)
- Formspree (contact form backend)

## File Structure

```
cv-portfolio/
├── index.html          # Main HTML file
├── css/
│   └── style.css       # All styles including responsive
├── js/
│   ├── main.js         # JavaScript functionality
│   └── sw.js           # Service worker for caching
├── images/
│   ├── profile.jpg     # Profile photo
│   └── *.mp4           # Project demo videos
└── README.md           # Project documentation
```

## Deployment

This project can be deployed on any static hosting platform, including:
- Vercel
- Netlify
- GitHub Pages

## Local Development

1. Clone the repository:
   ```bash
   git clone https://github.com/turab1020/CV-Portfolio-Resume.git
   ```

2. Open `index.html` in your browser or use a local server:
   ```bash
   # Using Python
   python -m http.server 5500
   
   # Using Node.js
   npx serve
   ```

## Responsive Breakpoints

- Desktop: 1024px and above
- Large Tablet: 900px - 1024px
- Tablet: 768px - 900px
- Mobile: 480px - 768px
- Small Mobile: 320px - 480px
- Extra Small: below 320px
- Landscape Mode: Optimized for mobile landscape orientation

## License

© 2026 Turab Haider. All Rights Reserved.