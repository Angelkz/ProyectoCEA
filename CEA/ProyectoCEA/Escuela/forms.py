from django import forms
from .models import *
from django.forms import ModelForm

class UsuarioForm(forms.Form):
	Username = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control','style':'width: 15em;',"placeholder":'Username','id':'idUsername'}))
	Password = forms.CharField(widget=forms.PasswordInput(attrs={'class':'form-control','style':'width: 15em;',"placeholder":'Password','id':'idPassword'}))

class TituloForm(forms.ModelForm):
	class Meta:
			model = Titulo
			fields = '__all__'

class GradoMaximoForm(forms.ModelForm):
	class Meta:
			model = GradoMaximo
			fields = '__all__'

class NumeroHorasForm(forms.ModelForm):
	class Meta:
			model = NumeroHoras
			fields = '__all__'

class CarreraForm(forms.ModelForm):
	class Meta:
			model = Carrera
			fields = '__all__'

class DiaForm(forms.ModelForm):
	class Meta:
			model = Dia
			fields = '__all__'

class HoraForm(forms.ModelForm):
	class Meta:
			model = Hora
			fields = '__all__'

class ProfesorForm(forms.ModelForm):
	class Meta:
			model = Profesor
			fields = '__all__'

class MateriaForm(forms.ModelForm):
	class Meta:
			model = Materia
			fields = '__all__'


class ProfesorMateriaForm(forms.ModelForm):
	class Meta:
			model = ProfesorMateria
			fields = '__all__'

class ProfesorHoraForm(forms.ModelForm):
	class Meta:
			model = ProfesorHora
			fields = '__all__'

# class UsuBuildNom(forms.Form):
# 	Build= forms.ModelChoiceField(queryset=UsuBuild.objects.all()) 
# 	Build_Oponente= forms.ModelChoiceField(queryset=UsuBuild.objects.all())
# 	Niveles 	= (
# 		(1,1), (2,2), (3,3), (4,4), (5,5), (6,6), (7,7), (8,8), (9,9), (10,10), (11,11), (12,12), (13,13), (14,14), (15,15), (16,16), (17,17), (18,18)
# 			  )
# 	Nivel	=	forms.ChoiceField(choices = Niveles)
# 	Nivel_Oponente	=	forms.ChoiceField(choices = Niveles)

# 	class Meta:
# 	    model = UsuBuild
# 	    fields = '__all__'