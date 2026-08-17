from django.contrib import admin
from .models import Driver, PricingTier

class PricingTierInline(admin.TabularInline):
    model = PricingTier
    extra = 1

@admin.register(Driver)
class DriverAdmin(admin.ModelAdmin):
    list_display = ('full_name', 'city', 'experience_years', 'transmission_type', 'is_available', 'is_verified')
    list_filter = ('city', 'transmission_type', 'is_available', 'is_verified')
    search_fields = ('full_name', 'city', 'phone_number')
    inlines = [PricingTierInline]