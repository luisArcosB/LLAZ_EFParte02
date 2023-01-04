from django.shortcuts import render

from LLAZ_MIAPP.models import Docente

from LLAZ_MIAPP.forms import DocenteForm


# Create your views here.

def ruta_integrantes(request):

    return render (request, "integrantes.html")


def ruta_inicio (request):

    return render (request, "inicio.html")


def saludo(request):

    
    return render (request, "saludo.html")


def crear_docente(request):

    data={

        'form': DocenteForm()

    }

    if request.method=='POST':

        formulario=DocenteForm(data=request.POST)

        if formulario.is_valid():

            formulario.save()

            data["mensaje"]="Docente agregado exitosamente"

        else:

            data["form"]=formulario

    return render(request,'crear_docente.html',data)
def crear_curso(request):

    
    return render (request, "crear_curso.html")
def listar_curso(request):

    
    return render (request, "listar_curso.html")
def listar_docente(request):

    
    return render (request, "listar_docente.html")
