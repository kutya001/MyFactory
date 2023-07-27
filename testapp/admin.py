from django.contrib import admin
from .models import Country, City, Street, Position, Department

class CountryAdmin(admin.ModelAdmin):
    list_display = ["name"]
    list_display_links = ('name',)

    class Meta:
        model = Country

admin.site.register(Country, CountryAdmin)


class CityAdmin(admin.ModelAdmin):
    list_display = ["name", 'country']
    list_display_links = ('name',)

    class Meta:
        model = City

admin.site.register(City, CityAdmin)


class StreetAdmin(admin.ModelAdmin):
    list_display = ["name", 'city']
    list_display_links = ('name',)

    class Meta:
        model = Street

admin.site.register(Street, StreetAdmin)


class PositionAdmin(admin.ModelAdmin):
    list_display = ["title"]
    list_display_links = ('title',)

    class Meta:
        model = Position

admin.site.register(Position, PositionAdmin)


class DepartmentAdmin(admin.ModelAdmin):
    list_display = ["name", 'position']
    list_display_links = ('name',)

    class Meta:
        model = Department

admin.site.register(Department, DepartmentAdmin)