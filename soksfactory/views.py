from django.shortcuts import render, redirect
from soksfactory.models.modelsREFBOOKS import (CategoryNomenclature, Nomenclature, CharacteristicDOC, 
                                    CharacteristicITEM, TypeNomenclature, PropertyChar,
                                    ValueChar, SpecificationDOC, SpecificationITEM, Color, Panton)


def index(request):
    return render(request, 'soksfactory/index.html')
