from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import AllowAny
from rest_framework.response import Response


@api_view(["GET"])
@permission_classes([AllowAny])
def api_index(request):
    return Response(
        {
            "status": "mvp-ready",
            "authentication": ["Django sessions", "JWT planned for mobile API"],
            "endpoints": [
                "/api/auth/",
                "/api/households/",
                "/api/collections/",
                "/api/methane/",
                "/api/billing/",
                "/api/analytics/",
            ],
            "future_integrations": ["AI microservices", "WebSocket live updates", "OpenStreetMap", "IoT telemetry"],
        }
    )
