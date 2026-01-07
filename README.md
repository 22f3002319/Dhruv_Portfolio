# Python Developer Portfolio

A production-ready portfolio application built with FastAPI, showcasing backend engineering expertise in Python, trading systems, system design, and production-grade architectures.

## Architecture

This portfolio is built as a single FastAPI application with server-side rendering using Jinja2 templates. The architecture emphasizes:

- **Backend-first approach**: FastAPI serves all routes and templates
- **Server-side rendering**: Jinja2 templates for clean, SEO-friendly pages
- **Static file serving**: CSS and JavaScript served via FastAPI static files
- **Minimal frontend dependencies**: Bootstrap 5 and Chart.js via CDN
- **Single deployment unit**: Backend and frontend deployed together

## Tech Stack

- **Backend**: FastAPI (Python 3.9+)
- **Templates**: Jinja2
- **Styling**: Bootstrap 5 (CDN)
- **Charts**: Chart.js (CDN)
- **Server**: Uvicorn

## Project Structure

```
portfolio/
├── app/
│   ├── __init__.py
│   ├── main.py                 # FastAPI application entry point
│   ├── routers/
│   │   ├── __init__.py
│   │   └── pages.py            # Route handlers
│   ├── data/
│   │   ├── __init__.py
│   │   ├── projects.py         # Project and case study data
│   │   ├── experience.py       # Experience and principles data
│   │   └── charts.py           # Chart data configuration
│   ├── templates/
│   │   ├── base.html           # Base template with navigation
│   │   ├── home.html           # Home page
│   │   ├── case_studies.html   # Case studies page
│   │   ├── projects.html       # Projects page
│   │   └── contact.html        # Contact page
│   └── static/
│       ├── css/
│       │   └── style.css       # Custom styles
│       └── js/
│           └── charts.js       # Chart utilities
├── requirements.txt
├── README.md
└── Dockerfile
```
## Docker

Build and run with Docker:

```bash
docker build -t portfolio .
docker run -p 8000:8000 portfolio
```

## Routes

- `GET /` - Home page with hero section, tech stack, and focus areas chart
- `GET /case-studies` - System design case studies
- `GET /projects` - Deployed projects showcase
- `GET /contact` - Contact information and links
