from django import forms
from django.utils.translation import gettext_lazy as _
from django.core.validators import EmailValidator
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError

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




class RegisterForm(forms.Form):
    username = forms.CharField(
        label="Nombre de usuario",
        widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Ej: jdoe'})
    )
    email = forms.EmailField(
        label="Correo electrónico",
        widget=forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'email@ejemplo.com'})
    )
    password = forms.CharField(
        label="Contraseña",
        widget=forms.PasswordInput(attrs={'class': 'form-control'})
    )
    password_confirm = forms.CharField(
        label="Confirma tu contraseña",
        widget=forms.PasswordInput(attrs={'class': 'form-control'})
    )

    # Validación 1: ¿El usuario ya existe?
    def clean_username(self):
        username = self.cleaned_data.get('username')
        if User.objects.filter(username=username).exists():
            raise ValidationError("Este nombre de usuario ya está registrado.")
        return username

    # Validación 2: ¿Las contraseñas coinciden?
    def clean(self):
        cleaned_data = super().clean()
        password = cleaned_data.get("password")
        password_confirm = cleaned_data.get("password_confirm")

        if password and password_confirm and password != password_confirm:
            raise ValidationError("Las contraseñas no coinciden.")
        return cleaned_data
