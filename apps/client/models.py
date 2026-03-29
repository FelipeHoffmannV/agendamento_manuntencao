from django.db import models
from django.contrib.auth.models import AbstractUser
from django.contrib.auth.hashers import check_password, make_password
# Create your models here.

class User(AbstractUser):
    pass

class Cidade(models.TextChoices):
    RIO_NEGRO = 'RN', 'Rio Negro (PR)'
    MAFRA = 'MF', 'Mafra (SC)'

class EnderecoClient(models.Model):
    id_endereco_client = models.AutoField(primary_key=True, null=False, unique=True)
    cep = models.CharField("CEP", max_length=9, blank=False)
    rua = models.CharField("Rua/Logradouro", max_length=200, blank=False)
    numero = models.CharField("Numero", max_length=10, blank=False)
    bairro = models.CharField("Bairro", max_length=200, blank=False, null=True)
    cidade = models.CharField(max_length=2, choices=Cidade.choices, default=Cidade.RIO_NEGRO)


class Client(User):
    
    email_client = models.EmailField(unique=True)
    tel_client = models.CharField(max_length=14, unique=True)
    endereco = models.OneToOneField(EnderecoClient, on_delete=models.SET_NULL, null=True)



    def __str__(self):
        return self.get_full_name() or self.username



    