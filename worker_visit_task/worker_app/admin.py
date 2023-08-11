from django.contrib import admin
from .models import *

class WorkerAdmin(admin.ModelAdmin):
    list_display = ('name', 'phone_number')
    search_fields = ('name',)


class UnitAdmin(admin.ModelAdmin):
    list_display = ('name', 'worker')
    search_fields = ('name',)


class VisitAdmin(admin.ModelAdmin):
    list_display = ('unit', 'latitude', 'longitude', 'visit_created')
    search_fields = ('unit__name', 'unit__worker__name')

admin.site.register(Worker, WorkerAdmin)
admin.site.register(Unit, UnitAdmin)
admin.site.register(Visit, VisitAdmin)