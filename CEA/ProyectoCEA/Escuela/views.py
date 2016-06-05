from django.shortcuts import render, RequestContext, render_to_response

from .forms import *
from .models import *

from django.contrib.auth.models import User

# Create your views here.

def formTitulo(request):
	
	if request.method == 'POST':

		form = TituloForm(request.POST)

		if (form.is_valid()):
		
			obj = Titulo()

			obj.Nombre  = form['Nombre']

			obj.save()

			form = TituloForm()
			ctx = {
				"mensaje": "Guardado", "form": form
			}

	else:
		form = TituloForm()
		ctx = { "form": form }

	return render(request, "Escuela/formTitulo_view.html", ctx)

def formGradoMaximo(request):
	
	if request.method == 'POST':

		form = GradoMaximoForm(request.POST)

		if (form.is_valid()):
		
			obj = GradoMaximo()

			obj.Nombre  = form['Nombre']

			obj.save()

			form = GradoMaximoForm()
			ctx = {
				"mensaje": "Guardado", "form": form
			}

	else:
		form = GradoMaximoForm()
		ctx = { "form": form }

	return render(request, "Escuela/formGradoMaximo_view.html", ctx)

def formCarrera(request):
	
	if request.method == 'POST':

		form = CarreraForm(request.POST)

		if (form.is_valid()):
		
			obj = Carrera()

			obj.Nombre  = form['Nombre']

			obj.save()

			form = CarreraForm()
			ctx = {
				"mensaje": "Guardado", "form": form
			}

	else:
		form = CarreraForm()
		ctx = { "form": form }

	return render(request, "Escuela/formCarrera_view.html", ctx)

def formProfesor(request):
	
	if request.method == 'POST':

		form = ProfesorForm(request.POST)

		if (form.is_valid()):
		
			obj = Profesor()

			obj.Nombre  = form['Nombre']
			obj.ApellidoPaterno  = form['ApellidoPaterno']
			obj.ApellidoMaterno  = form['ApellidoMaterno']
			obj.FK_Titulo  = form['FK_Titulo']
			obj.FK_GradoMaximo  = form['FK_GradoMaximo']
			obj.TelefonoCelular  = form['TelefonoCelular']
			obj.TelefonoCasa  = form['TelefonoCasa']
			obj.Tutorias  = form['Tutorias']
			obj.NumeroEmpleado  = form['NumeroEmpleado']
			obj.FK_NumeroHoras  = form['FK_NumeroHoras']
			obj.Laboratorio  = form['Laboratorio']
			obj.Paquete  = form['Paquete']

			obj.save()

			form = ProfesorForm()
			ctx = {
				"mensaje": "Guardado", "form": form
			}

	else:
		form = ProfesorForm()
		ctx = { "form": form }

	return render(request, "Escuela/formProfesor_view.html", ctx)

def formMateria(request):
	
	if request.method == 'POST':

		form = MateriaForm(request.POST)

		if (form.is_valid()):
		
			obj = Materia()

			obj.Nombre  = form['Nombre']
			obj.Serie  = form['Serie']
			obj.HorasTeoricas  = form['HorasTeoricas']
			obj.HorasPracticas  = form['HorasPracticas']
			obj.Creditos  = form['Creditos']
			obj.FK_Carrera  = form['FK_Carrera']

			obj.save()

			form = MateriaForm()
			ctx = {
				"mensaje": "Guardado", "form": form
			}

	else:
		form = MateriaForm()
		ctx = { "form": form }

	return render(request, "Escuela/formMateria_view.html", ctx)

def formProfesorMateria(request):
	
	if request.method == 'POST':

		form = ProfesorMateriaForm(request.POST)

		if (form.is_valid()):
		
			obj = ProfesorMateria()

			obj.FK_Profesor  = form['FK_Profesor']
			obj.FK_Materia  = form['FK_Materia']

			obj.save()

			form = ProfesorMateriaForm()
			ctx = {
				"mensaje": "Guardado", "form": form
			}

	else:
		form = ProfesorMateriaForm()
		ctx = { "form": form }

	return render(request, "Escuela/formProfesorMateria_view.html", ctx)

def formProfesorHora(request):
	
	if request.method == 'POST':

		form = ProfesorHoraForm(request.POST)

		if (form.is_valid()):
		
			obj = ProfesorHora()

			obj.FK_Profesor  = form['FK_Profesor']
			obj.FK_Dia  = form['FK_Dia']
			obj.FK_Hora  = form['FK_Hora']

			obj.save()

			form = ProfesorHoraForm()
			ctx = {
				"mensaje": "Guardado", "form": form
			}

	else:
		form = ProfesorHoraForm()
		ctx = { "form": form }

	return render(request, "Escuela/formProfesorHora_view.html", ctx)