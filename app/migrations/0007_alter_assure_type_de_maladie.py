# Generated by Django 4.2 on 2023-05-02 00:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0006_assure'),
    ]

    operations = [
        migrations.AlterField(
            model_name='assure',
            name='type_de_maladie',
            field=models.CharField(blank=True, choices=[('c1', 'c1'), ('c2', 'c2'), ('c3', 'c3'), ('c4', 'c4'), ('c5', 'c5'), ('c6', 'c6'), ('c7', 'c7'), ('c8', 'c8'), ('c9', 'c9'), ('c10', 'c10'), ('c11', 'c11'), ('c12', 'c12'), ('c13', 'c13'), ('c14', 'c14'), ('c15', 'c15'), ('c16', 'c16'), ('c17', 'c17'), ('c18', 'c18'), ('c19', 'c19'), ('c20', 'c20'), ('c21', 'c21'), ('c22', 'c22'), ('c23', 'c23'), ('c24', 'c24'), ('c25', 'c25'), ('c26', 'c26'), ('c27', 'c27')], max_length=3, null=True),
        ),
    ]
