from django import forms
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError
from .models import ContactMessage  # Asegúrate de importar tu modelo



class ContactForm(forms.ModelForm): # <--- Cambiado de forms.Form a forms.ModelForm
    
    class Meta:
        model = ContactMessage
        # Definimos los campos que el ModelForm debe manejar
        fields = ['name', 'email', 'message']
        
        # Mantenemos tus widgets personalizados aquí
        widgets = {
            'name': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': ("Tu nombre aquí..."),
            }),
            'email': forms.EmailInput(attrs={
                'class': 'form-control',
                'placeholder': 'ejemplo@correo.com',
            }),
            'message': forms.Textarea(attrs={
                'class': 'form-control',
                'rows': 5,
                'placeholder': ("¿En qué podemos ayudarte?"),
            }),
        }
        
        # Mantenemos tus etiquetas (labels)
        labels = {
            'name': ("Nombre completo"),
            'email': ("Correo electrónico"),
            'message': ("Comentario o mensaje"),
        }

    # Tu validación personalizada clean_message se queda EXACTAMENTE IGUAL
    def clean_message(self):
        data = self.cleaned_data.get('message')
        if data and len(data) < 10:
            raise forms.ValidationError(("El mensaje debe tener al menos 10 caracteres."))
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
