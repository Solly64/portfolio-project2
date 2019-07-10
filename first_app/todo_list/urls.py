from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('about', views.about, name='about'),
    path('delete/<list_id>', views.delete, name= 'delete'),
    path('nfl_week1', views.nfl_week1, name= 'nfl_week1'),
]
