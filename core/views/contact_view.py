from dotenv import load_dotenv
import os
from django.views.generic import CreateView
from django.urls import reverse_lazy
from django.contrib import messages
from django.core.mail import send_mail
from django.conf import settings
from core.forms import ContactForm
from core.models import ContactMessage

load_dotenv()
class ContactCreateView(CreateView):
    model = ContactMessage
    form_class = ContactForm
    template_name = 'core/contact.html'
    success_url = reverse_lazy('core:contact')

    def form_valid(self, form):
        # 1. Guardamos el objeto en la DB (esto ya crea el registro)
        # self.object = form.save()  <-- CreateView hace esto internamente al llamar a super()
        response = super().form_valid(form)
        
        # 2. Lógica de envío de email
        try:
            send_mail(
                'Prueba de envio de correo',
                form.cleaned_data['message'],
                settings.EMAIL_HOST_USER,
                [os.getenv('EMAIL_PRUEBA')],
                fail_silently=False,
            )
            messages.success(self.request, "¡Gracias! Tu mensaje ha sido enviado y guardado correctamente.")
        except Exception:
            # Si el email falla, el registro ya se guardó en la DB por el super().form_valid()
            messages.warning(self.request, "El mensaje se guardó en nuestra base de datos, pero hubo un error al enviar el correo.")
        
        return response

    def form_invalid(self, form):
        messages.error(self.request, "Por favor, corrige los errores en el formulario.")
        return super().form_invalid(form)