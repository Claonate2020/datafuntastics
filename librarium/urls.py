from django.urls import path
from . import views

urlpatterns = [
    path("", views.v_index, name="v_index"),
    path("reporte.pdf", views.v_reporte_pdf, name="v_reporte_pdf"),
]
