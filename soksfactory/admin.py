from django.contrib import admin


from soksfactory.models.modelsINEM import (Counterparty, Individuals, Employes, Department, JobTitle)
from soksfactory.models.modelsOTHERS import (SpecialKeys, TypeSpecialKeys)
from django.apps import apps

# Получаем все модели из текущего приложения
app_models = apps.get_app_config('soksfactory').get_models()


class TypeSpecialKeysAdmin(admin.ModelAdmin):
    list_coletions = ['name_type_special_keys']
    list_display = list_coletions
    search_fields = list_coletions
    list_filter = list_coletions
    fields = list_coletions
    app_label='My App Group'
    

admin.site.register(TypeSpecialKeys, TypeSpecialKeysAdmin)

class SpecialKeysAdmin(admin.ModelAdmin):
    list_coletions = ['type_special_keys_fk', 'name_special_keys']
    list_display = list_coletions
    search_fields = list_coletions
    list_filter = list_coletions
    fields = list_coletions
    app_label='My App Group'

admin.site.register(SpecialKeys, SpecialKeysAdmin)


class CounterpartyAdmin(admin.ModelAdmin):
    list_coletions = ['name_counterparty', 'inn_individuals', 'phone_number']
    list_display = list_coletions
    search_fields = list_coletions
    list_filter = list_coletions
    fields = list_coletions

admin.site.register(Counterparty, CounterpartyAdmin)

class EmployesAdmin(admin.ModelAdmin):
    list_coletions = ['date_of_employment', 'individuals_fk', 'department_fk', 'job_title_fk', 'salary']
    list_display = list_coletions
    search_fields = list_coletions
    list_filter = list_coletions
    fields = list_coletions

admin.site.register(Employes, EmployesAdmin)

class DepartmentAdmin(admin.ModelAdmin):
    
    list_coletions = ['name_department']
    list_display = list_coletions
    search_fields = list_coletions
    list_filter = list_coletions
    fields = list_coletions

admin.site.register(Department, DepartmentAdmin)

class JobTitleAdmin(admin.ModelAdmin):
    
    list_coletions = ['name_jobTitle']
    list_display = list_coletions
    search_fields = list_coletions
    list_filter = list_coletions
    fields = list_coletions

admin.site.register(JobTitle, JobTitleAdmin)

class IndividualsAdmin(admin.ModelAdmin):
    # Определите поля, которые будут отображаться в административной панели
    list_display = ['full_name_individuals', 'gender', 'birthday', 'phone_number', 'biography']

    # Группируем поля
    fieldsets = (
        ('Информация о человеке', {
            'fields': ('second_name_individuals', 'first_name_individuals', 'surname_individuals', 'full_name_individuals')
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



