from django.contrib import admin

from .models import Paciente

from .models import Procedimento

admin.site.register(Paciente)
admin.site.register(Procedimento)