from django.db import models

# Create your models here.
class TodoItem(models.Model):
  content = models.TextField()

class Veiculo(models.Model): 
  marca = models.TextField()
  modelo = models.TextField()
  ano = models.IntegerField()
  placa = models.TextField()
  foto_carro = models.ImageField()
  
#CRIAR CLASS FRETEIRO - VER SE VAMOS CADASTRAR OU NAO

class Frete(models.Model):
  data = models.DateField()
  avaliacao = models.TextField() #VER COM O PROFESSOR

class Cliente(models.Model):
  nome = models.TextField()
  telefone = models.TextField()
  cpf = models.TextField()

class Depoimento(models.Model):
  texto = models.TextField()
  avaliacao = models.TextField() 
  #VER COM O PROFESSOR
  
class Carga(models.Model):
 descricao = models.TextField()
 dimensao = models.TextField()
 peso = models.TextField()    


class Endereco(models.Model):
  logradouro = models.TextField()
  numero = models.IntegerField()
  cep = models.TextField()
  

class Estado(models.Model):
  sigla = models.TextField()
  #VER COM O PROFESSOR
  nome = models.TextField()

class Cidade(models.Model):
  nome = models.TextField()

class Bairro(models.Model):
  nome = models.TextField()

class Duvida(models.Model):
  pergunta = models.TextField()
  resposta = models.TextField()









