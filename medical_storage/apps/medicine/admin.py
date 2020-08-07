from django.contrib import admin
"""
from medical_storage.apps.medicine.models import MedCode, Lot, Laboratory, Active, Article, MedType

admin.site.register(MedCode)
admin.site.register(Lot)
admin.site.register(Laboratory)
admin.site.register(Active)
admin.site.register(MedType)


@admin.register(Medicine)
class MedicineAdmin(admin.ModelAdmin):
    
    list_display = (
        'name',
        'laboratory',
        'med_type',
        'med_function',
        'indications',
        'contraindications',
        'cad',
        'reg_date'
    )

    #exclude = ['user']


@admin.register(Article)
class ArticleAdmin(admin.ModelAdmin):

    list_display = (
        'name',
        'description',
        'qty'
    )
"""