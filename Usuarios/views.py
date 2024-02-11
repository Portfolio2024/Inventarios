from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm, PasswordChangeForm
from django.contrib.auth import login
from django.views.generic.base import TemplateView
from django.views.generic import UpdateView, FormView
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required
from .models import *
from django.contrib import messages
from .forms import CreateUserForm, UserUpdateForm, ProfileUpdateForm
from django.contrib.auth.models import User
from django.urls import reverse_lazy
from django.contrib.auth.views import PasswordChangeView
from django.contrib.auth import update_session_auth_hash

class PasswordsChangeView(PasswordChangeView):
    title = "Editar password"
    form_class = PasswordChangeForm
    success_url = reverse_lazy('perfil')

def register(request):
    title = "Registro de Usuarios"
    if request.method == 'POST':
        form = CreateUserForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
    else:
        form = CreateUserForm()
    context = {
        'form': form,
        'title': title
    }
    return render(request, 'register.html', context)

def login_user(request):
    title = "Inicio de sesión"
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('index')
    else:
        form = AuthenticationForm()
    context = {
        'form': form,
        'title': title
    }
    return render(request, 'login.html', context)


# PAGINA PERFIL
class PaginaPerfil(TemplateView):
    title = "Perfil de usuario"
    template_name = 'perfil.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = self.title
        user = self.request.user
        return context
    
    
    
def editar_perfil(request):
    title = "Editar perfil"
    if request.method == 'POST':
        user_form = UserUpdateForm(request.POST, instance=request.user)
        perfil_form = ProfileUpdateForm(request.POST, request.FILES, instance=request.user.profile)

    # Verfica que los formularios sean validos
        if user_form.is_valid() and perfil_form.is_valid():
            # Guarda los datos en la base de datos
            user_form.save()
            perfil_form.save()
            return redirect('perfil')     
    else:
        user_form = UserUpdateForm(instance=request.user)
        perfil_form = ProfileUpdateForm(instance=request.user.profile)                
        context = {
                'title': title,
                'user_form': user_form,
                'perfil_form': perfil_form
            }
    return render(request, 'update_perfil.html', context)


    
    
