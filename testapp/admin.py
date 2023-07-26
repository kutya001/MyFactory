from django.contrib import admin
from .models import Country, City, Street, Position, Department

# InlineModelAdmin для моделей City и Street
class CityInline(admin.StackedInline):
    model = City
    extra = 1

class StreetInline(admin.StackedInline):
    model = Street
    extra = 1

# Admin класс для модели Country с включенными InlineModelAdmin
class CountryAdmin(admin.ModelAdmin):
    inlines = [CityInline]

# InlineModelAdmin для модели Department
class DepartmentInline(admin.StackedInline):
    model = Department
    extra = 1

# Admin класс для модели Position с включенным InlineModelAdmin
class PositionAdmin(admin.ModelAdmin):
    inlines = [DepartmentInline]

# Регистрация моделей с их админ классами
admin.site.register(Country, CountryAdmin)
admin.site.register(Position, PositionAdmin)
