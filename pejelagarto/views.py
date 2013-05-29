from django.http import HttpResponse
from models import Estudiante

def index(raton):
    Estudiante.objects.crear_estudiante(Estudiante())

    return HttpResponse('<html><body><b>hola mundo</b></body></html>')
