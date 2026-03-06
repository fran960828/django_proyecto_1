from django import forms

class SearchForm(forms.Form):
    # Definimos el campo y sus reglas
    search = forms.CharField(label="Buscar", max_length=100, required=False)

    