from django.views.generic import TemplateView

class AboutUsView(TemplateView):
    template_name = "core/about_us.html" # Solo definimos la ruta del template