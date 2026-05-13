METRICS = [
    {"label": "Waste Collected", "value": "18.7 t", "delta": "+12.4%", "tone": "green"},
    {"label": "Methane Produced", "value": "4,280 m3", "delta": "+8.1%", "tone": "blue"},
    {"label": "Billing Revenue", "value": "$96.4k", "delta": "+5.8%", "tone": "slate"},
    {"label": "Carbon Reduced", "value": "34.2 tCO2e", "delta": "+16.2%", "tone": "green"},
]

COLLECTIONS = [
    {"route": "North Grid A7", "worker": "Asha Perera", "truck": "TRK-104", "status": "Live", "progress": 78},
    {"route": "Lakeside B2", "worker": "Nimal Silva", "truck": "TRK-088", "status": "Delayed", "progress": 43},
    {"route": "Civic Center C1", "worker": "Maya Chen", "truck": "EV-021", "status": "Verified", "progress": 100},
]

NOTIFICATIONS = [
    "Organic collection scheduled tomorrow at 07:30",
    "Recycling credit of $6.80 applied to household bill",
    "Methane cylinder batch MTH-22 ready for distribution",
    "District 4 contamination rate exceeded threshold",
]

GAUGES = [
    {"label": "Digester Health", "value": 91, "unit": "%"},
    {"label": "Gas Purity", "value": 96, "unit": "%"},
    {"label": "Pressure", "value": 74, "unit": "bar"},
    {"label": "Cylinder Fill", "value": 68, "unit": "%"},
]

TIMELINE = [
    ("07:15", "Route A7 started household collection"),
    ("08:40", "QR verification completed for 248 bins"),
    ("10:05", "Organic load delivered to methane plant"),
    ("11:30", "Recycling inventory updated for PET and glass"),
]
