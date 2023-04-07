"""MiFamilia URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
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
from familiares.views import saludo , familia, mostrar_familia,mostrar_familia_tabla

urlpatterns = [
    path('admin/', admin.site.urls),
    path("familia/<nombre>/<apellido>/<edad>",saludo),
    path("familia/personas",familia),
    path("familia/mostrar",mostrar_familia),
    path("familia/mostrar_tabla",mostrar_familia_tabla)

]
