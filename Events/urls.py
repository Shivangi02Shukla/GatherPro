from django.urls import path, include
from .views import *
from . import views

urlpatterns = [
    path('', home, name='home'),
    path('sabrang/', sabrang, name='sabrang'),
    path('sabrang-2022/', views.sabrang22.as_view(), name='sabrang22'),
    path('events/<int:myid>', views.sabrang22view.as_view(), name='sabrang22'),
    path('our-team/', views.team.as_view(), name='Our Team'),
    path('sponsors/', views.sponsors.as_view(), name='Sponsors'),
]
