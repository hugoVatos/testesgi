
from  django.urls import path
from assureur import views
app_name = 'assureur'

urlpatterns = [
    path('assureur-nouveau', views.CreateAssureurView.as_view(), name='creation-assureur'),
    path('assureur-gestion', views.ListAssureurView.as_view(), name='gestion-assureur'),
    path('assureur-edit', views.EditAssureurView.as_view(), name='edit-assureur')
]