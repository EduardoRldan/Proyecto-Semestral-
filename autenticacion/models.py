from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class Producto (models.Model):
    nombre = models.CharField(max_length=255)
    descripcion = models.TextField()
    precio = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return self.nombre
    
class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='autenticacion_userprofile')
    full_name = models.CharField(max_length=100)
    birth_date = models.DateField(null=True, blank=True)
    address = models.TextField(blank=True)

    def __str__(self):
        return self.user.username
    
class UserActivity(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    activity_type = models.CharField(max_length=100)
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.user.username}-{self.activity_type}"
    
class UserSettings (models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    receive_email_notifications = models.BooleanField(default=True)
    preferred_language = models.CharField(max_length=20, default='en')

    def __str__(self):
        return self.user.username