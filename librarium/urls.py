from django.urls import path
from . import views

urlpatterns = [
    path("", views.v_index, name="v_index"),
    path("reporte.pdf", views.v_reporte_pdf, name="v_reporte_pdf"),
    path('data-analitica', views.data_analitica, name='data_analitica'),
    path('data-frames', views.data_frames, name='data_frames'),
    path('servicios', views.servicios, name='servicios'),
]
