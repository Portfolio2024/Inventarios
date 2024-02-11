from django.urls import path, reverse_lazy
from Usuarios import views
from django.conf import settings
from django.conf.urls.static import static
from .views import *
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('register/', views.register, name='register'),
    path('login/', views.login_user, name='login_user'),
    path('perfil', PaginaPerfil.as_view(), name='perfil'),
    path('editar_perfil', views.editar_perfil, name='editar_perfil'),
    path('update_password', auth_views.PasswordChangeView.as_view(), name='update_password'),
]
if settings.DEBUG:
    from django.conf.urls.static import static
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)