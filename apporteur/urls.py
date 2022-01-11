
from  django.urls import path
from apporteur import views
app_name = 'apporteur'

urlpatterns = [
    path('apporteur-nouveau', views.CreateApporteurView.as_view(), name='creation-apporteur'),
]