
from django.shortcuts import render, redirect
from django.urls import reverse
from django.contrib.auth.models import User
from core.forms import RegisterForm
from django.contrib import messages # Para enviar alertas de éxito

def register_view(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            # Extraemos los datos validados
            data = form.cleaned_data
            
            # Creamos el usuario profesionalmente
            User.objects.create_user(
                username=data['username'],
                email=data['email'],
                password=data['password']
            )
            
            messages.success(request, "¡Cuenta creada con éxito! Ya puedes iniciar sesión.")
            return redirect(reverse('core:login'))
    else:
        form = RegisterForm()
    
    return render(request, 'core/register.html', {'form': form})