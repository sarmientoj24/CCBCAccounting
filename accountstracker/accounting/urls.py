from django.urls import path
from . import views

urlpatterns = [
    path('', views.transactions, name="transactions"),
    path('export_to_csv/', views.export_to_csv, name="export_to_csv"),
]
