from django.db import router
from django.urls import path, include
from .views import * 
from rest_framework import routers

#crear las urls necesarios para el rest
router = routers.DefaultRouter()
router.register('guitarra', GuitarraViewset),
router.register('bajo', BajoViewset),
router.register('piano', PianoViewset),
router.register('percusion', PercusionViewset),
router.register('amplificador', AmplificadorViewset),
router.register('accesorio', AccesorioViewset)

urlpatterns = [
    path('', include(router.urls)),
    path('contacto', contacto, name="contacto"),
    path('api/', include(router.urls)),
    

]