"""taffe URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.contrib.auth import views as auth
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('connexion/', auth.LoginView.as_view(template_name="connexion.html"), name="connexion"),

    path('core/', include("core.urls")),
    # partie apporteur
    path('apporteur/', include("apporteur.urls")),
    path('assure/', include("assure.urls")),
    path('assureur/', include("assureur.urls")),
    path('courtier/', include("courtier.urls")),
    path('tier/', include("tier.urls")),

    # Partie gestion
    path('gestion/', include("gestion.urls")),

] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)\
  + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
