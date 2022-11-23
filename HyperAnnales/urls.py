"""HyperAnnales URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/dev/topics/http/urls/
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
from django.contrib import admin
from django.urls import path
from django.conf.urls import include, url
from django.contrib.auth import urls, views
from django.views.generic import RedirectView
from django.contrib.sitemaps.views import sitemap
from . import views, signup, logout, login, secret

urlpatterns = [
    #Redirections
    path('accounts/login/', RedirectView.as_view(url='/login/')),
    #path('robot.txt', views.robot),
    #path('sitemap.xml', sitemap, {'sitemaps': sitemaps}, name='django.contrib.sitemaps.views.sitemap'),
    #Accueil
    path('', views.index),
    #Administration
    path('admin/', admin.site.urls),
    #Gestion utilisateur
    path('signup/', signup.signup_view),
    url(r'^activate/(?P<uidb64>[0-9A-Za-z_\-\']+)/(?P<token>[0-9A-Za-z]{1,13}-[0-9A-Za-z]{1,20})/$',signup.activate, name='activate'),
    path('login/', login.login_view),
    path('logout/', logout.logout_view),
    #Reset password
    path('password_reset/', include('django.contrib.auth.urls')),
    #Gestion des fichiers
    path('pdf/', include('pdf.urls')),
    path('Docs/', views.docs),
    #Gestion des fichiers sensibles
    path('secret/', secret.secret_index),
    path('secret/<str:matiere>/', secret.secret),
    path('secret/<str:matiere>/pdf/<int:Id>/', secret.mega_secret),
    #Gestion de la navigation
    path('<int:annee>/', views.promo),
    path('<int:annee>/<str:option>/', views.url_option),
    path('<int:annee>/<str:semestre>/<str:matiere>/', views.url_matiere),
]
