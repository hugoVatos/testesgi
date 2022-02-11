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

    path('creation-navire', views.CreateNavireView.as_view(), name='creation-navire'),
    path('modification-navire/<int:pk>', views.EditNavireView.as_view(), name='edition-navire'),
    path('liste-navire', views.ListNavireView.as_view(), name='liste-navire'),

    path('creation-reclamation', views.CreateReclamationView.as_view(), name='creation-reclamation'),
    path('modification-reclamation/<int:pk>', views.EditReclamationView.as_view(), name='edition-reclamation'),
    path('liste-reclamation', views.ListReclamationView.as_view(), name='liste-reclamation'),

]