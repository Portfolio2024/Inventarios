from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('dashboard/', views.dashboard, name='dashboard'),
    path('productos/', views.productos, name='productos'),
    path('productos/eliminar/<id>/', views.eliminar_producto, name='eliminar_producto'),
    path('productos/editar/<id>/', views.editar_producto, name='editar_producto'),
    path('pedidos/', views.pedidos, name='pedidos'),
    path('clientes/', views.clientes, name='clientes'),
    path('logout_user', views.logout_user, name='logout'),
]


