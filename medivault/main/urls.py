from django.urls import path
from main import views

urlpatterns = [
   path("",view=views.home,name='main'),
   path("contact/",view=views.contact,name='contact'),
   path('about/',view=views.about,name='about'),
]
