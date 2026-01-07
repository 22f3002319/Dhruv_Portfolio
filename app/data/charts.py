"""
Chart data for Chart.js visualizations.
"""


def get_backend_focus_chart_data():
    """Return data for backend engineering focus areas chart."""
    return {
        "labels": [
            "API Design",
            "Databases",
            "Async Processing",
            "System Design",
            "Reliability"
        ],
        "data": [25, 20, 20, 20, 15],
        "colors": [
            "rgba(54, 162, 235, 0.8)",
            "rgba(255, 99, 132, 0.8)",
            "rgba(75, 192, 192, 0.8)",
            "rgba(255, 206, 86, 0.8)",
            "rgba(153, 102, 255, 0.8)"
        ]
    }


