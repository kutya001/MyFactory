from django.contrib import admin
from soksfactory.models.modelsREFBOOKS import (CategoryNomenclature, Nomenclature, CharacteristicDOC, 
                                    CharacteristicITEM, TypeNomenclature, PropertyChar,
                                    ValueChar, SpecificationDOC, SpecificationITEM, Color, Panton)

class ColorAdmin(admin.ModelAdmin):
    
    model = Color
    list_coletions = ['pantone_fk', 'color_note', 'color_name']
    list_display = list_coletions
    search_fields = list_coletions
    list_filter = list_coletions
    fields = list_coletions


class PantonAdmin(admin.ModelAdmin):
    
    model = Panton
    list_coletions = ['color_name']
    list_display = list_coletions
    search_fields = list_coletions
    list_filter = list_coletions
    fields = list_coletions
    
    class Media:
        css = {
            'all': ('css/assets_admin.css',)
        }
        js = ('js/assets_admin.js',)


class CategoryNomenclatureAdmin(admin.ModelAdmin):

    model = CategoryNomenclature
    list_coletions = ['name_category_nomenclature']
    list_display = list_coletions
    search_fields = list_coletions
    list_filter = list_coletions
    fields = list_coletions


class NomenclatureAdmin(admin.ModelAdmin):

    model = Nomenclature
    list_coletions = ['category_nomenclature_fk', 'type_nomenclature_fk', 'name_nomenclature']
    list_display = list_coletions
    search_fields = list_coletions
    list_filter = list_coletions
    fields = list_coletions


class CharacteristicDOCAdmin(admin.ModelAdmin):
    
    model = CharacteristicDOC
    list_coletions = ['nomenclature_fk', 'name_сharacteristic']
    list_display = list_coletions
    search_fields = list_coletions
    list_filter = list_coletions
    fields = list_coletions


class CharacteristicITEMAdmin(admin.ModelAdmin):
    
    model = CharacteristicITEM
    list_coletions = ['characteristic_doc_fk', 'property_fk', 'value_fk', 'text_name']
    list_display = list_coletions
    search_fields = list_coletions
    list_filter = list_coletions
    fields = list_coletions


class TypeNomenclatureAdmin(admin.ModelAdmin):
    
    model = TypeNomenclature
    list_coletions = ['name_type_nomenclature']
    list_display = list_coletions
    search_fields = list_coletions
    list_filter = list_coletions
    fields = list_coletions


class PropertyCharAdmin(admin.ModelAdmin):
    
    model = PropertyChar
    list_coletions = ['property_char_name']
    list_display = list_coletions
    search_fields = list_coletions
    list_filter = list_coletions
    fields = list_coletions


class ValueCharAdmin(admin.ModelAdmin):
    
    model = ValueChar
    list_coletions = ['property_char_fk', 'value_char']
    list_display = list_coletions
    search_fields = list_coletions
    list_filter = list_coletions
    fields = list_coletions


class SpecificationDOCAdmin(admin.ModelAdmin):
    
    model = SpecificationDOC
    list_coletions = ['characteristic_fk', 'name_specification', 'special_key']
    list_display = list_coletions
    search_fields = list_coletions
    list_filter = list_coletions
    fields = list_coletions


class SpecificationITEMAdmin(admin.ModelAdmin):
    
    model = SpecificationITEM
    list_coletions = ['specificationDOC_fk', 'material_fk', 'value', 'unit']
    list_display = list_coletions
    search_fields = list_coletions
    list_filter = list_coletions
    fields = list_coletions