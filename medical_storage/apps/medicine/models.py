from django.db import models

from django.contrib.auth.models import User


class MedCode(models.Model):

    code = models.CharField(max_length=5, blank=False, null=False)
    is_active = models.BooleanField('Activo', default=True)
    reg_date = models.DateTimeField(auto_now_add=True, verbose_name='Fecha de Registro')
    user = models.ForeignKey(User, default='', on_delete=models.DO_NOTHING)

    def __str__(self):
        return code + ' - ' + self.user


class Lot(models.Model):

    lot = models.CharField(max_length=50, blank=False, null=False)
    is_active = models.BooleanField('Activo', default=True)
    reg_date = models.DateTimeField(auto_now_add=True, verbose_name='Fecha de Registro')
    user = models.ForeignKey(User, on_delete=models.DO_NOTHING)

    def __str__(self):
        return self.lot + ' - ' + '{}'.format(self.reg_date)
      

class Laboratory(models.Model):

    name = models.CharField('Laboratorio', max_length=100, null=False, blank=False)
    is_active = models.BooleanField('Activo', default=True)
    reg_date = models.DateTimeField(auto_now_add=True, verbose_name='Fecha de Registro')
    user = models.ForeignKey(User, on_delete=models.DO_NOTHING)

    def __str__(self):
        return self.name.capitalize()


class Active(models.Model):

    active = models.CharField('Activo', max_length=300, null=False, blank=True)
    grs = models.CharField(max_length=25, null=True, verbose_name='Gramage')
    is_active = models.BooleanField('Activo', default=True)
    reg_date = models.DateTimeField(auto_now_add=True, verbose_name='Fecha de Registro')
    user = models.ForeignKey(User, on_delete=models.DO_NOTHING)

    def __str__(self):
        return self.active + ' - ' + self.grs


class MedType(models.Model):

    type = models.CharField(max_length=50, blank=False, null=False)
    is_active = models.BooleanField('Activo', default=True)
    reg_date = models.DateTimeField(auto_now_add=True, verbose_name='Fecha de Registro')
    user = models.ForeignKey(User, on_delete=models.DO_NOTHING)

    def __str__(self):
        return self.type


class Medicine(models.Model):

    code = models.ForeignKey(MedCode, verbose_name='Codigo único', on_delete=models.DO_NOTHING)
    name = models.CharField('Nombre', max_length=100, null=True, blank=True)
    laboratory = models.ForeignKey(Laboratory, verbose_name='Laboratorio', on_delete=models.DO_NOTHING, blank=True, null=True)
    active = models.ManyToManyField(Active, verbose_name='Activo')
    med_type = models.ForeignKey(MedType, on_delete=models.DO_NOTHING, verbose_name='Tipo', null=True)
    total_qty = models.CharField('Cantidad total de pzas', max_length=1000, null=True, blank=True)
    med_function = models.TextField('Función', max_length=100, null=True, blank=True)
    indications = models.TextField('Indicaciones', max_length=100, null=True, blank=True)
    contraindications = models.TextField('Contraindicaciones', max_length=100, null=True, blank=True)
    lot = models.ForeignKey(Lot, blank=True, null=True, verbose_name='Lote', on_delete=models.DO_NOTHING)
    cad = models.DateField('Caducidad')
    med_qty = models.CharField(max_length=1000, blank=True, null=True, verbose_name='Unidades disponibles por caja')
    is_active = models.BooleanField('Activo', default=True)
    reg_date = models.DateTimeField(auto_now_add=True, verbose_name='Fecha de Registro')
    user = models.ForeignKey(User, on_delete=models.DO_NOTHING)

    def __str__(self):
        return '{}'.format(self.name) + '  -  ' + '{}'.format(self.active)


class Article(models.Model):

    name = models.CharField(max_length=100, blank=False, null=False, verbose_name='Nombre')
    description = models.TextField(max_length=2000, null=False, verbose_name='Descripciòn')
    qty = models.CharField(max_length=1000, blank=False, null=False, verbose_name='Cantidad')
    is_active = models.BooleanField('Activo', default=True)
    reg_date = models.DateTimeField(auto_now_add=True, verbose_name='Fecha de registro')
    user = models.ForeignKey(User, on_delete=models.DO_NOTHING)

    def __str__(self):
        return self.name + '  -  ' + '{}'.format(self.reg_date)
