from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.shortcuts import render
from .forms import FormularioLogin

def ingresar(request):
	formulario = FormularioLogin(request.POST)
	if request.method == 'POST':		
		if formulario.is_valid():
			usuario = request.POST.get('username')
			clave = request.POST.get('password')
			user = authenticate(username = usuario, password = clave)
			if user is not None:
				if user.is_active:
					login(request, user)
					return HttpResponseRedirect(reverse('cliente'))
				else:
					print('usuario desactivado')
			else:
				print('usuario y/o contrasena incorrecto')
	else:
		formulario = FormularioLogin()
	context = {
		'formulario': formulario
	}
	return render (request, 'login/login.html', context)

def cerrar(request):
	logout(request)
	return HttpResponseRedirect(reverse('cerrarSesion'))