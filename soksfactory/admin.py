from django.contrib import admin

from .models.modelsINEM import (Counterparty, Individuals, Employes, Department, JobTitle)
from .models.modelsOTHERS import (SpecialKeys, TypeSpecialKeys)

class CustomAdminSite(admin.AdminSite):
    site_header = 'My Factory Admin'  # Заголовок административной панели
    site_title = 'My Factory Admin'   # Заголовок во вкладке браузера

custom_admin_site = CustomAdminSite(name='customadmin')

custom_admin_site.register(TypeSpecialKeys, admin.ModelAdmin)
custom_admin_site.register(SpecialKeys, admin.ModelAdmin)


class CounterpartyAdmin(admin.ModelAdmin):
    
    list_display = ['name_counterparty', 'inn_individuals', 'phone_number']
    search_fields = ['name_counterparty', 'inn_individuals', 'phone_number']
    list_filter = ['name_counterparty', 'inn_individuals', 'phone_number']
    fields = ['name_counterparty', 'inn_individuals', 'phone_number']

admin.site.register(Counterparty, CounterpartyAdmin)
admin.site.register(Employes)
admin.site.register(Department)

class JobTitleAdmin(admin.ModelAdmin):
    
    list_display = ['name_jobTitle']
    search_fields = ['name_jobTitle']
    list_filter = ['name_jobTitle']
    fields = ['name_jobTitle']

admin.site.register(JobTitle, JobTitleAdmin)

class IndividualsAdmin(admin.ModelAdmin):
    # Определите поля, которые будут отображаться в административной панели
    list_display = ['full_name_individuals', 'gender', 'birthday', 'phone_number', 'biography']

    # Группируем поля
    fieldsets = (
        ('Информация о человеке', {
            'fields': ('second_name_individuals', 'first_name_individuals', 'surname_individuals')
        }),
        ('Дополнительная информация', {
            'fields': ('gender', 'birthday', 'phone_number', 'biography')
        }),
    )

    search_fields = ['full_name_individuals']
    list_filter = ['full_name_individuals']
    list_per_page = 5

    def save_model(self, request, obj, form, change):
        
        # Автоматически заполните поле "Полное имя" перед сохранением экземпляра модели
        obj.full_name_individuals = f"{obj.second_name_individuals} {obj.first_name_individuals} {obj.surname_individuals}"
        super().save_model(request, obj, form, change)

admin.site.register(Individuals, IndividualsAdmin)



