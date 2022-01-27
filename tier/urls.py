
from  django.urls import path
from tier import views
app_name = 'tier'

urlpatterns = [
    path('tier-nouveau', views.CreateTierView.as_view(), name='creation-tier'),
    path('tier-gestion', views.ListTierView.as_view(), name='gestion-tier'),
    path('tier-edit', views.EditTierView.as_view(), name='edit-tier')
]