from django.shortcuts import render
from .mock_data import COLLECTIONS, GAUGES, METRICS, NOTIFICATIONS, TIMELINE


def page(request, template_name, title, section, extra=None):
    context = {
        "title": title,
        "section": section,
        "metrics": METRICS,
        "collections": COLLECTIONS,
        "notifications": NOTIFICATIONS,
        "gauges": GAUGES,
        "timeline": TIMELINE,
    }
    if extra:
        context.update(extra)
    return render(request, template_name, context)


def dashboard(request):
    return page(request, "pages/dashboard.html", "Smart Circular Command Center", "dashboard")


def citizen(request):
    return page(request, "pages/citizen.html", "Citizen Sustainability Portal", "citizen")


def admin_dashboard(request):
    return page(request, "pages/admin_dashboard.html", "Enterprise Admin Command", "admin")


def collections(request):
    return page(request, "pages/collections.html", "Waste Collection Operations", "collections")


def methane(request):
    return page(request, "pages/methane.html", "Methane Production Monitor", "methane")


def recycling(request):
    return page(request, "pages/recycling.html", "Recycling Inventory and Marketplace", "recycling")


def analytics(request):
    return page(request, "pages/analytics.html", "Sustainability Analytics", "analytics")


def smart_map(request):
    return page(request, "pages/map.html", "Smart City Map", "map")


def ai_modules(request):
    return page(request, "pages/ai.html", "AI Upgrade Center", "ai")


def billing(request):
    return page(request, "pages/billing.html", "Citizen Billing", "billing")


def notifications(request):
    return page(request, "pages/notifications.html", "Notification Center", "notifications")


def settings(request):
    return page(request, "pages/settings.html", "Platform Settings", "settings")


def users(request):
    return page(request, "pages/users.html", "User and RBAC Management", "users")


def audit_logs(request):
    return page(request, "pages/audit_logs.html", "Audit Logs", "audit")
