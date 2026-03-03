from todos.models import Serie,Director,Capitulo
from django.db.models import Q
from django.db.models import Avg, Count, Max
#Ejercicio 1
dramas=Serie.objects.filter(categoria='Drama', precio_suscripcion__gt=15)
#Ejercicio 2
try:
    director = Director.objects.get(nacionalidad='Británico')
except Director.DoesNotExist:
    print("No hay directores británicos")
except Director.MultipleObjectsReturned:
    print("Hay más de un director británico, usa filter()")
#Ejercicio 3
antiguas=Serie.objects.all().order_by('fecha_estreno')[:2]
# Ejercicio 4
capitulos=Capitulo.objects.filter(
    serie__director__nombre='Vince Gilligan'
)
# Ejercicio 5
series=Serie.objects.filter(
    Q(titulo__icontains='Saul')|Q(precio_suscripcion__lt=10)
)
# Ejercicio 6
sciFi=Serie.objects.exclude(
    categoria__icontains='Sci-Fi'
).order_by('-titulo')

# Ejercicio 7
promedio=Serie.objects.aggregate(precio_medio=Avg('precio_suscripcion'))

# Ejercicio 8
dirigidas=Director.objects.annotate(num_series=Count('series'))

# Ejercicio 9
serie = Serie.objects.order_by('-capitulos__duracion_minutos').first()
