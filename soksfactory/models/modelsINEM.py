from django.db import models
from django.core.validators import MinLengthValidator
from django.utils.translation import gettext_lazy as _


class BaseModel(models.Model):
    created_date = models.DateTimeField(verbose_name="Дата создания", auto_now_add=True, editable=False)
    updated_date = models.DateTimeField(verbose_name="Дата изменения", auto_now=True)
    deleted_date = models.DateTimeField(verbose_name="Дата удаления", null=True, blank=True)

    class Meta:
        abstract = True


# Контрагент
class Counterparty(BaseModel):
    
    name_counterparty = models.CharField(_("Имя (Название):"), max_length=50)    
    inn_individuals = models.CharField(_("ИНН"), max_length=14, validators=[MinLengthValidator(14)])
    phone_number = models.CharField(_("Номер телефона: "), max_length=50)

    class Meta:
        verbose_name = "Контрагент"
        verbose_name_plural = "Контрагенты"
        db_table = "socks_factory_" + "counterparty"
    
    def __str__(self) -> str:
        return f"{self.name_counterparty}"


# Физ лицо
class Individuals(BaseModel):
    
    GENDER_LIST = [
        ('M', 'Мужчина'),
        ('W', 'Женщина'),
        ('O', 'Неизвестно'),
        ]   

    birthday = models.DateField(_("Дата рождения: "))
    gender = models.CharField(_("Пол: "), max_length=50, choices=GENDER_LIST)
    
    second_name_individuals = models.CharField(_("Фамилия:"), max_length=50)    
    first_name_individuals = models.CharField(_("Имя:"), max_length=50)  
    surname_individuals = models.CharField(_("Отчество:"), max_length=50)  
    full_name_individuals = models.CharField(_("Полное имя:"), max_length=100, blank=True)  
    
    inn_individuals = models.CharField(_("ИНН"), max_length=14, validators=[MinLengthValidator(14)], unique=True)
    phone_number = models.CharField(_("Номер телефона: "), max_length=50)
    biography = models.TextField(_("Биография: "), null=True, blank=True)
    
    class Meta:
        verbose_name = "Физ.лицо"
        verbose_name_plural = "Физ.лица"
        db_table = "socks_factory_" + "individuals"

    def __str__(self) -> str:
        return f"{self.first_name_individuals}.{self.surname_individuals[0:1]}"
    
    
# Подразделение
class Department(BaseModel):
    
    name_department = models.CharField(_("Подразделение:"), max_length=50)    

    
    class Meta:
        verbose_name = "Подразделение"
        verbose_name_plural = "Подразделения"
        db_table = "socks_factory_" + "department"

    def __str__(self) -> str:
        return f"{self.name_department}"
    

# Должность
class JobTitle(BaseModel):
    
    name_jobTitle = models.CharField(_("Должность:"), max_length=50)    

    
    class Meta:
        verbose_name = "Должность"
        verbose_name_plural = "Должности"
        db_table = "socks_factory_" + "jobTitle"

    def __str__(self) -> str:
        return f"{self.name_jobTitle}"
    

# Сотрудник
class Employes(BaseModel):
    
    date_of_employment = models.DateField(_("Дата приянятия на работу: "))
    
    individuals_fk = models.ForeignKey(Individuals, verbose_name=_("Физ.Лицо:"), on_delete=models.CASCADE)    
    department_fk = models.ForeignKey(Department, verbose_name=_("Подразделение:"), on_delete=models.CASCADE)    
    job_title_fk = models.ForeignKey(JobTitle, verbose_name=_("Должность:"), on_delete=models.CASCADE) 

    salary = models.IntegerField(_("Оклад (Зарплата): "))   
    
    class Meta:
        verbose_name = "Сотрудник"
        verbose_name_plural = "Сотрудники"
        db_table = "socks_factory_" + "employes"

    def __str__(self) -> str:
        return f"{self.individuals_fk} - {self.department_fk}"