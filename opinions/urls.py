from django.urls import path
from . import views

urlpatterns = [
    path('', views.all_opinions, name="all_opinions"),
    path('<int:opinion_id>', views.single_opinion, name="opinion"),
    path('add-opinion', views.add_opinion, name='add_opinion'),
    path('delete_opinion/<int:opinion_id>', views.delete_opinion, name='delete_opinion'),
]
