from django.urls import path

from core import views


app_name = 'core'
urlpatterns = [

    # Suppression d'un objet, peu importe sa classe (préciser le module, la classe et l'url de retour en query)
    path('suppression/<int:pk>', views.DeleteObjectView.as_view(), name='suppression'),
]
