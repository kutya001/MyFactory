# from django.db import models

# Create your models here.

# class BaseModel(models.Model):
#     created_date = models.DateTimeField(verbose_name="Дата создания", auto_now_add=True)
#     updated_date = models.DateTimeField(verbose_name="Дата изменения", auto_now=True)
#     deleted_date = models.DateTimeField(verbose_name="Дата удаления", null=True, default= None)

#     class Meta:
#         abstract = True

# class Gender(BaseModel):

#     gender = models.CharField(_("Пол"), max_length=50)

#     class Meta:
#         db_table = "socks_factory_" + "gender"

#     def __str__(self) -> str:
#         return f"{self.gender}"



# class Color(BaseModel):

#     color_name = models.CharField(_("Категория"), max_length=50)

#     class Meta:
#         db_table = "socks_factory_" + "color"

#     def __str__(self) -> str:
#         return f"{self.color_name}"



# class CategoryNamenclature(BaseModel):

#     category_name = models.CharField(_("Категория"), max_length=50)

#     class Meta:
#         db_table = "socks_factory_" + "category_name"

#     def __str__(self) -> str:
#         return f"{self.category_name}"
    


# class Article(BaseModel):

#     article_name = models.CharField(_("Артикул"), max_length=50)

#     class Meta:
#         db_table = "socks_factory_" + "article_name"

#     def __str__(self) -> str:
#         return f"{self.article_name}"
    

    
# class Nomenclature(BaseModel):

#     category = models.ForeignKey(CategoryNamenclature, verbose_name=_("Категория"), on_delete=models.CASCADE)
#     article = models.ForeignKey(Article, verbose_name=_("Артикул"), on_delete=models.CASCADE)
#     nomenclature_name = models.CharField(_("Номенклатура"), max_length=50)
#     gender = models.ForeignKey(Gender, verbose_name=_("Пол"), on_delete=models.CASCADE, null=True)

#     class Meta:
#         db_table = "socks_factory_" + "nomenclature_name"

#     def __str__(self) -> str:
#         return f"{self.nomenclature_name}"  



# class Counterparties(BaseModel):

#     counterparties_name = models.CharField(_("Контрагент"), max_length=50)

#     class Meta:
#         db_table = "socks_factory_" + "counterparties_name"

#     def __str__(self) -> str:
#         return f"{self.counterparties_name}"



# class OrderDocument(BaseModel):

#     counterparties = models.ForeignKey(Counterparties, verbose_name=_("Контрагент"), on_delete=models.CASCADE, unique=False)
#     total = models.PositiveIntegerField("Общая сумма заказа", default=0)
#     note = models.CharField(_("Примечание"), max_length=100, null=True, unique=False)

#     class Meta:
#         db_table = "socks_factory_" + "order_document"

#     def __str__(self) -> str:
#         return f"{self.counterparties}"



# class OrderItem(BaseModel):
    
#     order_document = models.ForeignKey(OrderDocument, verbose_name=_("Документ"), on_delete=models.CASCADE, related_name="order_document")
#     serial_numb_spec = models.IntegerField(_("Порядковый номер плана"),auto_created=True)
#     nomenclature = models.ForeignKey(Nomenclature, verbose_name=_("Номенклатура"), on_delete=models.CASCADE)
#     color = models.ForeignKey(Color, verbose_name=_("Цвет"), on_delete=models.CASCADE, null=True)
#     color_discription = models.CharField(_("Описание к цвету"), max_length=100, null=True, unique=False)
#     price = models.IntegerField(_("Цена"))
#     amount = models.IntegerField(_("Кол-во"))
#     summ = models.IntegerField(_("Сумма"), null=True)
#     note = models.CharField(_("Примечание"), max_length=100, null=True, unique=False)

#     class Meta:
#         db_table = "socks_factory_" + "order_item"

#     def __str__(self) -> str:
#         return f"{self.nomenclature}"