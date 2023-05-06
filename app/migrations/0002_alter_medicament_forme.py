# Generated by Django 4.2 on 2023-05-01 22:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='medicament',
            name='forme',
            field=models.CharField(choices=[('comprimé', 'Comprimé'), ('capsule', 'Capsule'), ('sirop', 'Sirop'), ('suspension', 'Suspension'), ('gelule', 'Gélule'), ('patch', 'Patch'), ('suppositoire', 'Suppositoire'), ('inhalateur', 'Inhalateur'), ('autre', 'Autre')], max_length=255),
        ),
    ]