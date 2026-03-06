import os
from dotenv import load_dotenv
from config import settings
from core.forms import ContactForm
from django.shortcuts import render, redirect
from django.contrib import messages
from core.forms import ContactForm
from core.models import ContactMessage
from django.core.mail import send_mail

load_dotenv()
def contact_view(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            # Lógica de procesamiento (ej. enviar email) aquí
            ContactMessage.objects.create(
                name=form.cleaned_data['name'],
                email=form.cleaned_data['email'],
                message=form.cleaned_data['message']
            )
            try:

                send_mail(
                    'Prueba de envio de correo',        # 1. Subject (Asunto)
                    form.cleaned_data['message'],      # 2. Message (Texto plano)
                    settings.EMAIL_HOST_USER,     # 3. From Email (De quién viene)
                    [os.getenv('EMAIL_PRUEBA')],     # 4. Recipient List (Lista de destinos)
                    fail_silently=False,       # 5. Error handling (¿Explota si falla?)
                    )
                messages.success(request, "¡Gracias! Tu mensaje ha sido enviado y guardado correctamente.")
                return redirect('core:contact')

            except Exception as e:
                # Si el correo falla por red/configuración, avisamos al admin pero el dato ya está en la DB
                messages.warning(request, "El mensaje se guardó en nuestra base de datos, pero hubo un error al enviar la notificación por correo.")
                return redirect('core:contact')
        else:
            # OPCIONAL: Mensaje de error si la validación falla
            messages.error(request, "Por favor, corrige los errores en el formulario.")
    else:
        form = ContactForm()

    # El render final sirve tanto para el GET inicial 
    # como para cuando el POST falla (y así muestra los errores)
    return render(request, 'core/contact.html', {'form': form})



