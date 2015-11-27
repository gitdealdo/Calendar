from django.conf.urls import url

urlpatterns = [
    url(r'^$', 'apps.calendario.views.calendar', name='panel'),
    url(r'^institucion$', 'apps.informes.views.institucion', name='institucion'),    
    url(r'^institucion/registro/nuevo/$', 'apps.informes.views.crear_registro', name='nuevo'),    
]
