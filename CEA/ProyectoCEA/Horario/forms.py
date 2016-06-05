from django import forms
from .models import *
from django.forms import ModelForm

class PeriodoForm(forms.ModelForm):
	class Meta:
			model = Periodo
			fields ='__all__'

class SemestreForm(forms.ModelForm):
	class Meta:
			model = Semestre
			fields = '__all__'

class SalonForm(forms.ModelForm):
	class Meta:
			model = Salon
			fields = '__all__'

class HorarioCarreraForm(forms.ModelForm):
	class Meta:
			model = HorarioCarrera
			fields = '__all__'

class ClaseHoraForm(forms.ModelForm):
	class Meta:
			model = ClaseHora
			fields = '__all__'

class HorarioFiltroForm(forms.Form):
	Horario= forms.ModelChoiceField(queryset=HorarioCarrera.objects.all()) 

	class Meta:
	    model = HorarioCarrera
	    fields = '__all__'