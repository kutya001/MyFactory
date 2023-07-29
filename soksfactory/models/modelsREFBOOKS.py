from django.db import models
from django.utils.translation import gettext_lazy as _
from .modelsINEM import BaseModel


class CategoryNomenclature(BaseModel):

    name_category_nomenclature = models.CharField(_("Категория номенклатуры :"), max_length=50)    

    class Meta:
        verbose_name = "Категория номенклатуры"
        verbose_name_plural = "Категория номенклатуры"
        db_table = "socks_factory_" + "category_nomenclature"
    
    def __str__(self) -> str:
        return f"{self.name_category_nomenclature}"


class TypeNomenclature(BaseModel):

    name_type_nomenclature = models.CharField(_("Группа номенклатуры :"), max_length=50)    

    class Meta:
        verbose_name = "Вид номенклатуры"
        verbose_name_plural = "Вид номенклатуры"
        db_table = "socks_factory_" + "type_nomenclature"
    
    def __str__(self) -> str:
        return f"{self.name_type_nomenclature}"
    

class Nomenclature(BaseModel):

    category_nomenclature_fk = models.ForeignKey(CategoryNomenclature, verbose_name=_("Категория номенклатуры :"), on_delete=models.CASCADE)
    type_nomenclature_fk = models.ForeignKey(TypeNomenclature, verbose_name=_("Вид номенклатуры:"), on_delete=models.CASCADE)
    name_nomenclature = models.CharField(_("Номенклатура"), max_length=50)

    class Meta:
        verbose_name = "Номенклатура"
        verbose_name_plural = "Номенклатура"
        db_table = "socks_factory_" + "nomenclature"
    
    def __str__(self) -> str:
        return f"{self.name_nomenclature}"


class CharacteristicDOC(BaseModel):

    nomenclature_fk = models.ForeignKey(Nomenclature, verbose_name=_("Номенклатура :"), on_delete=models.CASCADE)
    name_сharacteristic = models.CharField(_("Характеристика : "), max_length=50)

    class Meta:
        verbose_name = "Характеристика"
        verbose_name_plural = "Характеристика"
        db_table = "socks_factory_" + "characteristic_DOC"
    
    def __str__(self) -> str:
        return f"{self.name_сharacteristic}"


class PropertyChar(BaseModel):

    property_char_name = models.CharField(_("Свойство :"), max_length=50)    

    class Meta:
        verbose_name = "Свойство"
        verbose_name_plural = "Свойство"
        db_table = "socks_factory_" + "property_char"
    
    def __str__(self) -> str:
        return f"{self.property_char_name}"


class ValueChar(BaseModel):

    property_char_fk = models.ForeignKey(PropertyChar, verbose_name=_("Свойство :"), on_delete=models.CASCADE)
    value_char = models.CharField(_("Значение : "), max_length=50)

    class Meta:
        verbose_name = "Значение"
        verbose_name_plural = "Значение"
        db_table = "socks_factory_" + "value_char"
    
    def __str__(self) -> str:
        return f"{self.value_char}"


class CharacteristicITEM(BaseModel):

    characteristic_doc_fk = models.ForeignKey(CharacteristicDOC, verbose_name=_("Номенклатура :"), on_delete=models.CASCADE)
    property_fk = models.ForeignKey(PropertyChar, verbose_name=_("Свойство :"), on_delete=models.CASCADE)
    value_fk = models.ForeignKey(ValueChar, verbose_name=_("Значение :"), on_delete=models.CASCADE)
    text_name = models.CharField(_("Текст : "), max_length=50)

    class Meta:
        verbose_name = "Характеристика элемент"
        verbose_name_plural = "Характеристика элемент"
        db_table = "socks_factory_" + "characteristic_ITEM"
    
    def __str__(self) -> str:
        return f"{self.text_name}"


class Panton(BaseModel):

    color_name = models.CharField(_("Пантон : "), max_length=100)

    class Meta:
        verbose_name = "Пантон"
        verbose_name_plural = "Пантон"
        db_table = "socks_factory_" + "pantone"
    
    def __str__(self) -> str:
        return f"{self.color_name}"


class Color(BaseModel):

    pantone_fk = models.ForeignKey(Panton, verbose_name=_("Пантон :"), on_delete=models.CASCADE)
    color_note = models.CharField(_("Примечание к цвету :"), max_length=100)
    color_name = models.CharField(_("Цвет : "), max_length=200)

    class Meta:
        verbose_name = "Цвет"
        verbose_name_plural = "Цвет"
        db_table = "socks_factory_" + "color"
    
    def __str__(self) -> str:
        return f"{self.color_name}"


from .modelsOTHERS import SpecialKeys
class SpecificationDOC(BaseModel):

    characteristic_fk = models.ForeignKey(CharacteristicDOC, verbose_name=_("Характеристика :"), on_delete=models.CASCADE)
    name_specification = models.CharField(_("Название спецификации : "), max_length=50)
    special_key = models.ForeignKey(SpecialKeys, verbose_name=_("Ключ :"), on_delete=models.CASCADE)

    class Meta:
        verbose_name = "Спецификация"
        verbose_name_plural = "Спецификация"
        db_table = "socks_factory_" + "specificationDOC"
    
    def __str__(self) -> str:
        return f"{self.name_specification} / {self.special_key}"
    
class Unit(BaseModel):

    unit_name = models.CharField(_("Единица измерения : "), max_length=100)

    class Meta:
        verbose_name = "Единица измерения"
        verbose_name_plural = "Единица измерения"
        db_table = "socks_factory_" + "unit"
    
    def __str__(self) -> str:
        return f"{self.unit_name}"


class SpecificationITEM(BaseModel):

    specificationDOC_fk = models.ForeignKey(SpecificationDOC, verbose_name=_("Документ :"), on_delete=models.CASCADE)
    material_fk = models.ForeignKey(Nomenclature, verbose_name=_("Материал :"), on_delete=models.CASCADE)
    value = models.DecimalField(_("Значение : "), max_digits=5, decimal_places=4)
    unit = models.CharField(_(""), max_length=50)

    class Meta:
        verbose_name = "Спецификация элемент"
        verbose_name_plural = "Спецификация элемент"
        db_table = "socks_factory_" + "specificationITEM"
    
    def __str__(self) -> str:
        return f"{self.name_specification} / {self.special_key}"
