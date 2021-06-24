from django.shortcuts import render
from .models import *
from .forms import ContactoForm
from rest_framework import viewsets
from .serializers import *
from rest_framework.views import APIView
from rest_framework.response import Response


#ayuda
#clases de serializer



class GuitarraViewset(viewsets.ModelViewSet):
    queryset = Guitarra.objects.all()
    serializer_class = GuitarraSerializer

class BajoViewset(viewsets.ModelViewSet):
    queryset = Bajo.objects.all()
    serializer_class = BajoSerializer

class PianoViewset(viewsets.ModelViewSet):
    queryset = Piano.objects.all()
    serializer_class = PianoSerializer

class PercusionViewset(viewsets.ModelViewSet):
    queryset = Percusion.objects.all()
    serializer_class = PercusionSerializer

class AmplificadorViewset(viewsets.ModelViewSet):
    queryset = Amplificador.objects.all()
    serializer_class = AmplificadorSerializer

class AccesorioViewset(viewsets.ModelViewSet):
    queryset = Accesorio.objects.all()
    serializer_class = AccesorioSerializer


class GuitaApiView(APIView):
    serializer_class=GuitaSerializer
    def get(self,request):
        queryset = Guitarra.objects.all().values()
        return Response({"Message":"Lista de Guitarra", "Lista Guitarra":queryset})

    def post(self,request):
        print('Request data is : ',request.data)
        serializer_obj=GuitaSerializer(data=request.data)
        if(serializer_obj.is_valid()):

            Guitarra.objects.create(id=serializer_obj.data.get("id"),
                            marca=serializer_obj.data.get("marca"),
                            tipo_cuerpo=serializer_obj.data.get("tipo_cuerpo"),
                            tipo_guitarra=serializer_obj.data.get("tipo_guitarra"),
                            valor=serializer_obj.data.get("valor"),
                            descripcion=serializer_obj.data.get("descripcion")
                            )

        guitarra=Guitarra.objects.all().filter(id=request.data["id"]).values()
        return Response({"Message":"Nueva Guitarra Agregada", "Guitarra":guitarra})

#fin serializer



def home(request):
    guitarra = Guitarra.objects.all()
    bajo = Bajo.objects.all()
    piano = Piano.objects.all()
    percusion = Percusion.objects.all()
    amplificador = Amplificador.objects.all()
    accesorios = Accesorio.objects.all()
    data = {
        'guitarra':guitarra,
        'bajo':bajo,
        'piano':piano,
        'percusion':percusion,
        'amplificador':amplificador,
        'accesorios':accesorios
    }
    return render(request, 'core/home.html', data)

def contacto(request):
    data = {
       'form': ContactoForm() 
    }

    if request.method == 'POST':
        formulario = ContactoForm(data=request.POST)
        if formulario.is_valid():
            formulario.save()
            data["mensaje"] = "mensaje enviado"
        else:
            data["form"] = formulario
            
    return render(request, 'core/contacto.html', data)

