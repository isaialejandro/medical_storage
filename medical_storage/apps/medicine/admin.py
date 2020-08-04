from django.contrib import admin

from medical_storage.apps.medicine.models import Name, Active, Medicine


admin.site.register(Active)
admin.site.register(Name)

@admin.register(Medicine)
class MedicineAdmin(admin.ModelAdmin):

    list_display = (
        'name',
        'laboratory',
        #'active',
        'med_type',
        'total_qty',
        'disp_qty',
        'function',
        'indications',
        'contraindications',
        'cad'
    )

    exclude = (
        'reg_date',
        #'user'
    )
