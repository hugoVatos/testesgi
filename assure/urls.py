
from  django.urls import path
from assure import views
app_name = 'assure'

urlpatterns = [
    path('assure-nouveau', views.CreateAssureView.as_view(), name='creation-assure'),
    path('assure-gestion', views.ListAssureView.as_view(), name='gestion-assure'),
    path('assure-edit', views.EditAssureView.as_view(), name='edit-assure')
]