from django.contrib import admin
from soksfactory.models.modelsREFBOOKS import (CategoryNomenclature, Nomenclature, CharacteristicDOC, 
                                    CharacteristicITEM, TypeNomenclature, PropertyChar,
                                    ValueChar, SpecificationDOC, SpecificationITEM)

class CategoryNomenclatureAdmin(admin.ModelAdmin):
    model = CategoryNomenclature
    list_coletions = all
    list_display = list_coletions
    search_fields = list_coletions
    list_filter = list_coletions
    fields = list_coletions