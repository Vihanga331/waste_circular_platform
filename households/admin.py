from django.contrib import admin
from .models import Household


@admin.register(Household)
class HouseholdAdmin(admin.ModelAdmin):
    list_display = ("account_number", "district", "owner", "smart_bin_id")
    search_fields = ("account_number", "address", "district", "smart_bin_id")
