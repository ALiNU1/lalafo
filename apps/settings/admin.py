from django.contrib import admin
from apps.settings.models import Setting, AboutUs

# Register your models here.
admin.site.register(Setting)
admin.site.register(AboutUs)