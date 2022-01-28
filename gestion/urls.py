from django.urls import path

from gestion import views

app_name = 'gestion'

urlpatterns = [
    path('creation-utilisateur', views.CreateUtilisateurView.as_view(), name='creation-utilisateur'),
    path('modification-utilisateur/<int:pk>', views.EditUtilisateurView.as_view(), name='edition-utilisateur'),
    path('liste-utilisateur', views.ListUtilisateurView.as_view(), name='liste-utilisateur'),

    path('creation-tache', views.CreateTacheView.as_view(), name='creation-tache'),
    path('modification-tache/<int:pk>', views.EditTacheView.as_view(), name='edition-tache'),
    path('liste-tache', views.ListTacheView.as_view(), name='liste-tache'),

]