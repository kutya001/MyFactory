from django.contrib import admin
from soksfactory.models.modelsINEM import (Counterparty, Individuals, Employes, Department, JobTitle)



class CounterpartyAdmin(admin.ModelAdmin):
    model = Counterparty
    list_coletions = ['name_counterparty', 'inn_individuals', 'phone_number']
    list_display = list_coletions
    search_fields = list_coletions
    list_filter = list_coletions
    fields = list_coletions


class EmployesAdmin(admin.ModelAdmin):
    model = Employes
    list_coletions = ['date_of_employment', 'individuals_fk', 'department_fk', 'job_title_fk', 'salary']
    list_display = list_coletions
    search_fields = list_coletions
    list_filter = list_coletions
    fields = list_coletions


class DepartmentAdmin(admin.ModelAdmin):
    model = Department
    list_coletions = ['name_department']
    list_display = list_coletions
    search_fields = list_coletions
    list_filter = list_coletions
    fields = list_coletions


class JobTitleAdmin(admin.ModelAdmin):
    model = JobTitle
    list_coletions = ['name_jobTitle']
    list_display = list_coletions
    search_fields = list_coletions
    list_filter = list_coletions
    fields = list_coletions


class IndividualsAdmin(admin.ModelAdmin):
    model = Individuals
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