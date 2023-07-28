# from .models.modelsREFBOOKS import (CategoryNomenclature, Nomenclature, CharacteristicDOC, 
#                                     CharacteristicITEM, TypeNomenclature, PropertyChar,
#                                     ValueChar, SpecificationDOC, SpecificationITEM)

class CounterpartyGroup:
    app_name = 'soksfactory'
    group_name = 'Counterparty'
    models_list = ['Counterparty']


class SpecialKeysGroup:
    app_name = 'soksfactory'
    group_name = 'Ключи'
    models_list = ['SpecialKeys', 'TypeSpecialKeys']


class PersonsGroup:
    app_name = 'soksfactory'
    group_name = 'Кадры'
    models_list = ['Individuals', 'Employes', 'Department', 'JobTitle']


class FefGroup:
    app_name = 'soksfactory'
    group_name = 'Справочники'
    models_list = ['CategoryNomenclature', 'Nomenclature', 'CharacteristicDOC',
                   'CharacteristicITEM', 'TypeNomenclature', 'PropertyChar',
                   'ValueChar', 'SpecificationDOC', 'SpecificationITEM']
