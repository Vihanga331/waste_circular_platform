def platform_navigation(request):
    nav_items = [
        ("Dashboard", "core:dashboard", "layout-dashboard"),
        ("Citizen Portal", "core:citizen", "user-round"),
        ("Admin Command", "core:admin_dashboard", "shield-check"),
        ("Collections", "core:collections", "truck"),
        ("Methane Plant", "core:methane", "gauge"),
        ("Recycling", "core:recycling", "recycle"),
        ("Analytics", "core:analytics", "chart-spline"),
        ("Smart City Map", "core:map", "map"),
        ("AI Upgrades", "core:ai", "sparkles"),
    ]
    future_items = [
        "IoT Smart Bins",
        "Carbon Credit Marketplace",
        "Blockchain Traceability",
        "Smart Energy Grid",
        "Fleet Telematics",
        "ESG Reporting",
        "Mobile App Integration",
        "Government Reporting API",
    ]
    return {"nav_items": nav_items, "future_items": future_items}
