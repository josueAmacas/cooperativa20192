from django import forms
from apps.modelo.models import Cliente, Cuenta, Transaccion

class FormularioCliente(forms.ModelForm):
	class Meta:
		model = Cliente
		fields = ["cedula", "nombres", "apellidos", "genero", "estadoCivil", "fechaNacimiento", "correo","telefono", "celular", "direccion"]
		labels = {
			'cedula':'Cedula',
			'nombres':'Nombres',
			'apellidos':'Apellidos',
			'genero':'Genero',
			'estadoCivil':'Estado Civil',
			'fechaNacimiento':'Fecha de Nacimiento',
			'correo': 'Correo Electronico',
			'telefono':'Telefono',
			'celular':'Celular',
			'direccion':'Direccion',
		}
		widgets = {
			'cedula':forms.TextInput(attrs={'class':'input-group form-control','placeholder':'ej: 1XXXXXXXXX'}),
			'nombres':forms.TextInput(attrs={'class':'input-group form-control','placeholder':'Nombres'}),
			'apellidos':forms.TextInput(attrs={'class':'input-group form-control','placeholder':'Apellidos'}),
			'genero':forms.Select(attrs={'class':'input-group form-control','placeholder':'Genero'}),
			'estadoCivil':forms.Select(attrs={'class':'input-group form-control','placeholder':'Estado Civil'}),
			'fechaNacimiento':forms.DateInput(attrs={'class':'input-group form-control','placeholder':'AAAA-MM-DD'}),
			'correo': forms.TextInput(attrs={'class':'input-group form-control','placeholder':'ej: usuario@usuario.com'}),
			'telefono':forms.TextInput(attrs={'class':'input-group form-control','placeholder':'ej: 07XXXXXXX'}),
			'celular':forms.TextInput(attrs={'class':'input-group form-control','placeholder':'ej: 09XXXXXXXX'}),
			'direccion':forms.TextInput(attrs={'class':'input-group form-control','placeholder':'Direccion'}),
		}

class FormularioModificarCliente(forms.ModelForm):
	class Meta:
		model = Cliente
		fields = ["nombres", "apellidos", "genero", "estadoCivil", "fechaNacimiento", "correo","telefono", "celular", "direccion"]
		labels = {
			'nombres':'Nombres',
			'apellidos':'Apellidos',
			'genero':'Genero',
			'estadoCivil':'Estado Civil',
			'fechaNacimiento':'Fecha de Nacimiento',
			'correo': 'Correo Electronico',
			'telefono':'Telefono',
			'celular':'Celular',
			'direccion':'Direccion',
		}
		widgets = {
			'nombres':forms.TextInput(attrs={'class':'input-group form-control','placeholder':'Nombres'}),
			'apellidos':forms.TextInput(attrs={'class':'input-group form-control','placeholder':'Apellidos'}),
			'genero':forms.Select(attrs={'class':'input-group form-control'}),
			'estadoCivil':forms.Select(attrs={'class':'input-group form-control'}),
			'fechaNacimiento':forms.DateInput(attrs={'class':'input-group form-control','placeholder':'AAAA-MM-DD'}),
			'correo': forms.TextInput(attrs={'class':'input-group form-control','placeholder':'ej: usuario@usuario.com'}),
			'telefono':forms.TextInput(attrs={'class':'input-group form-control','placeholder':'ej: 07XXXXXXX'}),
			'celular':forms.TextInput(attrs={'class':'input-group form-control','placeholder':'ej: 09XXXXXXXX'}),
			'direccion':forms.TextInput(attrs={'class':'input-group form-control','placeholder':'Direccion'}),
		}

class FormularioCuenta(forms.ModelForm):
	class Meta:
		model = Cuenta
		fields = ["numero", "tipoCuenta", "saldo","cliente"]
		labels = {
			'numero':'Numero de Cuenta',
			'tipoCuenta':'Tipo de Cuenta',
			'saldo':'Saldo',
		}
		widgets = {
			'numero':forms.TextInput(attrs={'class':'input-group form-control'}),
			'tipoCuenta':forms.Select(attrs={'class':'input-group form-control'}),
			'saldo':forms.TextInput(attrs={'class':'input-group form-control','placeholder':'Saldo'}),
			'cliente':forms.Select(attrs={'class':'input-group form-control'}),
		}
		

class FormularioTransaccion(forms.ModelForm):
	class Meta:
		model = Transaccion
		fields = ["valor", "descripcion"]
		labels = {
			'valor':'Valor',
			'descripcion':'Descripcion',
		}
		widgets = {
			'valor':forms.TextInput(attrs={'class':'input-group form-control'}),
			'descripcion':forms.TextInput(attrs={'class':'input-group form-control'}),
		}
