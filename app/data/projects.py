"""
Project and case study data.
"""


def get_case_studies():
    """Return list of case studies."""
    return [
        {
            "title": "Trading System Architecture",
            "repo_url": "https://github.com/22f3002319/trading-system-design",
            "description": (
                "A design-first architecture for a production-grade trading system, "
                "focusing on order lifecycle modeling, API design, idempotency, "
                "database schema design, asynchronous processing, failure recovery, "
                "monitoring, and operational runbooks.\n\n"
                "This repository contains architecture documents, diagrams, "
                "and trade-off analysis without exposing proprietary code."
            )
        },
        {
            "title": "Real-Time Trading Alerts Architecture",
            "repo_url": "https://github.com/22f3002319/trading-alerts-system-design",
            "description": (
                "A system design case study for a real-time trading alerts pipeline, "
                "built using event-driven principles.\n\n"
                "Focus areas include rule evaluation, alert deduplication, "
                "backpressure handling, WebSocket-based delivery, "
                "retry strategies, and horizontal scalability."
            )
        },
        
        {
            "title": "Strategy Engineering & Automation",
            "repo_url": None,
            "description": (
                "Designed and implemented multiple rule-based trading strategies with a focus on "
                "deterministic execution logic and system integration readiness.\n\n"
                "Engineering Focus:\n"
                "• Clean separation between signal generation and execution\n"
                "• Deterministic, reproducible rule evaluation\n"
                "• Config-driven strategy parameters\n"
                "• Outputs designed for direct integration with order and alert systems\n"
                "• Validation and backtesting considerations\n\n"
                "The emphasis is on engineering discipline and system compatibility, "
                "not on exposing proprietary trading logic."
            )
        }
    ]


def get_projects():
    """Return list of deployed projects."""
    return [
        {
            "title": "Customer Purchase Value Prediction",
            "description": (
                "Predict how much a customer will spend during a session using behavioral, "
                "device, traffic, and geographic data."
            ),
            "tech_highlights": ["Python", "pandas", "numpy", "scikit-learn", "matplotlib", "seaborn"],
            "repo_url": "https://github.com/22f3002319/ml-customer-purchase-value-prediction"
        },

        {
            "title": "ARIA v2.0 — Two-way Sign Language Interpreter",
            "description": (
                "Production-grade two-way sign language interpreter built for the "
                "NXT Wave × OpenAI Buildathon. Features an async FastAPI backend, "
                "JWT authentication, encrypted per-user API keys, file storage, "
                "history tracking, and modular microservices."
            ),
            "tech_highlights": ["FastAPI", "JWT", "PostgreSQL", "Async Processing"],
            "demo_frontend": "https://aria-eight-alpha.vercel.app/",
            "demo_backend": "https://aria-ddqo.onrender.com/",
            "repo_url": "https://github.com/22f3002319/ARIA"
        },
        {
            "title": "IITM Assignment API",
            "description": (
                "FastAPI service that accepts assignment-style questions along with "
                "uploaded CSV, ZIP, PDF, and Excel files and returns automated answers "
                "using an LLM backend with safe function-calling."
            ),
            "tech_highlights": ["FastAPI", "LLM Integration", "File Processing"],
            "demo_url": "https://tds-project-12-1.onrender.com",
            "repo_url": "https://github.com/22f3002319/tds_project_12"
        },
        {
            "title": "LLM Agent",
            "description": (
                "Deployed LLM agent application demonstrating advanced AI capabilities "
                "with production-ready architecture."
            ),
            "tech_highlights": ["LLM", "API Design", "Deployment"],
            "demo_url": "https://tds-bonus-project-llm-agent-three.vercel.app/",
            "repo_url": "https://github.com/22f3002319/tds-bonus-project-LLM-Agent"
        },
        {
            "title": "Auto PPT Generator",
            "description": (
                "Automated presentation generator with intelligent content creation "
                "and formatting capabilities."
            ),
            "tech_highlights": ["Automation", "Content Generation", "API Integration"],
            "demo_url": "https://tds-bonus-project-auto-ppt-generato-rho.vercel.app/",
            "repo_url": "https://github.com/22f3002319/tds-bonus-project-Auto-PPT-Generator-GyaanSetu-Deck/"
        },
        {
            "title": "Vehicle Parking Management System",
            "description": (
                "Backend system demonstrating Redis-based caching and Celery-powered "
                "background jobs for booking workflows and notifications."
            ),
            "tech_highlights": ["Redis", "Celery", "Background Jobs", "Caching"],
            "demo_url": None,
            "repo_url": "https://github.com/22f3002319/Vehicle-Parking-App---22f3002319"
        }
    ]


