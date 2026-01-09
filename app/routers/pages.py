"""
Page route handlers for the portfolio application.
"""
from fastapi import APIRouter, Request
from fastapi.responses import HTMLResponse
from starlette.templating import Jinja2Templates

# Initialize templates
templates = Jinja2Templates(directory="app/templates")

router = APIRouter()

from app.data import projects, experience, charts


@router.get("/", response_class=HTMLResponse)
async def home(request: Request):
    """Home page route."""
    return templates.TemplateResponse(
        "home.html",
        {
            "request": request,
            "chart_data": charts.get_backend_focus_chart_data()
        }
    )


@router.get("/case-studies", response_class=HTMLResponse)
async def case_studies(request: Request):
    """Case studies page route."""
    return templates.TemplateResponse(
        "case_studies.html",
        {
            "request": request,
            "case_studies": projects.get_case_studies()
        }
    )


@router.get("/projects", response_class=HTMLResponse)
async def projects_page(request: Request):
    """Projects page route."""
    return templates.TemplateResponse(
        "projects.html",
        {
            "request": request,
            "projects": projects.get_projects()
        }
    )


@router.get("/contact", response_class=HTMLResponse)
async def contact(request: Request):
    """Contact page route."""
    return templates.TemplateResponse(
        "contact.html",
        {
            "request": request
        }
    )

@router.get("/certificates", response_class=HTMLResponse)
async def certificates(request: Request):
    """Contact page route."""
    return templates.TemplateResponse(
        "certifications.html",
        {
            "request": request,
            "certifications": certifications.get_certifications()
        }
    )
