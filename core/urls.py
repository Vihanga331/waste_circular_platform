from django.urls import path
from . import views

app_name = "core"

urlpatterns = [
    path("", views.dashboard, name="dashboard"),
    path("citizen/", views.citizen, name="citizen"),
    path("admin-command/", views.admin_dashboard, name="admin_dashboard"),
    path("collections/", views.collections, name="collections"),
    path("methane/", views.methane, name="methane"),
    path("recycling/", views.recycling, name="recycling"),
    path("analytics/", views.analytics, name="analytics"),
    path("map/", views.smart_map, name="map"),
    path("ai/", views.ai_modules, name="ai"),
    path("billing/", views.billing, name="billing"),
    path("notifications/", views.notifications, name="notifications"),
    path("settings/", views.settings, name="settings"),
    path("users/", views.users, name="users"),
    path("audit-logs/", views.audit_logs, name="audit_logs"),
]
