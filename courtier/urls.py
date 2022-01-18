
from  django.urls import path
from courtier import views
app_name = 'courtier'

urlpatterns = [
    path('courtier-nouveau', views.CreateCourtierView.as_view(), name='creation-courtier'),
    path('courtier-gestion', views.ListCourtierView.as_view(), name='gestion-courtier')
]