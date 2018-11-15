from django.shortcuts import render,redirect

# Create your views here.

def inicio(request):
	return render(request,'frutas/index.html')
