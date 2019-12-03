from django.urls import path
from . import views

urlpatterns = [
    path('', views.principal, name= 'cliente'),
    path('crear_cliente/', views.crear),
    path('modificar_cliente/', views.modificar),
    path('principal_cuenta/', views.listarCuentas),
    path(r'^deposito/(?P<numero>d+)/$', views.depositar, name='deposito'),
    path(r'^retiro/(?P<numero>d+)/$', views.retirar, name='retiro'),
    path('nueva_cuenta/', views.crearCuenta, name='nuevaCuenta'),

]