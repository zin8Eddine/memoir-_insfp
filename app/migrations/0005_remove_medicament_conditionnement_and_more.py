# Generated by Django 4.2 on 2023-05-01 23:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0004_remove_conditionnement_field'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='medicament',
            name='conditionnement',
        ),
        migrations.AlterField(
            model_name='medicament',
            name='dosage',
            field=models.DecimalField(decimal_places=2, max_digits=10),
        ),
    ]
