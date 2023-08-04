from django import forms
from soksfactory.models.modelsREFBOOKS import (CategoryNomenclature, Nomenclature, CharacteristicDOC, 
                                    CharacteristicITEM, TypeNomenclature, PropertyChar,
                                    ValueChar, SpecificationDOC, SpecificationITEM, Color, Panton)


class CategoryNomenclatureForm(forms.ModelForm):
    class Meta:
        model = CategoryNomenclature
        fields = '__all__'
