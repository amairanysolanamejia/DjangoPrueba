from django.shortcuts import render
from django.utils import timezone
#importamos la línea anterior porque la usamos en la función inicio
from .models import Post   
# Esta última linea se agrega en el paso5
# El punto antes de models indica el directorio actual o 
# la aplicación actual. Ambos, views.py y models.py están en el mismo directorio. 
# Esto significa que podemos utilizar . y el nombre del archivo (sin .py). Ahora importamos el 
# nombre del modelo (Post).
from .models import Producto
#Hacemos lo mismo con producto, que es el nuevo creado
# Para tomar posts reales del modelo Post, necesitamos algo llamado QuerySet.   # 
from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse_lazy
from django.views import generic
# Create your views here.

def inicio(request):
	#Esto es para publicarlos por fecha
	posts = Post.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
	return render(request,'blog/index.html',{'posts': posts})

# hemos creado una función (def) llamada post_list 
# que acepta request y return una función render que reproduce (construye) nuestra plantilla 
# blog/post_list.html.
class SignUp(generic.CreateView):
    form_class = UserCreationForm
    success_url = reverse_lazy('login')
    template_name = 'signup.html'