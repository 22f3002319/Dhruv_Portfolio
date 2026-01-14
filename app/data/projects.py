"""
Project and case study data.
"""


def get_case_studies():
    """Return list of case studies with structured content."""
    return [
        {
            "slug": "trading-system-architecture",
            "title": "Algorithmic Trading System Architecture",
            "type": "Production System",
            "repo_url": "https://github.com/22f3002319/trading-system-design",
            "summary": "Comprehensive system design for a production algorithmic trading platform focused on reliability, idempotency, and transactional correctness.",
            "challenge": "Design a production trading system that handles ₹2 Cr deployed capital across multiple brokers with zero tolerance for financial errors, race conditions, or data loss.",
            "design_decisions": [
                "Explicit order state machine with audit logging",
                "Idempotency via request IDs and DB constraints for exactly-once execution",
                "Async processing (FastAPI + Celery) to isolate external dependencies",
                "Multi-broker adapter pattern with circuit breakers and retry strategies",
                "Transactional snapshots and careful schema design for analytics/backtesting"
            ],
            "results": [
                "99.99% uptime over deployment period",
                "1,000+ orders/day with zero financial discrepancies",
                "Sub-100ms latency for critical signal-to-order paths",
                "Zero data loss in face of external API failures"
            ],
            "image": "/static/assets/trading-system-architecture.png"
        },
        {
            "slug": "real-time-alerts",
            "title": "Real-Time Trading Alerts Architecture",
            "type": "Event-Driven Architecture",
            "repo_url": "https://github.com/22f3002319/trading-alerts-system-design",
            "summary": "Design of a dual-layer notification system serving strategy and execution events with strong delivery guarantees and horizontal scalability.",
            "challenge": "Build a notification pipeline that reliably delivers 1,000+ alerts/day with <1s latency during market hours across Telegram and push notification channels.",
            "design_decisions": [
                "Event sourcing using Redis Pub/Sub for low-latency distribution",
                "Dual delivery model: Telegram for strategy events, push notifications for execution status",
                "Message IDs and deduplication to ensure idempotent delivery",
                "Circuit breakers and throttling to handle external rate limits",
                "WebSocket connection pooling and automatic reconnection handling"
            ],
            "results": [
                "<1s end-to-end delivery latency",
                "High delivery success with retries for transient failures",
                "Handled 5x traffic spikes during volatile market windows",
                "Zero missed critical SL/TP alerts in monitored period"
            ],
            "image": "/static/assets/alerts-system-architecture.png"
        },
        {
            "slug": "strategy-engineering",
            "title": "Strategy Engineering & Automation",
            "type": "Strategy Engineering",
            "repo_url": None,
            "summary": "Designed rule-based trading strategies focused on deterministic execution and system integration readiness.",
            "challenge": "Create strategies that are reproducible, auditable, and directly integrable with execution and alerting layers without exposing proprietary logic.",
            "design_decisions": [
                "Separation between signal generation and execution",
                "Config-driven parameters and test harness for backtesting",
                "Validation pipelines and monitoring for deployed strategies"
            ],
            "results": [
                "Produced deterministic signals ready for production execution",
                "Integrated validation and backtesting artifacts for strategy QA"
            ],
            "image": None
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


