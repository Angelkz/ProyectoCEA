from django.shortcuts import render

from .forms import *
from .models import *
from Escuela.forms import *
from Escuela.models import *

def formPeriodo(request):
	
	if request.method == 'POST':

		form = PeriodoForm(request.POST)

		if (form.is_valid()):
		
			obj = Periodo()

			obj.Nombre  = form['Nombre']

			obj.save()

			form = PeriodoForm()
			ctx = {
				"mensaje": "Guardado", "form": form
			}

	else:
		form = PeriodoForm()
		ctx = { "form": form }

	return render(request, "Horario/formPeriodo_view.html", ctx)

def formSalon(request):
	
	if request.method == 'POST':

		form = SalonForm(request.POST)

		if (form.is_valid()):
		
			obj = Salon()

			obj.Nombre  = form['Nombre']

			obj.save()

			form = SalonForm()
			ctx = {
				"mensaje": "Guardado", "form": form
			}

	else:
		form = SalonForm()
		ctx = { "form": form }

	return render(request, "Horario/formSalon_view.html", ctx)

def formHorarioCarrera(request):
	
	if request.method == 'POST':

		form = HorarioCarreraForm(request.POST)

		if (form.is_valid()):
		
			obj = HorarioCarrera()

			obj.Clave  = form['Clave']
			obj.FK_Semestre  = form['FK_Semestre']
			obj.FK_Periodo  = form['FK_Periodo']
			obj.FK_Carrera  = form['FK_Carrera']

			filtro = HorarioCarrera.objects.filter(Clave=obj.Clave)
			
			if filtro:
				form = HorarioCarreraForm()
        		ctx = {
        		"mensaje": "Clave de horario existente, ingresar otro", "form": form
        		}
        	else:
        		obj.save()
        		form = HorarioCarreraForm()
        		ctx = {
				"mensaje": "Guardado", "form": form
				}
	else:
		form = HorarioCarreraForm()
		ctx = { "form": form }

	return render(request, "Horario/formHorarioCarrera_view.html", ctx)

def formClaseHora(request):
	
	if request.method == 'POST':

		form = ClaseHoraForm(request.POST)

		if (form.is_valid()):
		
			obj = ClaseHora()

			obj.FK_HorarioCarrera  = form['FK_HorarioCarrera']
			obj.FK_Hora  = form['FK_Hora']
			obj.FK_Dia = form['FK_Dia']
			obj.FK_Salon = form['FK_Salon']
			obj.FK_Profesor  = form['FK_Profesor']
			obj.FK_Materia  = form['FK_Materia']

			filtro1 = ClaseHora.objects.filter(FK_HorarioCarrera = obj.HorarioCarrera).filter(FK_Hora = obj.Hora).filter(FK_Dia = obj.Dia)
			filtro2 = ClaseHora.objects.filter(FK_Profesor = obj.FK_Profesor).filter(FK_Hora = obj.Hora).filter(FK_Dia = obj.Dia)
			filtro3 = ClaseHora.objects.filter(FK_Salon = obj.Salon).filter(FK_Hora = obj.Hora).filter(FK_Dia = obj.Dia)
			
			if filtro1:
				form = HorarioCarreraForm()
				
				mensaje = "Clase existente en el mismo horario."
				

			elif filtro2:
				form = HorarioCarreraForm()
				mensaje = "Profesor no disponible en ese horario."

			elif filtro3:
				form = HorarioCarreraForm()
				mensaje = "Salon ocupado en ese horario."
			else:
				obj.save()
				form = ClaseHoraForm()
				mensaje = "Guardado"

			l78 = ClaseHora.objects.filter(FK_HorarioCarrera = obj.HorarioCarrera).filter(Hora = "7-8").filter(Dia = "Lunes")
			l89 = ClaseHora.objects.filter(FK_HorarioCarrera = obj.HorarioCarrera).filter(Hora = "8-9").filter(Dia = "Lunes")
			l910 = ClaseHora.objects.filter(FK_HorarioCarrera = obj.HorarioCarrera).filter(Hora = "9-10").filter(Dia = "Lunes")
			l1011 = ClaseHora.objects.filter(FK_HorarioCarrera = obj.HorarioCarrera).filter(Hora = "10-11").filter(Dia = "Lunes")
			l1112 = ClaseHora.objects.filter(FK_HorarioCarrera = obj.HorarioCarrera).filter(Hora = "11-12").filter(Dia = "Lunes")
			l1213 = ClaseHora.objects.filter(FK_HorarioCarrera = obj.HorarioCarrera).filter(Hora = "12-13").filter(Dia = "Lunes")
			l1314 = ClaseHora.objects.filter(FK_HorarioCarrera = obj.HorarioCarrera).filter(Hora = "13-14").filter(Dia = "Lunes")
			l1415 = ClaseHora.objects.filter(FK_HorarioCarrera = obj.HorarioCarrera).filter(Hora = "14-15").filter(Dia = "Lunes")
			l1516 = ClaseHora.objects.filter(FK_HorarioCarrera = obj.HorarioCarrera).filter(Hora = "15-16").filter(Dia = "Lunes")
			l1617 = ClaseHora.objects.filter(FK_HorarioCarrera = obj.HorarioCarrera).filter(Hora = "16-17").filter(Dia = "Lunes")
			l1718 = ClaseHora.objects.filter(FK_HorarioCarrera = obj.HorarioCarrera).filter(Hora = "17-18").filter(Dia = "Lunes")
			l1819 = ClaseHora.objects.filter(FK_HorarioCarrera = obj.HorarioCarrera).filter(Hora = "18-19").filter(Dia = "Lunes")
			l1920 = ClaseHora.objects.filter(FK_HorarioCarrera = obj.HorarioCarrera).filter(Hora = "19-20").filter(Dia = "Lunes")
			l2021 = ClaseHora.objects.filter(FK_HorarioCarrera = obj.HorarioCarrera).filter(Hora = "20-21").filter(Dia = "Lunes")
			l2122 = ClaseHora.objects.filter(FK_HorarioCarrera = obj.HorarioCarrera).filter(Hora = "21-22").filter(Dia = "Lunes")
			b78 = ClaseHora.objects.filter(FK_HorarioCarrera = obj.HorarioCarrera).filter(Hora = "7-8").filter(Dia = "Martes")
			b89 = ClaseHora.objects.filter(FK_HorarioCarrera = obj.HorarioCarrera).filter(Hora = "8-9").filter(Dia = "Martes")
			b910 = ClaseHora.objects.filter(FK_HorarioCarrera = obj.HorarioCarrera).filter(Hora = "9-10").filter(Dia = "Martes")
			b1011 = ClaseHora.objects.filter(FK_HorarioCarrera = obj.HorarioCarrera).filter(Hora = "10-11").filter(Dia = "Martes")
			b1112 = ClaseHora.objects.filter(FK_HorarioCarrera = obj.HorarioCarrera).filter(Hora = "11-12").filter(Dia = "Martes")
			b1213 = ClaseHora.objects.filter(FK_HorarioCarrera = obj.HorarioCarrera).filter(Hora = "12-13").filter(Dia = "Martes")
			b1314 = ClaseHora.objects.filter(FK_HorarioCarrera = obj.HorarioCarrera).filter(Hora = "13-14").filter(Dia = "Martes")
			b1415 = ClaseHora.objects.filter(FK_HorarioCarrera = obj.HorarioCarrera).filter(Hora = "14-15").filter(Dia = "Martes")
			b1516 = ClaseHora.objects.filter(FK_HorarioCarrera = obj.HorarioCarrera).filter(Hora = "15-16").filter(Dia = "Martes")
			b1617 = ClaseHora.objects.filter(FK_HorarioCarrera = obj.HorarioCarrera).filter(Hora = "16-17").filter(Dia = "Martes")
			b1718 = ClaseHora.objects.filter(FK_HorarioCarrera = obj.HorarioCarrera).filter(Hora = "17-18").filter(Dia = "Martes")
			b1819 = ClaseHora.objects.filter(FK_HorarioCarrera = obj.HorarioCarrera).filter(Hora = "18-19").filter(Dia = "Martes")
			b1920 = ClaseHora.objects.filter(FK_HorarioCarrera = obj.HorarioCarrera).filter(Hora = "19-20").filter(Dia = "Martes")
			b2021 = ClaseHora.objects.filter(FK_HorarioCarrera = obj.HorarioCarrera).filter(Hora = "20-21").filter(Dia = "Martes")
			b2122 = ClaseHora.objects.filter(FK_HorarioCarrera = obj.HorarioCarrera).filter(Hora = "21-22").filter(Dia = "Martes")
			c78 = ClaseHora.objects.filter(FK_HorarioCarrera = obj.HorarioCarrera).filter(Hora = "7-8").filter(Dia = "Miercoles")
			c89 = ClaseHora.objects.filter(FK_HorarioCarrera = obj.HorarioCarrera).filter(Hora = "8-9").filter(Dia = "Miercoles")
			c910 = ClaseHora.objects.filter(FK_HorarioCarrera = obj.HorarioCarrera).filter(Hora = "9-10").filter(Dia = "Miercoles")
			c1011 = ClaseHora.objects.filter(FK_HorarioCarrera = obj.HorarioCarrera).filter(Hora = "10-11").filter(Dia = "Miercoles")
			c1112 = ClaseHora.objects.filter(FK_HorarioCarrera = obj.HorarioCarrera).filter(Hora = "11-12").filter(Dia = "Miercoles")
			c1213 = ClaseHora.objects.filter(FK_HorarioCarrera = obj.HorarioCarrera).filter(Hora = "12-13").filter(Dia = "Miercoles")
			c1314 = ClaseHora.objects.filter(FK_HorarioCarrera = obj.HorarioCarrera).filter(Hora = "13-14").filter(Dia = "Miercoles")
			c1415 = ClaseHora.objects.filter(FK_HorarioCarrera = obj.HorarioCarrera).filter(Hora = "14-15").filter(Dia = "Miercoles")
			c1516 = ClaseHora.objects.filter(FK_HorarioCarrera = obj.HorarioCarrera).filter(Hora = "15-16").filter(Dia = "Miercoles")
			c1617 = ClaseHora.objects.filter(FK_HorarioCarrera = obj.HorarioCarrera).filter(Hora = "16-17").filter(Dia = "Miercoles")
			c1718 = ClaseHora.objects.filter(FK_HorarioCarrera = obj.HorarioCarrera).filter(Hora = "17-18").filter(Dia = "Miercoles")
			c1819 = ClaseHora.objects.filter(FK_HorarioCarrera = obj.HorarioCarrera).filter(Hora = "18-19").filter(Dia = "Miercoles")
			c1920 = ClaseHora.objects.filter(FK_HorarioCarrera = obj.HorarioCarrera).filter(Hora = "19-20").filter(Dia = "Miercoles")
			c2021 = ClaseHora.objects.filter(FK_HorarioCarrera = obj.HorarioCarrera).filter(Hora = "20-21").filter(Dia = "Miercoles")
			c2122 = ClaseHora.objects.filter(FK_HorarioCarrera = obj.HorarioCarrera).filter(Hora = "21-22").filter(Dia = "Miercoles")
			d78 = ClaseHora.objects.filter(FK_HorarioCarrera = obj.HorarioCarrera).filter(Hora = "7-8").filter(Dia = "Jueves")
			d89 = ClaseHora.objects.filter(FK_HorarioCarrera = obj.HorarioCarrera).filter(Hora = "8-9").filter(Dia = "Jueves")
			d910 = ClaseHora.objects.filter(FK_HorarioCarrera = obj.HorarioCarrera).filter(Hora = "9-10").filter(Dia = "Jueves")
			d1011 = ClaseHora.objects.filter(FK_HorarioCarrera = obj.HorarioCarrera).filter(Hora = "10-11").filter(Dia = "Jueves")
			d1112 = ClaseHora.objects.filter(FK_HorarioCarrera = obj.HorarioCarrera).filter(Hora = "11-12").filter(Dia = "Jueves")
			d1213 = ClaseHora.objects.filter(FK_HorarioCarrera = obj.HorarioCarrera).filter(Hora = "12-13").filter(Dia = "Jueves")
			d1314 = ClaseHora.objects.filter(FK_HorarioCarrera = obj.HorarioCarrera).filter(Hora = "13-14").filter(Dia = "Jueves")
			d1415 = ClaseHora.objects.filter(FK_HorarioCarrera = obj.HorarioCarrera).filter(Hora = "14-15").filter(Dia = "Jueves")
			d1516 = ClaseHora.objects.filter(FK_HorarioCarrera = obj.HorarioCarrera).filter(Hora = "15-16").filter(Dia = "Jueves")
			d1617 = ClaseHora.objects.filter(FK_HorarioCarrera = obj.HorarioCarrera).filter(Hora = "16-17").filter(Dia = "Jueves")
			d1718 = ClaseHora.objects.filter(FK_HorarioCarrera = obj.HorarioCarrera).filter(Hora = "17-18").filter(Dia = "Jueves")
			d1819 = ClaseHora.objects.filter(FK_HorarioCarrera = obj.HorarioCarrera).filter(Hora = "18-19").filter(Dia = "Jueves")
			d1920 = ClaseHora.objects.filter(FK_HorarioCarrera = obj.HorarioCarrera).filter(Hora = "19-20").filter(Dia = "Jueves")
			d2021 = ClaseHora.objects.filter(FK_HorarioCarrera = obj.HorarioCarrera).filter(Hora = "20-21").filter(Dia = "Jueves")
			d2122 = ClaseHora.objects.filter(FK_HorarioCarrera = obj.HorarioCarrera).filter(Hora = "21-22").filter(Dia = "Jueves")
			e78 = ClaseHora.objects.filter(FK_HorarioCarrera = obj.HorarioCarrera).filter(Hora = "7-8").filter(Dia = "Viernes")
			e89 = ClaseHora.objects.filter(FK_HorarioCarrera = obj.HorarioCarrera).filter(Hora = "8-9").filter(Dia = "Viernes")
			e910 = ClaseHora.objects.filter(FK_HorarioCarrera = obj.HorarioCarrera).filter(Hora = "9-10").filter(Dia = "Viernes")
			e1011 = ClaseHora.objects.filter(FK_HorarioCarrera = obj.HorarioCarrera).filter(Hora = "10-11").filter(Dia = "Viernes")
			e1112 = ClaseHora.objects.filter(FK_HorarioCarrera = obj.HorarioCarrera).filter(Hora = "11-12").filter(Dia = "Viernes")
			e1213 = ClaseHora.objects.filter(FK_HorarioCarrera = obj.HorarioCarrera).filter(Hora = "12-13").filter(Dia = "Viernes")
			e1314 = ClaseHora.objects.filter(FK_HorarioCarrera = obj.HorarioCarrera).filter(Hora = "13-14").filter(Dia = "Viernes")
			e1415 = ClaseHora.objects.filter(FK_HorarioCarrera = obj.HorarioCarrera).filter(Hora = "14-15").filter(Dia = "Viernes")
			e1516 = ClaseHora.objects.filter(FK_HorarioCarrera = obj.HorarioCarrera).filter(Hora = "15-16").filter(Dia = "Viernes")
			e1617 = ClaseHora.objects.filter(FK_HorarioCarrera = obj.HorarioCarrera).filter(Hora = "16-17").filter(Dia = "Viernes")
			e1718 = ClaseHora.objects.filter(FK_HorarioCarrera = obj.HorarioCarrera).filter(Hora = "17-18").filter(Dia = "Viernes")
			e1819 = ClaseHora.objects.filter(FK_HorarioCarrera = obj.HorarioCarrera).filter(Hora = "18-19").filter(Dia = "Viernes")
			e1920 = ClaseHora.objects.filter(FK_HorarioCarrera = obj.HorarioCarrera).filter(Hora = "19-20").filter(Dia = "Viernes")
			e2021 = ClaseHora.objects.filter(FK_HorarioCarrera = obj.HorarioCarrera).filter(Hora = "20-21").filter(Dia = "Viernes")
			e2122 = ClaseHora.objects.filter(FK_HorarioCarrera = obj.HorarioCarrera).filter(Hora = "21-22").filter(Dia = "Viernes")
			f78 = ClaseHora.objects.filter(FK_HorarioCarrera = obj.HorarioCarrera).filter(Hora = "7-8").filter(Dia = "Sabado")
			f89 = ClaseHora.objects.filter(FK_HorarioCarrera = obj.HorarioCarrera).filter(Hora = "8-9").filter(Dia = "Sabado")
			f910 = ClaseHora.objects.filter(FK_HorarioCarrera = obj.HorarioCarrera).filter(Hora = "9-10").filter(Dia = "Sabado")
			f1011 = ClaseHora.objects.filter(FK_HorarioCarrera = obj.HorarioCarrera).filter(Hora = "10-11").filter(Dia = "Sabado")
			f1112 = ClaseHora.objects.filter(FK_HorarioCarrera = obj.HorarioCarrera).filter(Hora = "11-12").filter(Dia = "Sabado")
			f1213 = ClaseHora.objects.filter(FK_HorarioCarrera = obj.HorarioCarrera).filter(Hora = "12-13").filter(Dia = "Sabado")
			f1314 = ClaseHora.objects.filter(FK_HorarioCarrera = obj.HorarioCarrera).filter(Hora = "13-14").filter(Dia = "Sabado")
			f1415 = ClaseHora.objects.filter(FK_HorarioCarrera = obj.HorarioCarrera).filter(Hora = "14-15").filter(Dia = "Sabado")
			f1516 = ClaseHora.objects.filter(FK_HorarioCarrera = obj.HorarioCarrera).filter(Hora = "15-16").filter(Dia = "Sabado")
			f1617 = ClaseHora.objects.filter(FK_HorarioCarrera = obj.HorarioCarrera).filter(Hora = "16-17").filter(Dia = "Sabado")
			f1718 = ClaseHora.objects.filter(FK_HorarioCarrera = obj.HorarioCarrera).filter(Hora = "17-18").filter(Dia = "Sabado")
			f1819 = ClaseHora.objects.filter(FK_HorarioCarrera = obj.HorarioCarrera).filter(Hora = "18-19").filter(Dia = "Sabado")
			f1920 = ClaseHora.objects.filter(FK_HorarioCarrera = obj.HorarioCarrera).filter(Hora = "19-20").filter(Dia = "Sabado")
			f2021 = ClaseHora.objects.filter(FK_HorarioCarrera = obj.HorarioCarrera).filter(Hora = "20-21").filter(Dia = "Sabado")
			f2122 = ClaseHora.objects.filter(FK_HorarioCarrera = obj.HorarioCarrera).filter(Hora = "21-22").filter(Dia = "Sabado")
			g78 = ClaseHora.objects.filter(FK_HorarioCarrera = obj.HorarioCarrera).filter(Hora = "7-8").filter(Dia = "Domingo")
			g89 = ClaseHora.objects.filter(FK_HorarioCarrera = obj.HorarioCarrera).filter(Hora = "8-9").filter(Dia = "Domingo")
			g910 = ClaseHora.objects.filter(FK_HorarioCarrera = obj.HorarioCarrera).filter(Hora = "9-10").filter(Dia = "Domingo")
			g1011 = ClaseHora.objects.filter(FK_HorarioCarrera = obj.HorarioCarrera).filter(Hora = "10-11").filter(Dia = "Domingo")
			g1112 = ClaseHora.objects.filter(FK_HorarioCarrera = obj.HorarioCarrera).filter(Hora = "11-12").filter(Dia = "Domingo")
			g1213 = ClaseHora.objects.filter(FK_HorarioCarrera = obj.HorarioCarrera).filter(Hora = "12-13").filter(Dia = "Domingo")
			g1314 = ClaseHora.objects.filter(FK_HorarioCarrera = obj.HorarioCarrera).filter(Hora = "13-14").filter(Dia = "Domingo")
			g1415 = ClaseHora.objects.filter(FK_HorarioCarrera = obj.HorarioCarrera).filter(Hora = "14-15").filter(Dia = "Domingo")
			g1516 = ClaseHora.objects.filter(FK_HorarioCarrera = obj.HorarioCarrera).filter(Hora = "15-16").filter(Dia = "Domingo")
			g1617 = ClaseHora.objects.filter(FK_HorarioCarrera = obj.HorarioCarrera).filter(Hora = "16-17").filter(Dia = "Domingo")
			g1718 = ClaseHora.objects.filter(FK_HorarioCarrera = obj.HorarioCarrera).filter(Hora = "17-18").filter(Dia = "Domingo")
			g1819 = ClaseHora.objects.filter(FK_HorarioCarrera = obj.HorarioCarrera).filter(Hora = "18-19").filter(Dia = "Domingo")
			g1920 = ClaseHora.objects.filter(FK_HorarioCarrera = obj.HorarioCarrera).filter(Hora = "19-20").filter(Dia = "Domingo")
			g2021 = ClaseHora.objects.filter(FK_HorarioCarrera = obj.HorarioCarrera).filter(Hora = "20-21").filter(Dia = "Domingo")
			g2122 = ClaseHora.objects.filter(FK_HorarioCarrera = obj.HorarioCarrera).filter(Hora = "21-22").filter(Dia = "Domingo")

			ctx = {
				 "mensaje": mensaje, "form": form, "l78": l78, "b78": b78, "c78": c78,
				}

	else:
		form = ClaseHoraForm()
		ctx = { "form": form }

	return render(request, "Horario/formClaseHora_view.html", ctx)