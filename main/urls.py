from django.urls import path
from . import views

urlpatterns = [
    path('', views.homepage, name="homepage"),
    path('about-us', views.about_us, name="about_us"),
    path('contact-us', views.contact_us, name='contact_us'),
    path('thanks/', views.thanks, name='thanks'),
    path('news', views.all_news, name='news')
]
