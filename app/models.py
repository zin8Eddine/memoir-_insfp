from django.db import models
from django import forms


# -------------------- Medicament Table -----------------------------------

class Medicament(models.Model):
    FORME_CHOICES = [
        ('comprimé', 'Comprimé'),
        ('capsule', 'Capsule'),
        ('sirop', 'Sirop'),
        ('suspension', 'Suspension'),
        ('gelule', 'Gélule'),
        ('patch', 'Patch'),
        ('suppositoire', 'Suppositoire'),
        ('inhalateur', 'Inhalateur'),
        ('autre', 'Autre'),
    ]

    code = models.CharField(max_length=20, primary_key=True)
    nom = models.CharField(max_length=255,)
    forme = models.CharField(max_length=255, choices=FORME_CHOICES)
    dosage = models.DecimalField(max_digits=10, decimal_places=2)
    prix_public = models.DecimalField(max_digits=10, decimal_places=2)
    remboursable = models.BooleanField()
    tarif_reference = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return self.code


class MedicamentForm(forms.ModelForm):
    class Meta:
        model = Medicament
        fields = ['code', 'nom', 'forme', 'dosage',
                  'prix_public', 'remboursable', 'tarif_reference']

# -------------------- Assure Table-----------------------------------


class Assure(models.Model):
    MATRICULE_MAX_LENGTH = 20
    NOM_MAX_LENGTH = 50
    PRENOM_MAX_LENGTH = 50
    LIEU_DE_NAISSANCE_MAX_LENGTH = 100

    TYPE_DE_MALADIE_CHOICES = [(f'c{i}', f'c{i}') for i in range(1, 28)]

    matricule = models.CharField(max_length=MATRICULE_MAX_LENGTH, primary_key=True)
    nom = models.CharField(max_length=NOM_MAX_LENGTH)
    prenom = models.CharField(max_length=PRENOM_MAX_LENGTH)
    date_de_naissance = models.DateField()
    lieu_de_naissance = models.CharField(
        max_length=LIEU_DE_NAISSANCE_MAX_LENGTH)
    type_de_maladie = models.CharField(
        max_length=3, choices=TYPE_DE_MALADIE_CHOICES, blank=True, null=True)

    def __str__(self):
        return self.matricule
