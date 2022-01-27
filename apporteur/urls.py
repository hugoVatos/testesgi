
from  django.urls import path
from apporteur import views
app_name = 'apporteur'

urlpatterns = [
    path('apporteur-nouveau', views.CreateApporteurView.as_view(), name='creation-apporteur'),
    path('apporteur-gestion', views.ListApporteurView.as_view(), name='gestion-apporteur'),
    path('apporteur-edit/<int:pk>', views.EditApporteurView.as_view(), name='edit-apporteur')
]