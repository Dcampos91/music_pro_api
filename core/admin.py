from django.contrib import admin
from .models import Marca, Guitarra, Bajo, Piano, Percusion, Amplificador, Accesorio, Contacto

# Register your models here.
admin.site.register(Marca)
admin.site.register(Guitarra)
admin.site.register(Bajo)
admin.site.register(Piano)
admin.site.register(Percusion)
admin.site.register(Amplificador)
admin.site.register(Accesorio)
admin.site.register(Contacto)