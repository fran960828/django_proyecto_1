

from django.db import models
from django.forms import CharField
from django.db.models import Q, CheckConstraint

#class Author(models.Model):
#    name = models.CharField(max_length=40) 
#    biography = models.TextField(null=True, blank=True) 
#
#    class Meta:
#        verbose_name = "Escritor"
#        verbose_name_plural = "Escritores"
#
#class Book(models.Model):
#    title = models.CharField(max_length=200)
#    isbn = models.CharField(max_length=30, unique=True)
#    release_date = models.DateField()
#    # Para SET_NULL es obligatorio null=True
#    author = models.ForeignKey(Author, on_delete=models.SET_NULL, null=True, blank=True)
#
#    class Meta:
#        ordering = ["-release_date"]



#class Suscripcion(models.Model): # Heredamos de Model
#    # Uso de TextChoices (Forma moderna y limpia)
#    class TipoMedalla(models.TextChoices):
#        GOLD = 'GOLD', 'Gold'
#        SILVER = 'SILVER', 'Silver'
#        BRONZE = 'BRONZE', 'Bronze'
#
#    tipo = models.CharField(
#        max_length=10, 
#        choices=TipoMedalla.choices, 
#        default=TipoMedalla.BRONZE
#    )
#    precio = models.IntegerField(default=0)
#    activo = models.BooleanField(default=True)
#
#    class Meta:
#        constraints = [
#            CheckConstraint(
#                condition=Q(precio__gte=0),
#                name='precio_no_negativo'
#            )
#        ]
#
#    def __str__(self):
#        estado = "Activa" if self.activo else "Inactiva"
#        # Usamos .label para obtener el nombre legible del Choice
#        return f"Suscripción {self.get_tipo_display()} - {estado}"



class Student(models.Model):
    name = models.CharField('Nombre', max_length=30)
    def __str__(self): return self.name

class Course(models.Model):
    name = models.CharField('Curso', max_length=50)
    code = models.CharField('Código', max_length=10, unique=True, primary_key=True)
    students = models.ManyToManyField(Student, through='Register')
    def __str__(self): return self.name

class Register(models.Model):
    # Usamos CASCADE: si desaparece el alumno o el curso, desaparece la inscripción
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    
    # Captura la fecha automáticamente al crear
    date_inscription = models.DateField(auto_now_add=True)
    
    # DecimalField para precisión matemática
    calification = models.DecimalField(max_digits=4, decimal_places=2, null=True, blank=True)

    class Meta:
        constraints = [
            models.UniqueConstraint(
                fields=['student', 'course'], 
                name='unique_student_course_registration'
            )
        ]
    
#class Product(models.Model):
#    product_name=models.CharField('Producto',max_length=20)
#
#    def __str__(self):
#        return self.product_name
#class Store(models.Model):
#    store_name=models.CharField('Almacen',max_length=20)
#
#    def __str__(self):
#        return self.store_name
#    
#class Stock(models.Model):
#    product=models.ForeignKey(Product,on_delete=models.CASCADE)
#    store=models.ForeignKey(Store,on_delete=models.CASCADE)
#    quantity=models.IntegerField('Cantidad',default=0)
#
#    class Meta:
#        constraints=[
#            models.UniqueConstraint(
#                fields=['product','store'],
#                name='product-store'
#            ),
#            CheckConstraint(
#                condition=Q(quantity__gte=0),
#                name='cantidad no negativa'
#            )
#            
#        ]






