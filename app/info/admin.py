from django.contrib import admin
from .models import Employees,Position

# Register your models here.
@admin.register(Employees)
class EmployessAdmin(admin.ModelAdmin):
    list_display = ("name","age","office","position",)
    list_display_links = ("name",)
    list_filter = ("name","position")
    search_fields = ("name","slug")


@admin.register(Position)
class PositionAdmin(admin.ModelAdmin):
    list_display = ("name",)
    list_filter = ("name",)