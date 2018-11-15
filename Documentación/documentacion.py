"""
Las sigientes funciones corresponden al proyecto 3 de web, una tienda funcional en Django, la cual fue realizada en Django 2.0
Las anotaciones son fundamentales para el entendimiento del proyecto
"""

def inicio(request):
	"""
	Función que permite abrir el index , la página inifical del sitio  web en Django2.0
	Para esto se realiza en la carpeta apps/frutas/ views.py
	Se requiere del import : from django.shortcuts import render,redirect
	"""
	return render(request,'frutas/index.html')


def registrate(request):
	"""
	Función que permite al usuario registrarse, Se ubuca en login/views.py
	Requiere de:
	from django.shortcuts import render,redirect
	from django.contrib.auth.forms import UserCreationForm
	from django.contrib.auth import authenticate,login,logout
	from django.contrib.auth.decorators import login_required
	from .forms import UserCreateForm

	"""
	if request.method == 'POST':
		form = UserCreateForm(request.POST)
		if form.is_valid():
			form.save()
			username = form.cleaned_data['username']
			password = form.cleaned_data['password1']
			user = authenticate(username=username,password=password)
			login(request,user)
			return redirect('inicio')

	else:
		form = UserCreateForm()
	return render(request,'registration/registrate.html',{'form':form})
