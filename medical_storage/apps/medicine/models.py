from django.db import models

from django.contrib.auth.models import User


class Name(models.Model):

    name = models.CharField('Nombre', max_length=100, null=False, blank=False)

    def __str__(self):
        return self.name.capitalize()


class Active(models.Model):

    active = models.CharField('Activo', max_length=300, null=False, blank=False)

    def __str__(self):
        return self.active


class Medicine(models.Model):

    PHILL = 'Pastilla'
    SOLUTION = 'Solucion'
    INJECTION = 'Inyeccion'
    POWDERED = 'En Polvo'

    MED_TYPE = [
        ('phill', PHILL),
        ('solution', SOLUTION),
        ('injection', INJECTION),
        ('powdered', POWDERED),
    ]

    name = models.ForeignKey(Name, verbose_name='Nombre', on_delete=models.DO_NOTHING, null=True)
    laboratory = models.CharField('Laboratorio', max_length=100, null=False, blank=False)
    active = models.ManyToManyField(Active, verbose_name='Activo')
    formule = models.TextField('Formula', max_length=100, null=False, blank=False)
    med_type = models.CharField('Tipo de medicamento', max_length=50, choices=MED_TYPE, default=PHILL)
    total_qty = models.CharField('Cantidad total de pzas', max_length=1000, null=True, blank=True)
    disp_qty = models.CharField('Cantidad Disponible', max_length=1000, null=False, blank=False)
    function = models.TextField('Función', max_length=100, null=False, blank=False)
    indications = models.TextField('Indicaciones', max_length=100, null=True)
    contraindications = models.TextField('Contraindicaciones', max_length=100, null=True, blank=True)
    cad = models.DateField('Caducidad')
    is_active = models.BooleanField('Activo', default=True)
    reg_date = models.DateTimeField(auto_now_add=True)
    user = models.ForeignKey(User, on_delete=models.DO_NOTHING)

    def __str__(self):
        return self.name + '  -  ' + self.function