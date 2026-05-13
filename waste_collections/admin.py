from django.contrib import admin
from .models import WasteCategory, WasteCollection


admin.site.register(WasteCategory)


@admin.register(WasteCollection)
class WasteCollectionAdmin(admin.ModelAdmin):
    list_display = ("route_code", "truck_id", "household", "category", "status", "weight_kg", "qr_verified")
    list_filter = ("status", "qr_verified", "category")
