from django.shortcuts import render
from django.contrib.auth import login,logout
from django.contrib.auth.forms import AuthenticationForm
from django.shortcuts import render, redirect

def login_view(request):
    # Pasamos 'request' como primer argumento porque AuthenticationForm 
    # lo necesita para algunas comprobaciones de seguridad de sesión.
    form = AuthenticationForm(request, data=request.POST or None)

    if request.method == 'POST':
        if form.is_valid():
            # El formulario ya verificó que el usuario y contraseña son correctos
            usuario_validado = form.get_user()
            
            # Iniciamos la sesión
            login(request, usuario_validado)
            
            return redirect('/')

    # Si hay errores (contraseña mal, usuario inexistente), 
    # se mostrarán automáticamente en el HTML gracias a form.as_p
    return render(request, 'core/login.html', {'form': form})

def logout_view(request):
    logout(request)
    return redirect('/')