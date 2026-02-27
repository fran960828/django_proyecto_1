from todos.models import Director, Serie, Capitulo
from datetime import date

def run():
    # Limpiar datos previos
    Capitulo.objects.all().delete()
    Serie.objects.all().delete()
    Director.objects.all().delete()

    # 1. Crear Directores
    nolan = Director.objects.create(nombre="Christopher Nolan", nacionalidad="Británico")
    scorsese = Director.objects.create(nombre="Martin Scorsese", nacionalidad="Estadounidense")
    v_gilligan = Director.objects.create(nombre="Vince Gilligan", nacionalidad="Estadounidense")

    # 2. Crear Series
    bb = Serie.objects.create(titulo="Breaking Bad", fecha_estreno=date(2008, 1, 20), precio_suscripcion=19.99, director=v_gilligan, categoria="Drama")
    bcsaul = Serie.objects.create(titulo="Better Call Saul", fecha_estreno=date(2015, 2, 8), precio_suscripcion=14.50, director=v_gilligan, categoria="Drama")
    dark = Serie.objects.create(titulo="Dark", fecha_estreno=date(2017, 12, 1), precio_suscripcion=9.99, director=nolan, categoria="Sci-Fi")
    interstellar = Serie.objects.create(titulo="Interstellar (Mini)", fecha_estreno=date(2014, 11, 7), precio_suscripcion=25.00, director=nolan, categoria="Sci-Fi")

    # 3. Crear Capítulos
    Capitulo.objects.create(titulo="Pilot", duracion_minutos=58, serie=bb)
    Capitulo.objects.create(titulo="Felina", duracion_minutos=55, serie=bb)
    Capitulo.objects.create(titulo="Uno", duracion_minutos=53, serie=bcsaul)
    Capitulo.objects.create(titulo="Secrets", duracion_minutos=45, serie=dark)
    Capitulo.objects.create(titulo="The Ghost", duracion_minutos=50, serie=interstellar)

    print("✅ Base de datos poblada con éxito.")


run()