from django import forms
from django.utils.translation import gettext_lazy as _
from django.core.validators import EmailValidator

class ContactForm(forms.Form):
    """
    Formulario de contacto con validación integrada y estilos CSS.
    """
    
    name = forms.CharField(
        label=_("Nombre completo"),
        max_length=100,
        widget=forms.TextInput(attrs={
            'class': 'form-control',
            'placeholder': _("Tu nombre aquí..."),
        })
    )

    email = forms.EmailField(
        label=_("Correo electrónico"),
        validators=[EmailValidator(message=_("Introduce un email válido."))],
        widget=forms.EmailInput(attrs={
            'class': 'form-control',
            'placeholder': 'ejemplo@correo.com',
        })
    )

    message = forms.CharField(
        label=_("Comentario o mensaje"),
        widget=forms.Textarea(attrs={
            'class': 'form-control',
            'rows': 5,
            'placeholder': _("¿En qué podemos ayudarte?"),
        })
    )

    def clean_message(self):
        """Validación personalizada: Evita mensajes demasiado cortos."""
        data = self.cleaned_data.get('message')
        if len(data) < 10:
            raise forms.ValidationError(_("El mensaje debe tener al menos 10 caracteres."))
        return data

