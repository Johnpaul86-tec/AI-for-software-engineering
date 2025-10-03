# Mini E-Learning Platform

## Overview

This is a prototype mini e-learning platform built with HTML, CSS, and JavaScript. The platform allows users to view courses, track progress, and use a career guide to help choose the right course. It’s designed with expandable course cards and a sidebar career guide, featuring a clean gradient-based visual style.

## Features

### Course Cards

1. Each course is displayed as a card with a summary (title, description, status).
2. Clicking a course card expands it horizontally, showing:
   - Lesson list
   - Progress bar
   - "Mark as Completed" button
3. Only one card can expand at a time for clarity.

## Career Guide SidebarS

1. Located on the left sidebar for easy access.
2. Provides a dropdown of career topics (e.g., Web Development, UI/UX Design, Programming Basics).
3. Selecting a topic displays:
   - Benefits of the topic
   - Recommended course(s)
   - Enroll button that scrolls and expands the recommended course card above.

## UI / UX Design

- Harmonized gradient background and cards for soft, visually cohesive design.
- Subtle hover effects on cards and buttons.
- Responsive card expansion without splitting the page.
- Smooth scrolling to courses when enrolling from the Career Guide.

## Project Structure

mini-e-learning-platform/
│
├── index.html # Main HTML file
├── style.css # Styles (gradients, card layouts, responsive design)
├── script.js # JavaScript functionality (expandable cards, career guide)
└── README.md # Project documentation

---

## Getting Started

1. **Clone or download** the repository.
2. Open `index.html` in a modern browser.
3. Interact with the platform:
   - Click course cards to view lessons and progress.
   - Use the Career Guide sidebar to select a topic and enroll.

---

## How It Works

1. **Courses** are stored in a JavaScript array with `id`, `title`, `description`, `lessons`, and `completed` status.
2. Clicking a course triggers **card expansion** using JavaScript:
   - Adds a `.expanded` class to the card
   - Appends a right-side detail section inside the card
3. **Career Guide**:
   - Topics are mapped to recommended courses
   - Selecting a topic dynamically shows benefits and an **Enroll button**
   - Enroll button scrolls to the corresponding course card and expands it automatically
4. **Progress Tracking**:
   - Each course card displays a progress bar
   - "Mark as Completed" button updates the course status

---

## Technologies Used

- **HTML5** – Semantic markup for structure
- **CSS3** – Gradient backgrounds, hover effects, card layouts
- **JavaScript** – Dynamic card expansion, career guide, progress tracking

## Author

**Johnpaul** – Prototype designed and developed for learning purposes.
