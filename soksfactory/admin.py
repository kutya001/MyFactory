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
