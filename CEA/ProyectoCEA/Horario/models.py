from django.db import models
from Escuela.models import *

# Create your models here.

class Periodo(models.Model):
	Nombre = models.CharField(max_length = 48)
	FecAct = models.DateTimeField(auto_now_add=True)

	def __unicode__(self):
		return  self.Nombre

class Semestre(models.Model):
	Nombre = models.CharField(max_length = 48)
	FecAct = models.DateTimeField(auto_now_add=True)

	def __unicode__(self):
		return  self.Nombre

class Salon(models.Model):
	Nombre = models.CharField(max_length = 48)
	FecAct = models.DateTimeField(auto_now_add=True)

	def __unicode__(self):
		return  self.Nombre

class HorarioCarrera(models.Model):
	Clave = models.CharField(max_length = 48)
	FK_Periodo = models.ForeignKey('Periodo')
	FK_Semestre = models.ForeignKey('Semestre')
	FK_Carrera = models.ForeignKey('Escuela.Carrera')
	FecAct = models.DateTimeField(auto_now_add=True)

	def __unicode__(self):
		return self.Clave #	identificamos por clave?

class ClaseHora(models.Model):
	FK_HorarioCarrera = models.ForeignKey('HorarioCarrera')
	FK_Dia = models.ForeignKey('Escuela.Dia')
	FK_Hora = models.ForeignKey('Escuela.Hora')
	FK_Salon = models.ForeignKey('Salon')
	FK_Profesor = models.ForeignKey('Escuela.Profesor')
	FK_Materia = models.ForeignKey('Escuela.Materia')
	FecAct = models.DateTimeField(auto_now_add=True)

	def __unicode__(self):
		return u'%s %s %s %s %s' % (self.FK_Dia.Nombre, self.FK_Hora.Nombre, self.FK_Salon.Nombre, self.FK_Profesor.Nombre, self.FK_Materia.Nombre)