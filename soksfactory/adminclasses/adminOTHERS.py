from django.contrib import admin
from soksfactory.models.modelsOTHERS import (SpecialKeys, TypeSpecialKeys)



class TypeSpecialKeysAdmin(admin.ModelAdmin):
    model = TypeSpecialKeys
    list_coletions = ['name_type_special_keys']
    list_display = list_coletions
    search_fields = list_coletions
    list_filter = list_coletions
    fields = list_coletions


class SpecialKeysAdmin(admin.ModelAdmin):
    model = SpecialKeys
    list_coletions = ['type_special_keys_fk', 'name_special_keys']
    list_display = list_coletions
    search_fields = list_coletions
    list_filter = list_coletions
    fields = list_coletions