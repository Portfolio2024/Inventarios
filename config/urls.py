"""Inventarios URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include, reverse_lazy
from Usuarios import views as user_view
from Usuarios.views import *
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('dashboard.urls')),  
    path('user/', include('Usuarios.urls')),  
    path('register/', user_view.register, name='register'),
    path('login/', user_view.login_user, name='login_user'),    
    path('perfil', PaginaPerfil.as_view(), name='perfil'),
    path('editar_perfil', user_view.editar_perfil, name='editar_perfil'),
    #path('update_password', auth_views.PasswordChangeView.as_view(template_name='update_password.html'), name='update_password'),
    path('update_password', PasswordsChangeView.as_view(template_name='update_password.html'), name='update_password'),
    
]
if settings.DEBUG:
    from django.conf.urls.static import static
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)