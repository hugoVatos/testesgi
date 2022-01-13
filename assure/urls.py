
from  django.urls import path
from assure import views
app_name = 'assure'

urlpatterns = [
    path('assure-nouveau', views.CreateAssureView.as_view(), name='creation-assure'),
]