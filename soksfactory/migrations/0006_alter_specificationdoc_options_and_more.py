# Generated by Django 4.1.7 on 2023-08-03 07:59

from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        (
            "soksfactory",
            "0005_categorynomenclature_characteristicdoc_nomenclature_and_more",
        ),
    ]

    operations = [
        migrations.AlterModelOptions(
            name="specificationdoc",
            options={
                "verbose_name": "Спецификация",
                "verbose_name_plural": "Спецификация",
            },
        ),
        migrations.AlterModelOptions(
            name="specificationitem",
            options={
                "verbose_name": "Спецификация элемент",
                "verbose_name_plural": "Спецификация элемент",
            },
        ),
    ]
