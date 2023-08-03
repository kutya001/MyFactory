from django.contrib import admin

from soksfactory.models.modelsOTHERS import (SpecialKeys, TypeSpecialKeys)
from soksfactory.models.modelsINEM import (Counterparty, Individuals, Employes, Department, JobTitle)
from soksfactory.models.modelsREFBOOKS import (CategoryNomenclature, Nomenclature, CharacteristicDOC, 
                                    CharacteristicITEM, TypeNomenclature, PropertyChar,
                                    ValueChar, SpecificationDOC, SpecificationITEM, Color, Panton)


from soksfactory.adminclasses.adminOTHERS import TypeSpecialKeysAdmin, SpecialKeysAdmin
from soksfactory.adminclasses.adminINEM import (CounterpartyAdmin, DepartmentAdmin, 
                                                EmployesAdmin, IndividualsAdmin, 
                                                JobTitleAdmin)
from soksfactory.adminclasses.adminREFBOOKS import (CategoryNomenclatureAdmin, NomenclatureAdmin, CharacteristicDOCAdmin, 
                                    CharacteristicITEMAdmin, TypeNomenclatureAdmin, PropertyCharAdmin,
                                    ValueCharAdmin, SpecificationDOCAdmin, SpecificationITEMAdmin, ColorAdmin, PantonAdmin)


#OTHERS
admin.site.register(TypeSpecialKeys, TypeSpecialKeysAdmin)
admin.site.register(SpecialKeys, SpecialKeysAdmin)

#INEM
admin.site.register(Counterparty, CounterpartyAdmin)
admin.site.register(Employes, EmployesAdmin)
admin.site.register(Department, DepartmentAdmin)
admin.site.register(JobTitle, JobTitleAdmin)
<<<<<<< HEAD

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

=======
>>>>>>> 4a98e34a9e8f4ae5630daf8ab5d7b06d914a07b5
admin.site.register(Individuals, IndividualsAdmin)

#INEM
admin.site.register(Color, ColorAdmin)
admin.site.register(Panton, PantonAdmin)
admin.site.register(CategoryNomenclature, CategoryNomenclatureAdmin)
admin.site.register(Nomenclature, NomenclatureAdmin)
admin.site.register(CharacteristicDOC, CharacteristicDOCAdmin)
admin.site.register(CharacteristicITEM, CharacteristicITEMAdmin)
admin.site.register(TypeNomenclature, TypeNomenclatureAdmin)
admin.site.register(PropertyChar, PropertyCharAdmin)
admin.site.register(ValueChar, ValueCharAdmin)
admin.site.register(SpecificationDOC, SpecificationDOCAdmin)
admin.site.register(SpecificationITEM, SpecificationITEMAdmin)
