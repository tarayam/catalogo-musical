from django.urls import path
from . import views

app_name = "musica"

urlpatterns = [
    path("", views.home, name="home"),
    path("<slug:genero_slug>/", views.bandas_por_genero, name="bandas"),
    path("<slug:genero_slug>/<slug:banda_slug>/", views.discos_por_banda, name="discos"),
    path("<slug:genero_slug>/<slug:banda_slug>/<slug:album_slug>/", views.album_detalle, name="album"),
]
