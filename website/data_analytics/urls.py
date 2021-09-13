from django.urls import path
from . import views

app_name = 'data'

urlpatterns = [
    path('input_data/', views.CSV_page),
    path('csv_data_set/', views.data_CSV), 
    path('csv_data_set/clean_data/', views.clean_data)
]
