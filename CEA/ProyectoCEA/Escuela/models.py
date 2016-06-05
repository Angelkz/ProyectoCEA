from django.db import models
from Horario.models import *
from django.contrib.auth.models import User

# Create your models here.

class PerfilUsuario(models.Model):
	Usuario = models.OneToOneField(User, related_name = 'profile')
	FecAct = models.DateTimeField(auto_now_add=True)

	def __unicode__(self):
		return self.Usuario.username

class Titulo(models.Model):
	Nombre = models.CharField(max_length = 48)
	FecAct = models.DateTimeField(auto_now_add=True)

	def __unicode__(self):
		return  self.Nombre

class GradoMaximo(models.Model):
	Nombre = models.CharField(max_length = 48)
	FecAct = models.DateTimeField(auto_now_add=True)

	def __unicode__(self):
		return  self.Nombre

class NumeroHoras(models.Model):
	Nombre = models.CharField(max_length = 48)
	FecAct = models.DateTimeField(auto_now_add=True)

	def __unicode__(self):
		return  self.Nombre

# NumeroHorasChoises = (
#     ('Tiempo Completo: 22 horas (+/- 2)', 'Tiempo Completo: 22 horas (+/- 2)'),
#     ('1/2 Tiempo: 12 horas (+/- 2) ', '1/2 Tiempo: 12 horas (+/- 2)'),
#     ('3/4 Tiempo: 16 horas (+/- 2)', '3/4 Tiempo: 16 horas (+/- 2)'),
#     ('Asignatura: 19 horas max', 'Asignatura: 19 horas max'),
# )

class Carrera(models.Model):
	Nombre = models.CharField(max_length = 48)
	FecAct = models.DateTimeField(auto_now_add=True)

	def __unicode__(self):
		return  self.Nombre

class Dia(models.Model):
	Nombre = models.CharField(max_length = 48)
	FecAct = models.DateTimeField(auto_now_add=True)

	def __unicode__(self):
		return  self.Nombre

class Hora(models.Model):
	Nombre = models.CharField(max_length = 48)
	FecAct = models.DateTimeField(auto_now_add=True)

	def __unicode__(self):
		return  self.Nombre

class Profesor(models.Model):
	Nombre = models.CharField(max_length = 48)
	ApellidoPaterno = models.CharField(max_length = 48)
	ApellidoMaterno = models.CharField(max_length = 48)
	FK_Titulo = models.ForeignKey('Titulo')
	FK_GradoMaximo = models.ForeignKey('GradoMaximo')
	TelefonoCelular = models.IntegerField()
	TelefonoCasa = models.IntegerField()
	Email = models.EmailField()
	Tutorias = models.BooleanField()
	NumeroEmpleado = models.CharField(max_length = 48, null=True, blank=True)
	FK_NumeroHoras = models.ForeignKey('NumeroHoras', null=True, blank=True)
	Laboratorio = models.BooleanField()
	Paquete = models.CharField(max_length = 200)
	FecAct = models.DateTimeField(auto_now_add=True)

	def __unicode__(self):
		return  self.Nombre

class Materia(models.Model):
	Nombre = models.CharField(max_length = 48)
	Serie = models.CharField(max_length = 48)
	HorasTeoricas = models.IntegerField()
	HorasPracticas = models.IntegerField()
	Creditos = models.IntegerField()
	FK_Carrera = models.ForeignKey('Carrera')
	FecAct = models.DateTimeField(auto_now_add=True)

	def __unicode__(self):
		return  self.Nombre

class ProfesorMateria(models.Model):
	FK_Profesor = models.ForeignKey('Profesor')
	FK_Materia = models.ForeignKey('Materia')
	FecAct = models.DateTimeField(auto_now_add=True)

	def __unicode__(self):
		return  self.FK_Materia.Nombre

class ProfesorHora(models.Model):
	FK_Profesor = models.ForeignKey('Profesor')
	FK_Dia = models.ForeignKey('Dia')
	FK_Hora = models.ForeignKey('Hora')
	FecAct = models.DateTimeField(auto_now_add=True)
	
	def __unicode__(self):
		return u'%s %s' % (self.FK_Dia.Nombre, self.FK_Hora.Nombre)