from django import forms

class FormularioLogin(forms.Form):
	username = forms.CharField(widget = forms.TextInput(attrs={'class':'input-group form-control','placeholder':'Usuario'}),
								label='Usuario')
	password = forms.CharField(widget = forms.PasswordInput(attrs={'class':'input-group form-control','placeholder':'Clave'}),
								label='Clave')
