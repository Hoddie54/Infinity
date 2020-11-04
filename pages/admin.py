from django.contrib import admin
from .models import Application, Notes, AutoAddApplication



class ApplicationAdmin(admin.ModelAdmin):
    fields = ['user', 'priority', 'industry', 'company', 'open_date', 'close_date', 'stage', 'notes']


admin.site.register(Application, ApplicationAdmin)
admin.site.register(Notes)
admin.site.register(AutoAddApplication)
