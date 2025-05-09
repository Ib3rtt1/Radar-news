from django.shortcuts import render
from .models import Noticia


def lista_noticias(request):
    noticias = Noticia.objects.all()  # Traemos todas las noticias
    return render(request, 'noticias/lista_noticias.html', {'noticias': noticias})
