from django.db import models
from django.contrib.auth.models import BaseUserManager,AbstractBaseUser, PermissionsMixin

# Create your models here.

class UserManager(BaseUserManager):

    def create_user(self, username, email=None, password=None, **extrafields):
        if not username:
            raise ValueError('Se debe tener un nombre de usuario')
        user = self.model(username=username, email=email, **extrafields)
        user.set_password(password)
        user.save(using=self._db)
        
        return user

   

class User(AbstractBaseUser, PermissionsMixin):
    nombre = models.CharField(max_length=30)
    apellidoP = models.CharField(max_length=20)
    apellidoM = models.CharField(max_length=20)
    email = models.CharField(max_length=50)
    username = models.CharField(max_length=20, unique=True)
    fechaDeNacimiento = models.DateField
    password = models.CharField(max_length=20)
    telefono = models.IntegerField()
    tipoCuenta = models.BooleanField(default=False)
    direccion = models.CharField(max_length=50)

    objects = UserManager()

    USERNAME_FIELD = 'username'