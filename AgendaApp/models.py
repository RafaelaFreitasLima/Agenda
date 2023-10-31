sfrom django.db import models

# Create your models here.

class Contato(models.Model):
    nome = models.CharField(max_length=100)
    apelido = models.CharField(max_length=30, blank=True, null=True)
    email = models.EmailField(max_length=100)
    data_nascimento = models.DateField(verbose_name= 'Data de Nascimento')
    endereco = models.CharField(max_length=200, verbose_name= 'Endereço')
    numero = models.CharField(max_length=10)
    complemento = models.CharField(max_length=50, blank=True, null=True)
    cep = models.CharField(max_length=9)
    bairro = models.CharField(max_length=100)
    cidade = models.CharField(max_length=100)
    estado = models.CharField(max_length=50)
    estado_civil = models.CharField(max_length=1, choices=ESTADO_CIVIS, null=True)

def __str__(self):
    return self.nome

#Configuração do modelo
class Meta:
    verbose_name = 'Pessoas'
    verbose_name_plural = 'Pessoa'
