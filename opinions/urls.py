from django.urls import path
from . import views

urlpatterns = [
    path('', views.all_opinions, name="all_opinions"),
    path('1', views.single_opinion, name="opinion"),
    path('add-opinion', views.add_opinion, name='add_opinion')
]
