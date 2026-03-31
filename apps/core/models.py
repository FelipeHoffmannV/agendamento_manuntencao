from django.db import models
from django.conf import settings

# Create your models here.
class TiposServico(models.TextChoices):
     LIMPEZA = ('LI', 'Limpeza')
     MANUNTENCAO = ('MN', 'Manuntenção')
     FORMATACAO = ('FO', 'Formatcação')

class Dispositivo(models.Model):
    id_dispositivo = models.AutoField(primary_key=True, null=False)
    class TipoDispositivo(models.TextChoices):
        NOTEBOOK = ('NT', 'Notebook')
        DESKTOP = ('DK', 'Desktop')
    
    tipo_dispositivo = models.CharField(max_length=2, choices=TipoDispositivo.choices, default=TipoDispositivo.DESKTOP)
    nome_meu_dispositivo = models.CharField(max_length=200, blank=True)
    client = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.SET_NULL, blank=True, null=True)

class Servico(models.Model):
    id_servico = models.AutoField(primary_key=True)
    tipo_servico = models.CharField(max_length=2, choices=TiposServico.choices, default=TiposServico.FORMATACAO)
    data_servico = models.DateField()

    client = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.SET_NULL, blank=True, null=True)
    dispositivo = models.ForeignKey('Dispositivo', on_delete=models.SET_NULL, blank=True, null=True)
    
  