from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from .forms import FormularioCliente, FormularioCuenta, FormularioModificarCliente, FormularioTransaccion
from apps.modelo.models import Cliente, Cuenta, Transaccion

@login_required
def principal(request):
	lista = Cliente.objects.all().order_by('apellidos')
	context ={
		'lista': lista,
	}
	return render (request, 'cliente/principal_cliente.html', context)

@login_required
def crear(request):
	formulario = FormularioCliente(request.POST)
	formularioCuenta = FormularioCuenta(request.POST)
	usuario = request.user #peticion que es procesada por el framework agrega el usuario
	if usuario.groups.filter(name= 'administrativo').exists():
		if request.method == 'POST':
			if formulario.is_valid() and formularioCuenta.is_valid():
				datos = formulario.cleaned_data #obteniendo todos los datos del formulario del Cliente
				cliente = Cliente()
				cliente.cedula = datos.get('cedula')
				cliente.nombres = datos.get('nombres')
				cliente.apellidos = datos.get('apellidos')
				cliente.genero = datos.get('genero')
				cliente.estadoCivil = datos.get('estadoCivil')
				cliente.fechaNacimiento = datos.get('fechaNacimiento')
				cliente.correo= datos.get('correo')
				cliente.telefono = datos.get('telefono')
				cliente.celular = datos.get('celular')
				cliente.direccion = datos.get('direccion')
				cliente.save()

				datosCuenta = formularioCuenta.cleaned_data #obteniendo todos los datos del formulario de la Cuenta
				cuenta = Cuenta()
				cuenta.numero = datosCuenta.get('numero')
				cuenta.estado = True
				cuenta.fechaApertura = datosCuenta.get('fechaApertura')
				cuenta.tipoCuenta = datosCuenta.get('tipoCuenta')
				cuenta.saldo = datosCuenta.get('saldo')
				cuenta.cliente = cliente
				cuenta.save();

				return redirect(principal)
	else:
		return render(request, 'cliente/acceso_prohibido.html')
	context = {
		'f': formulario,
		'fc': formularioCuenta,

	}
	return render (request, 'cliente/crear_cliente.html',context)

@login_required
def modificar(request):
	dni = request.GET['cedula']
	cliente = Cliente.objects.get(cedula = dni)
	if request.method == 'POST':
		#se modifica
		formulario = FormularioModificarCliente(request.POST)
		if formulario.is_valid():
			datos = formulario.cleaned_data #obteniendo todos los datos del formulario del Cliente
			cliente.nombres = datos.get('nombres')
			cliente.apellidos = datos.get('apellidos')
			cliente.genero = datos.get('genero')
			cliente.estadoCivil = datos.get('estadoCivil')
			cliente.fechaNacimiento = datos.get('fechaNacimiento')
			cliente.correo= datos.get('correo')
			cliente.telefono = datos.get('telefono')
			cliente.celular = datos.get('celular')
			cliente.direccion = datos.get('direccion')
			cliente.save()
			return redirect(principal)
	else:
		formulario = FormularioModificarCliente(instance = cliente)

	context = {
		'dni': dni,
		'cliente': cliente,
		'formulario': formulario
	}

	return render (request, 'cliente/modificar_cliente.html', context)

@login_required
def listarCuentas(request):
	dni = request.GET.get('cedula')
	cliente = Cliente.objects.get(cedula = dni)
	cuentas = Cuenta.objects.filter(cliente_id = cliente.cliente_id)

	context ={
		'cliente': cliente,
		'lista': cuentas,
	}
	return render(request, 'cliente/principal_cuenta.html', context)

@login_required
def crearCuenta(request):
	formularioCuenta = FormularioCuenta(request.POST)
	usuario = request.user #peticion que es procesada por el framework agrega el usuario
	print(usuario)
	if usuario.groups.filter(name= 'administrativo').exists():
		if request.method == 'POST':
			if formularioCuenta.is_valid():				
				datosCuenta = formularioCuenta.cleaned_data #obteniendo todos los datos del formulario de la Cuenta
				cuenta = Cuenta()
				cuenta.numero = datosCuenta.get('numero')
				cuenta.estado = True
				cuenta.fechaApertura = datosCuenta.get('fechaApertura')
				cuenta.tipoCuenta = datosCuenta.get('tipoCuenta')
				cuenta.saldo = datosCuenta.get('saldo')
				cuenta.cliente = datosCuenta.get('cliente')
				cuenta.save();

				return redirect(principal)
			else:
				print("Error en el formulario")
		else:
			print("Error en el methodo")
	else:
		return render(request, 'cliente/acceso_prohibido.html')
	context = {
		'fc': formularioCuenta,
	}

	return render (request, 'cliente/crear_cuenta.html',context)

@login_required
def depositar(request, numero):
	usuario = request.user
	cuenta = Cuenta.objects.get(numero = numero)
	cliente = Cliente.objects.get(cliente_id = cuenta.cliente_id)
	formulario = FormularioTransaccion(request.POST)
	if  request.method =='POST':
		if formulario.is_valid():
			datos = formulario.cleaned_data
			cuenta.saldo = cuenta.saldo + datos.get('valor')
			cuenta.save()

			transaccion = Transaccion()
			transaccion.tipo = 'deposito';
			transaccion.valor = datos.get('valor')			
			transaccion.descripcion = datos.get('descripcion')
			transaccion.responsable = usuario
			transaccion.cuenta = cuenta
			transaccion.save()
			deposito = float (datos.get('valor'))
			mensaje = 'Transaccion exitosa'
			return render(request, 'transaccion/estado.html', locals())			

	context ={
		'cliente': cliente,
		'cuenta': cuenta,
		'formulario': formulario,
	}
	return render(request, 'transaccion/depositar.html', context)

@login_required
def retirar(request, numero):
	usuario = request.user
	cuenta = Cuenta.objects.get(numero = numero)
	cliente = Cliente.objects.get(cliente_id = cuenta.cliente_id)
	formulario = FormularioTransaccion(request.POST)
	if  request.method =='POST':
		if formulario.is_valid():
			datos = formulario.cleaned_data
			cuenta.saldo = cuenta.saldo - datos.get('valor')
			cuenta.save()

			transaccion = Transaccion()
			transaccion.tipo = 'retiro';
			transaccion.valor = datos.get('valor')			
			transaccion.descripcion = datos.get('descripcion')
			transaccion.responsable = usuario
			transaccion.cuenta = cuenta
			transaccion.save()
			deposito = float (datos.get('valor'))
			mensaje = 'Transaccion exitosa'
			return render(request, 'transaccion/estado.html', locals())			

	context ={
		'cliente': cliente,
		'cuenta': cuenta,
		'formulario': formulario,
	}

	return render(request, 'transaccion/retirar.html', context)
