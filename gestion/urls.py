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

    path('creation-risque', views.CreateRisqueView.as_view(), name='creation-risque'),
    path('modification-risque/<int:pk>', views.EditRisqueView.as_view(), name='edition-risque'),
    path('liste-risque', views.ListRisqueView.as_view(), name='liste-risque'),

    path(r'download-reclamation/<int:pk>', views.download_reclamation, name="telechargement-reclamation"),
    path(r'download-risque/<int:pk>', views.download_risque, name="telechargement-risque"),

    path('creation-taxe', views.CreateTaxeView.as_view(), name='creation-taxe'),
    path('modification-taxe/<int:pk>', views.EditTaxeView.as_view(), name='edition-taxe'),
    path('liste-taxe', views.ListTaxeView.as_view(), name='liste-taxe'),
]