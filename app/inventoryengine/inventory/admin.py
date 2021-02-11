from django.contrib import admin
from .models import *
from import_export.admin import ImportExportModelAdmin

@admin.register(Workers, Room, Type, Admission, EquipmentWorker,Upload)
class TypeAdmin(ImportExportModelAdmin):
    pass



admin.site.site_header = "Учет оборудования и расходных материалов"


# Register your models here.
