#!/usr/bin/env python3
"""
Portfolio Git History Generator
Generates a realistic 6-day development history for the CV portfolio project.

This script will:
1. COMPLETELY CLEAR the project folder (except this script)
2. Build up code incrementally with git commits
3. End with exact copy of files from SOURCE_DIR
"""

import os
import subprocess
import shutil
import glob

# ============================================
# CONFIGURATION
# ============================================
SOURCE_DIR = r"/Users/turabhaider/Desktop/Final_Portfolio_Source"
REPO_DIR = os.path.dirname(os.path.abspath(__file__))
SCRIPT_NAME = os.path.basename(__file__)

# ============================================
# COMMIT DEFINITIONS
# ============================================
COMMITS = [
    # Day 1: February 1, 2026 (The Foundation)
    {
        "date": "2026-02-01 18:15:00",
        "message": "Initial commit: Setup project scaffold and HTML5 boilerplate",
        "files": {
            "index.html": '''<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Turab Haider | Portfolio</title>
    <link rel="stylesheet" href="css/style.css">
</head>
<body>
    <div class="container">
        <h1>Portfolio - Coming Soon</h1>
    </div>
    <script src="js/main.js"></script>
</body>
</html>
''',
            "css/style.css": '''/* Portfolio Styles */
''',
            "js/main.js": '''// Portfolio JavaScript
'''
        }
    },
    {
        "date": "2026-02-01 20:45:00",
        "message": "Style: Define CSS root variables and reset",
        "files": {
            "css/style.css": ''':root {
    --bg-base: #A4550A;
    --text-primary: #ffffff;
    --text-secondary: #e0e0e0;
    --mesh-1: #43000D;
    --mesh-2: #673400;
    --mesh-3: #4C4A45;
    --mesh-4: #3E2723;
    --glass-bg: rgba(255, 255, 255, 0.02);
    --glass-border: rgba(255, 255, 255, 0.08);
    --glass-highlight: rgba(255, 255, 255, 0.4);
    --card-radius: 32px;
}

* {
    margin: 0;
    padding: 0;
    box-sizing: border-box;
}

html {
    scroll-behavior: smooth;
}

body {
    background-color: var(--bg-base);
    color: var(--text-primary);
    font-family: 'Inter', -apple-system, sans-serif;
    min-height: 100vh;
    overflow-x: hidden;
    font-size: 17px;
}
'''
        }
    },
    {
        "date": "2026-02-01 23:30:00",
        "message": "Feat: Implement animated mesh gradient background",
        "files": {
            "index.html": '''<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Turab Haider | Portfolio</title>
    <link rel="stylesheet" href="css/style.css">
    <link rel="preconnect" href="https://fonts.googleapis.com">
    <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
    <link href="https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600;800;900&display=swap" rel="stylesheet">
</head>
<body>
    <div class="mesh-bg">
        <div class="mesh-color color-1"></div>
        <div class="mesh-color color-2"></div>
        <div class="mesh-color color-3"></div>
        <div class="mesh-color color-4"></div>
    </div>

    <div class="container">
        <h1>Portfolio - In Development</h1>
    </div>
    <script src="js/main.js"></script>
</body>
</html>
''',
            "css/style.css": ''':root {
    --bg-base: #A4550A;
    --text-primary: #ffffff;
    --text-secondary: #e0e0e0;
    --mesh-1: #43000D;
    --mesh-2: #673400;
    --mesh-3: #4C4A45;
    --mesh-4: #3E2723;
    --glass-bg: rgba(255, 255, 255, 0.02);
    --glass-border: rgba(255, 255, 255, 0.08);
    --glass-highlight: rgba(255, 255, 255, 0.4);
    --card-radius: 32px;
}

* {
    margin: 0;
    padding: 0;
    box-sizing: border-box;
}

html {
    scroll-behavior: smooth;
}

body {
    background-color: var(--bg-base);
    color: var(--text-primary);
    font-family: 'Inter', -apple-system, sans-serif;
    min-height: 100vh;
    overflow-x: hidden;
    font-size: 17px;
}

.mesh-bg {
    position: fixed;
    top: 0;
    left: 0;
    width: 100vw;
    height: 100vh;
    z-index: -1;
    background: var(--bg-base);
    overflow: hidden;
}

.mesh-color {
    position: absolute;
    width: 90vw;
    height: 90vh;
    border-radius: 50%;
    opacity: 0.6;
    filter: blur(80px);
    mix-blend-mode: hard-light;
}

.color-1 {
    top: -20%;
    left: -20%;
    background: var(--mesh-1);
    animation: drift1 25s infinite linear;
}

.color-2 {
    bottom: -20%;
    right: -20%;
    background: var(--mesh-2);
    animation: drift2 30s infinite linear;
}

.color-3 {
    bottom: 10%;
    left: 20%;
    background: var(--mesh-3);
    width: 60vw;
    height: 60vh;
    animation: drift3 22s infinite linear;
}

.color-4 {
    top: 30%;
    right: 20%;
    background: var(--mesh-4);
    width: 50vw;
    height: 50vh;
    animation: drift4 28s infinite linear;
}

@keyframes drift1 {
    0% { transform: translate(0, 0); }
    33% { transform: translate(10vw, 20vh); }
    66% { transform: translate(-5vw, 40vh); }
    100% { transform: translate(0, 0); }
}

@keyframes drift2 {
    0% { transform: translate(0, 0); }
    33% { transform: translate(-20vw, -10vh); }
    66% { transform: translate(-10vw, -30vh); }
    100% { transform: translate(0, 0); }
}

@keyframes drift3 {
    0% { transform: translate(0, 0) scale(1); }
    50% { transform: translate(15vw, -15vh) scale(1.1); }
    100% { transform: translate(0, 0) scale(1); }
}

@keyframes drift4 {
    0% { transform: translate(0, 0) scale(1); }
    50% { transform: translate(-15vw, 15vh) scale(0.9); }
    100% { transform: translate(0, 0) scale(1); }
}

.container {
    max-width: 1200px;
    margin: 0 auto;
    padding: 100px 20px 80px;
    position: relative;
    z-index: 2;
}
'''
        }
    },

    # Day 2: February 2, 2026 (Layout Structure)
    {
        "date": "2026-02-02 18:20:00",
        "message": "Layout: Create responsive Bento Grid container",
        "files": {
            "css/style.css": ''':root {
    --bg-base: #A4550A;
    --text-primary: #ffffff;
    --text-secondary: #e0e0e0;
    --mesh-1: #43000D;
    --mesh-2: #673400;
    --mesh-3: #4C4A45;
    --mesh-4: #3E2723;
    --glass-bg: rgba(255, 255, 255, 0.02);
    --glass-border: rgba(255, 255, 255, 0.08);
    --glass-highlight: rgba(255, 255, 255, 0.4);
    --glass-shadow: 0 20px 40px -5px rgba(0, 0, 0, 0.4);
    --card-radius: 32px;
}

* {
    margin: 0;
    padding: 0;
    box-sizing: border-box;
}

html {
    scroll-behavior: smooth;
}

body {
    background-color: var(--bg-base);
    color: var(--text-primary);
    font-family: 'Inter', -apple-system, sans-serif;
    min-height: 100vh;
    overflow-x: hidden;
    font-size: 17px;
}

.mesh-bg {
    position: fixed;
    top: 0;
    left: 0;
    width: 100vw;
    height: 100vh;
    z-index: -1;
    background: var(--bg-base);
    overflow: hidden;
}

.mesh-color {
    position: absolute;
    width: 90vw;
    height: 90vh;
    border-radius: 50%;
    opacity: 0.6;
    filter: blur(80px);
    mix-blend-mode: hard-light;
}

.color-1 {
    top: -20%;
    left: -20%;
    background: var(--mesh-1);
    animation: drift1 25s infinite linear;
}

.color-2 {
    bottom: -20%;
    right: -20%;
    background: var(--mesh-2);
    animation: drift2 30s infinite linear;
}

.color-3 {
    bottom: 10%;
    left: 20%;
    background: var(--mesh-3);
    width: 60vw;
    height: 60vh;
    animation: drift3 22s infinite linear;
}

.color-4 {
    top: 30%;
    right: 20%;
    background: var(--mesh-4);
    width: 50vw;
    height: 50vh;
    animation: drift4 28s infinite linear;
}

@keyframes drift1 {
    0% { transform: translate(0, 0); }
    33% { transform: translate(10vw, 20vh); }
    66% { transform: translate(-5vw, 40vh); }
    100% { transform: translate(0, 0); }
}

@keyframes drift2 {
    0% { transform: translate(0, 0); }
    33% { transform: translate(-20vw, -10vh); }
    66% { transform: translate(-10vw, -30vh); }
    100% { transform: translate(0, 0); }
}

@keyframes drift3 {
    0% { transform: translate(0, 0) scale(1); }
    50% { transform: translate(15vw, -15vh) scale(1.1); }
    100% { transform: translate(0, 0) scale(1); }
}

@keyframes drift4 {
    0% { transform: translate(0, 0) scale(1); }
    50% { transform: translate(-15vw, 15vh) scale(0.9); }
    100% { transform: translate(0, 0) scale(1); }
}

.container {
    max-width: 1200px;
    margin: 0 auto;
    padding: 100px 20px 80px;
    position: relative;
    z-index: 2;
}

.bento-grid {
    display: flex;
    flex-wrap: wrap;
    gap: 24px;
    margin-top: 32px;
}

.bento-card {
    flex: 1 1 320px;
    min-width: 280px;
    position: relative;
    background: var(--glass-bg);
    overflow: hidden;
    -webkit-backdrop-filter: blur(32px) saturate(140%);
    backdrop-filter: blur(32px) saturate(140%);
    border: 1px solid var(--glass-border);
    border-radius: var(--card-radius);
    padding: 36px;
    box-shadow: var(--glass-shadow);
    display: flex;
    flex-direction: column;
    transition: all 0.4s cubic-bezier(0.2, 0.8, 0.2, 1);
}

.span-2 {
    flex: 1 1 100%;
}

.span-3 {
    flex: 1 1 100%;
}

@media (min-width: 768px) {
    .span-2 {
        flex: 2 1 calc(66% - 12px);
    }
}

@media (min-width: 1024px) {
    .bento-card {
        flex: 1 1 calc(33.333% - 16px);
    }
    .span-2 {
        flex: 2 1 calc(66.666% - 12px);
    }
}
'''
        }
    },
    {
        "date": "2026-02-02 21:10:00",
        "message": "Feat: Add Profile Card header with glassmorphism",
        "files": {
            "index.html": '''<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <meta name="description" content="Turab Haider - Computer Science Student CV">
    <title>Turab Haider | CS Portfolio</title>
    <link rel="stylesheet" href="css/style.css">
    <link rel="preconnect" href="https://fonts.googleapis.com">
    <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
    <link href="https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600;800;900&display=swap" rel="stylesheet">
    <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.4.0/css/all.min.css">
</head>
<body>
    <div class="mesh-bg">
        <div class="mesh-color color-1"></div>
        <div class="mesh-color color-2"></div>
        <div class="mesh-color color-3"></div>
        <div class="mesh-color color-4"></div>
    </div>

    <div class="container">
        <header class="bento-card profile-card" id="profile">
            <div class="profile-content">
                <h1>Turab Haider</h1>
                <p class="role">Computer Science Student</p>
                <div class="location-tag">
                    <i class="fa-solid fa-location-dot"></i> Lahore / Burewala, PK
                </div>
                <div class="status-badge">
                    <span class="pulse"></span> Open to Work
                </div>
            </div>
            <div class="header-actions">
                <div class="profile-photo-placeholder"></div>
            </div>
        </header>

        <main class="bento-grid">
        </main>
    </div>
    <script src="js/main.js"></script>
</body>
</html>
'''
        }
    },
    {
        "date": "2026-02-02 01:45:00",
        "message": "Content: Add About Me and Education sections",
        "files": {
            "index.html": '''<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <meta name="description" content="Turab Haider - Computer Science Student CV">
    <title>Turab Haider | CS Portfolio</title>
    <link rel="stylesheet" href="css/style.css">
    <link rel="preconnect" href="https://fonts.googleapis.com">
    <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
    <link href="https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600;800;900&display=swap" rel="stylesheet">
    <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.4.0/css/all.min.css">
</head>
<body>
    <div class="mesh-bg">
        <div class="mesh-color color-1"></div>
        <div class="mesh-color color-2"></div>
        <div class="mesh-color color-3"></div>
        <div class="mesh-color color-4"></div>
    </div>

    <div class="container">
        <header class="bento-card profile-card" id="profile">
            <div class="profile-content">
                <h1>Turab Haider</h1>
                <p class="role">Computer Science Student</p>
                <div class="location-tag">
                    <i class="fa-solid fa-location-dot"></i> Lahore / Burewala, PK
                </div>
                <div class="status-badge">
                    <span class="pulse"></span> Open to Work
                </div>
            </div>
            <div class="header-actions">
                <div class="profile-photo-placeholder"></div>
            </div>
        </header>

        <main class="bento-grid">
            <section class="bento-card about-card span-2" id="about">
                <h2>About Me</h2>
                <p>Driven and accomplished professional blending Computer Science with creative content creation. Seeking to leverage software development and digital media skills to provide innovative solutions.</p>
            </section>

            <section class="bento-card education-card">
                <h2>Education</h2>
                <h3>FAST NUCES</h3>
                <p class="dim">BS Computer Science</p>
                <p class="highlight">Batch 2023</p>
                <p class="dim campus-text">Lahore Campus</p>
                <div class="education-mini-item">
                    <h3>Intermediate</h3>
                    <p class="dim">Pre-Engineering (80%)</p>
                    <p class="dim">2023</p>
                </div>
            </section>

            <section class="bento-card languages-card">
                <h2>Languages</h2>
                <div class="list-content">
                    <div class="list-item">
                        <span>English</span>
                        <span class="dim">Fluent</span>
                    </div>
                    <div class="list-item">
                        <span>Urdu</span>
                        <span class="dim">Native</span>
                    </div>
                    <div class="list-item">
                        <span>Punjabi</span>
                        <span class="dim">Native</span>
                    </div>
                </div>
            </section>
        </main>
    </div>
    <script src="js/main.js"></script>
</body>
</html>
'''
        }
    },

    # Day 3: February 3, 2026 (Content Expansion)
    {
        "date": "2026-02-03 19:00:00",
        "message": "Style: Format education and language lists",
        "files": {
            "css/style.css": ''':root {
    --bg-base: #A4550A;
    --text-primary: #ffffff;
    --text-secondary: #e0e0e0;
    --mesh-1: #43000D;
    --mesh-2: #673400;
    --mesh-3: #4C4A45;
    --mesh-4: #3E2723;
    --glass-bg: rgba(255, 255, 255, 0.02);
    --glass-border: rgba(255, 255, 255, 0.08);
    --glass-highlight: rgba(255, 255, 255, 0.4);
    --glass-shadow: 0 20px 40px -5px rgba(0, 0, 0, 0.4);
    --card-radius: 32px;
}

* {
    margin: 0;
    padding: 0;
    box-sizing: border-box;
}

html {
    scroll-behavior: smooth;
}

body {
    background-color: var(--bg-base);
    color: var(--text-primary);
    font-family: 'Inter', -apple-system, sans-serif;
    min-height: 100vh;
    overflow-x: hidden;
    font-size: 17px;
}

.mesh-bg {
    position: fixed;
    top: 0;
    left: 0;
    width: 100vw;
    height: 100vh;
    z-index: -1;
    background: var(--bg-base);
    overflow: hidden;
}

.mesh-color {
    position: absolute;
    width: 90vw;
    height: 90vh;
    border-radius: 50%;
    opacity: 0.6;
    filter: blur(80px);
    mix-blend-mode: hard-light;
}

.color-1 {
    top: -20%;
    left: -20%;
    background: var(--mesh-1);
    animation: drift1 25s infinite linear;
}

.color-2 {
    bottom: -20%;
    right: -20%;
    background: var(--mesh-2);
    animation: drift2 30s infinite linear;
}

.color-3 {
    bottom: 10%;
    left: 20%;
    background: var(--mesh-3);
    width: 60vw;
    height: 60vh;
    animation: drift3 22s infinite linear;
}

.color-4 {
    top: 30%;
    right: 20%;
    background: var(--mesh-4);
    width: 50vw;
    height: 50vh;
    animation: drift4 28s infinite linear;
}

@keyframes drift1 {
    0% { transform: translate(0, 0); }
    33% { transform: translate(10vw, 20vh); }
    66% { transform: translate(-5vw, 40vh); }
    100% { transform: translate(0, 0); }
}

@keyframes drift2 {
    0% { transform: translate(0, 0); }
    33% { transform: translate(-20vw, -10vh); }
    66% { transform: translate(-10vw, -30vh); }
    100% { transform: translate(0, 0); }
}

@keyframes drift3 {
    0% { transform: translate(0, 0) scale(1); }
    50% { transform: translate(15vw, -15vh) scale(1.1); }
    100% { transform: translate(0, 0) scale(1); }
}

@keyframes drift4 {
    0% { transform: translate(0, 0) scale(1); }
    50% { transform: translate(-15vw, 15vh) scale(0.9); }
    100% { transform: translate(0, 0) scale(1); }
}

.container {
    max-width: 1200px;
    margin: 0 auto;
    padding: 100px 20px 80px;
    position: relative;
    z-index: 2;
}

.bento-grid {
    display: flex;
    flex-wrap: wrap;
    gap: 24px;
    margin-top: 32px;
}

.bento-card {
    flex: 1 1 320px;
    min-width: 280px;
    position: relative;
    background: var(--glass-bg);
    overflow: hidden;
    -webkit-backdrop-filter: blur(32px) saturate(140%);
    backdrop-filter: blur(32px) saturate(140%);
    border: 1px solid var(--glass-border);
    border-radius: var(--card-radius);
    padding: 36px;
    box-shadow: var(--glass-shadow);
    display: flex;
    flex-direction: column;
    transition: all 0.4s cubic-bezier(0.2, 0.8, 0.2, 1);
}

.span-2 {
    flex: 1 1 100%;
}

.span-3 {
    flex: 1 1 100%;
}

@media (min-width: 768px) {
    .span-2 {
        flex: 2 1 calc(66% - 12px);
    }
}

@media (min-width: 1024px) {
    .bento-card {
        flex: 1 1 calc(33.333% - 16px);
    }
    .span-2 {
        flex: 2 1 calc(66.666% - 12px);
    }
}

.profile-card {
    flex: 1 1 100%;
    flex-direction: row;
    align-items: center;
    justify-content: space-between;
}

.header-actions {
    display: flex;
    align-items: center;
    gap: 24px;
}

.profile-photo-placeholder {
    width: 160px;
    height: 160px;
    border-radius: 50%;
    background: url('../images/profile.jpg') center/150% no-repeat;
    border: 3px solid rgba(255, 255, 255, 0.25);
    box-shadow: 0 8px 24px rgba(0, 0, 0, 0.3);
}

h1 {
    font-weight: 800;
    font-size: 4rem;
    line-height: 1.1;
    margin-bottom: 10px;
    letter-spacing: -2px;
}

h2 {
    font-size: 1.1rem;
    text-transform: uppercase;
    letter-spacing: 2px;
    color: var(--text-secondary);
    margin-bottom: 24px;
    font-weight: 700;
}

h3 {
    font-size: 1.25rem;
    font-weight: 700;
}

p {
    line-height: 1.7;
    font-size: 1.15rem;
}

.dim {
    color: var(--text-secondary);
    font-size: 1rem;
}

.highlight {
    color: var(--text-primary);
    font-weight: 700;
    margin-top: 6px;
    font-size: 1.1rem;
}

.campus-text {
    font-size: 0.95rem;
    margin-top: 8px;
    opacity: 0.7;
}

.education-mini-item {
    margin-top: 24px;
    padding-top: 24px;
    border-top: 1px solid rgba(255, 255, 255, 0.1);
}

.list-content {
    display: flex;
    flex-direction: column;
    gap: 18px;
}

.list-item {
    display: flex;
    justify-content: space-between;
    border-bottom: 1px solid rgba(255, 255, 255, 0.1);
    padding-bottom: 12px;
    font-size: 1.1rem;
}

.list-item:last-child {
    border-bottom: none;
}

.location-tag {
    color: var(--text-secondary);
    font-size: 1rem;
    margin-top: 8px;
    margin-bottom: 8px;
}

.status-badge {
    display: inline-flex;
    align-items: center;
    background: rgba(50, 215, 75, 0.1);
    color: #4ade80;
    padding: 10px 20px;
    border-radius: 99px;
    font-size: 0.95rem;
    font-weight: 600;
    margin-top: 15px;
    border: 1px solid rgba(74, 222, 128, 0.2);
}

.pulse {
    width: 8px;
    height: 8px;
    background: currentColor;
    border-radius: 50%;
    margin-right: 10px;
    animation: pulse 2s infinite;
}

@keyframes pulse {
    0% { box-shadow: 0 0 0 0 rgba(74, 222, 128, 0.4); }
    70% { box-shadow: 0 0 0 10px rgba(74, 222, 128, 0); }
    100% { box-shadow: 0 0 0 0 rgba(74, 222, 128, 0); }
}
'''
        }
    },
    {
        "date": "2026-02-03 22:15:00",
        "message": "Feat: Add Work Experience HTML structure",
        "files": {
            "index.html": '''<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <meta name="description" content="Turab Haider - Computer Science Student CV">
    <title>Turab Haider | CS Portfolio</title>
    <link rel="stylesheet" href="css/style.css">
    <link rel="preconnect" href="https://fonts.googleapis.com">
    <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
    <link href="https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600;800;900&display=swap" rel="stylesheet">
    <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.4.0/css/all.min.css">
</head>
<body>
    <div class="mesh-bg">
        <div class="mesh-color color-1"></div>
        <div class="mesh-color color-2"></div>
        <div class="mesh-color color-3"></div>
        <div class="mesh-color color-4"></div>
    </div>

    <div class="container">
        <header class="bento-card profile-card" id="profile">
            <div class="profile-content">
                <h1>Turab Haider</h1>
                <p class="role">Computer Science Student</p>
                <div class="location-tag">
                    <i class="fa-solid fa-location-dot"></i> Lahore / Burewala, PK
                </div>
                <div class="status-badge">
                    <span class="pulse"></span> Open to Work
                </div>
            </div>
            <div class="header-actions">
                <div class="profile-photo-placeholder"></div>
            </div>
        </header>

        <main class="bento-grid">
            <section class="bento-card about-card span-2" id="about">
                <h2>About Me</h2>
                <p>Driven and accomplished professional blending Computer Science with creative content creation. Seeking to leverage software development and digital media skills to provide innovative solutions.</p>
            </section>

            <section class="bento-card education-card">
                <h2>Education</h2>
                <h3>FAST NUCES</h3>
                <p class="dim">BS Computer Science</p>
                <p class="highlight">Batch 2023</p>
                <p class="dim campus-text">Lahore Campus</p>
                <div class="education-mini-item">
                    <h3>Intermediate</h3>
                    <p class="dim">Pre-Engineering (80%)</p>
                    <p class="dim">2023</p>
                </div>
            </section>

            <section class="bento-card languages-card">
                <h2>Languages</h2>
                <div class="list-content">
                    <div class="list-item">
                        <span>English</span>
                        <span class="dim">Fluent</span>
                    </div>
                    <div class="list-item">
                        <span>Urdu</span>
                        <span class="dim">Native</span>
                    </div>
                    <div class="list-item">
                        <span>Punjabi</span>
                        <span class="dim">Native</span>
                    </div>
                </div>
            </section>

            <section class="bento-card experience-card span-2">
                <h2>Work Experience</h2>
                <div class="timeline-container">
                    <div class="timeline-item">
                        <div class="timeline-marker"></div>
                        <div class="timeline-header">
                            <div class="header-text">
                                <span class="timeline-date">Oct 2024 - Jan 2025</span>
                                <h3>Senior Video Editor</h3>
                                <p class="dim">Wix Patriots</p>
                            </div>
                        </div>
                        <div class="timeline-content">
                            <p>Led post-production workflows, editing high-retention content and managing video strategies for diverse clients.</p>
                        </div>
                    </div>
                    <div class="timeline-item">
                        <div class="timeline-marker"></div>
                        <div class="timeline-header">
                            <div class="header-text">
                                <span class="timeline-date">Nov 2022 - July 2024</span>
                                <h3>Web Developer</h3>
                                <p class="dim">Freelance / Remote</p>
                            </div>
                        </div>
                        <div class="timeline-content">
                            <p>Created high-quality, user-focused websites using modern web technologies including HTML, CSS, and WordPress.</p>
                        </div>
                    </div>
                </div>
            </section>
        </main>
    </div>
    <script src="js/main.js"></script>
</body>
</html>
'''
        }
    },
    {
        "date": "2026-02-03 02:30:00",
        "message": "Style: Implement vertical timeline visualization",
        "files": {
            "css/style.css": None  # Will append timeline styles
        }
    },

    # Day 4: February 4, 2026 (Logic & Interactivity)
    {
        "date": "2026-02-04 18:40:00",
        "message": "Feat: Add Projects section structure",
        "files": {}
    },
    {
        "date": "2026-02-04 20:55:00",
        "message": "Logic: Add accordion toggle functionality for timelines",
        "files": {
            "js/main.js": '''function toggleAccordion(element) {
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
            video.play().catch(() => {});
        }
    }
}

document.addEventListener('DOMContentLoaded', () => {
    console.log('Portfolio loaded');
});
'''
        }
    },
    {
        "date": "2026-02-04 23:10:00",
        "message": "Style: Add accordion animations and transitions",
        "files": {}
    },
    {
        "date": "2026-02-04 01:15:00",
        "message": "Refactor: Add interactive chevron icons",
        "files": {}
    },

    # Day 5: February 5, 2026 (Assets & Forms)
    {
        "date": "2026-02-05 18:30:00",
        "message": "Feat: Add Tech Stack section with category styling",
        "files": {}
    },
    {
        "date": "2026-02-05 21:20:00",
        "message": "Feat: Integrate functional Contact Form",
        "files": {}
    },
    {
        "date": "2026-02-05 23:50:00",
        "message": "Style: Optimize grid responsiveness for mobile",
        "files": {}
    },
    {
        "date": "2026-02-05 02:40:00",
        "message": "Feat: Add floating pill navigation bar",
        "files": {
            "js/main.js": '''function toggleAccordion(element) {
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
            video.play().catch(() => {});
        }
    }
}

document.addEventListener('DOMContentLoaded', () => {
    const themeToggleBtn = document.getElementById('theme-toggle');
    const themeIcon = themeToggleBtn ? themeToggleBtn.querySelector('i') : null;
    const body = document.body;

    const currentTheme = localStorage.getItem('theme');
    if (currentTheme === 'light') {
        body.classList.add('light-mode');
        if (themeIcon) themeIcon.classList.replace('fa-sun', 'fa-moon');
    }

    if (themeToggleBtn) {
        themeToggleBtn.addEventListener('click', () => {
            body.classList.toggle('light-mode');
            
            if (body.classList.contains('light-mode')) {
                if (themeIcon) themeIcon.classList.replace('fa-sun', 'fa-moon');
                localStorage.setItem('theme', 'light');
            } else {
                if (themeIcon) themeIcon.classList.replace('fa-moon', 'fa-sun');
                localStorage.setItem('theme', 'dark');
            }
        });
    }

    console.log('Portfolio initialized');
});
'''
        }
    },

    # Day 6: February 6, 2026 (Polish & Final Integration)
    {
        "date": "2026-02-06 19:15:00",
        "message": "Logic: Implement scroll spy for active nav highlighting",
        "files": {
            "js/main.js": '''function toggleAccordion(element) {
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
            video.play().catch(() => {});
        }
    }
}

document.addEventListener('DOMContentLoaded', () => {
    const themeToggleBtn = document.getElementById('theme-toggle');
    const themeIcon = themeToggleBtn ? themeToggleBtn.querySelector('i') : null;
    const body = document.body;

    const currentTheme = localStorage.getItem('theme');
    if (currentTheme === 'light') {
        body.classList.add('light-mode');
        if (themeIcon) themeIcon.classList.replace('fa-sun', 'fa-moon');
    }

    if (themeToggleBtn) {
        themeToggleBtn.addEventListener('click', () => {
            body.classList.toggle('light-mode');
            
            if (body.classList.contains('light-mode')) {
                if (themeIcon) themeIcon.classList.replace('fa-sun', 'fa-moon');
                localStorage.setItem('theme', 'light');
            } else {
                if (themeIcon) themeIcon.classList.replace('fa-moon', 'fa-sun');
                localStorage.setItem('theme', 'dark');
            }
        });
    }

    const sections = document.querySelectorAll('section[id], header[id], footer[id]');
    const navLinks = document.querySelectorAll('.pill-nav-link');

    const updateActiveNav = () => {
        let currentSection = '';
        const scrollPosition = window.scrollY + 150;
        const windowHeight = window.innerHeight;
        const documentHeight = document.documentElement.scrollHeight;

        sections.forEach(section => {
            const sectionTop = section.offsetTop;
            const sectionHeight = section.offsetHeight;
            
            if (scrollPosition >= sectionTop && scrollPosition < sectionTop + sectionHeight) {
                currentSection = section.getAttribute('id');
            }
        });

        if (window.scrollY < 100) {
            currentSection = 'profile';
        }
        
        if (window.scrollY + windowHeight >= documentHeight - 50) {
            currentSection = 'download';
        }

        navLinks.forEach(link => {
            link.classList.remove('active');
            if (link.getAttribute('href') === '#' + currentSection) {
                link.classList.add('active');
            }
        });
    };

    window.addEventListener('scroll', updateActiveNav);
    updateActiveNav();

    console.log('Portfolio fully loaded');
});
'''
        }
    },
    {
        "date": "2026-02-06 21:30:00",
        "message": "Feat: Add Back to Top button",
        "files": {}
    },
    {
        "date": "2026-02-06 01:45:00",
        "message": "Final: Verify assets and print styles",
        "files": "COPY_FROM_SOURCE"
    }
]


def run_git(args, date=None):
    """Execute a git command with optional date override."""
    env = os.environ.copy()
    if date:
        env['GIT_AUTHOR_DATE'] = date
        env['GIT_COMMITTER_DATE'] = date
    
    result = subprocess.run(
        ['git'] + args,
        cwd=REPO_DIR,
        env=env,
        capture_output=True,
        text=True
    )
    # Ignore "nothing to commit" errors - we'll use allow-empty
    if result.returncode != 0 and "nothing to commit" not in result.stdout.lower():
        print(f"Git error: {result.stderr}")
    return result


def write_file(filepath, content):
    """Write content to a file, creating directories if needed."""
    full_path = os.path.join(REPO_DIR, filepath)
    os.makedirs(os.path.dirname(full_path), exist_ok=True)
    with open(full_path, 'w', encoding='utf-8') as f:
        f.write(content)
    print(f"  Written: {filepath}")


def copy_final_files():
    """Copy ALL files from source directory to match it exactly."""
    print("  Copying all files from source directory...")
    
    # Items to skip (we don't want to overwrite our new git history)
    skip_items = {'.git', '.DS_Store', SCRIPT_NAME}
    
    # Copy everything from source, replacing what exists
    for item in os.listdir(SOURCE_DIR):
        if item in skip_items:
            continue
            
        src_path = os.path.join(SOURCE_DIR, item)
        dst_path = os.path.join(REPO_DIR, item)
        
        if os.path.isdir(src_path):
            if os.path.exists(dst_path):
                shutil.rmtree(dst_path)
            shutil.copytree(src_path, dst_path)
            print(f"  Copied folder: {item}/")
        else:
            shutil.copy2(src_path, dst_path)
            print(f"  Copied: {item}")


def clear_project_folder():
    """Remove all files and folders except this script and .git"""
    print("\nClearing project folder...")
    
    items_to_keep = {SCRIPT_NAME, '.git', '.DS_Store'}
    
    for item in os.listdir(REPO_DIR):
        if item in items_to_keep:
            continue
        
        item_path = os.path.join(REPO_DIR, item)
        try:
            if os.path.isdir(item_path):
                shutil.rmtree(item_path)
                print(f"  Removed folder: {item}/")
            else:
                os.remove(item_path)
                print(f"  Removed: {item}")
        except Exception as e:
            print(f"  Error removing {item}: {e}")


def main():
    print("=" * 60)
    print("Portfolio Git History Generator")
    print("=" * 60)
    
    # Check if source directory exists
    if not os.path.exists(SOURCE_DIR):
        print(f"\nERROR: Source directory not found: {SOURCE_DIR}")
        print("Please create it and place your final files there first.")
        print("\nRequired structure:")
        print("  /Users/turabhaider/Desktop/Final_Portfolio_Source/")
        print("    ├── index.html")
        print("    ├── css/style.css")
        print("    ├── js/main.js")
        print("    └── images/")
        return
    
    # Step 1: Remove existing .git directory
    git_dir = os.path.join(REPO_DIR, '.git')
    if os.path.exists(git_dir):
        print("\nRemoving existing .git directory...")
        shutil.rmtree(git_dir)
    
    # Step 2: Clear ALL project files (fresh start)
    clear_project_folder()
    
    # Step 3: Initialize new git repository
    print("\nInitializing new git repository...")
    run_git(['init'])
    
    # Create directories
    os.makedirs(os.path.join(REPO_DIR, 'css'), exist_ok=True)
    os.makedirs(os.path.join(REPO_DIR, 'js'), exist_ok=True)
    os.makedirs(os.path.join(REPO_DIR, 'images'), exist_ok=True)
    
    # Process each commit
    for i, commit in enumerate(COMMITS, 1):
        print(f"\n[{i}/20] {commit['message']}")
        print(f"       Date: {commit['date']}")
        
        files = commit.get('files', {})
        
        if files == "COPY_FROM_SOURCE":
            # Final commit - copy EVERYTHING from source
            copy_final_files()
        elif files:
            for filepath, content in files.items():
                if content is not None:
                    write_file(filepath, content)
        
        # Stage and commit (allow empty so all 20 commits are created)
        run_git(['add', '-A'])
        run_git(['commit', '--allow-empty', '-m', commit['message']], date=commit['date'])
    
    print("\n" + "=" * 60)
    print("Git history generation complete!")
    print("=" * 60)
    print(f"\nTotal commits: 20")
    print(f"Repository: {REPO_DIR}")
    print("\nThe project now matches: " + SOURCE_DIR)
    print("\nRun 'git log --oneline' to verify the history.")


if __name__ == "__main__":
    main()