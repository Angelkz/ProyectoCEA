from django.conf import settings
from django.conf.urls import include, url, patterns
from .views import *


urlpatterns = [

 		url(r'^titulo/$', formTitulo, name = 'formTitulo'),
 		url(r'^gradomaximo/$', formGradoMaximo, name = 'formGradoMaximo'),
 		url(r'^carrera/$', formCarrera, name = 'formCarrera'),

 		url(r'^profesor/$', formProfesor, name = 'formProfesor'),
 		url(r'^materia/$', formMateria, name = 'formMateria'),
 		url(r'^profesormateria/$', formProfesorMateria, name = 'formProfesorMateria'),
 		url(r'^profesorhora/$', formProfesorHora, name = 'formProfesorHora'),

]