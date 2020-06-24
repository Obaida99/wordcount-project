
from django.urls import path
from . import views # . means from this project or this dir
urlpatterns = [
    path('', views.homepage, name='home'),
    path('count/', views.count, name='count'),
    path('about/', views.about, name='about'),

]
