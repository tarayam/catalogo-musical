from django.shortcuts import render, get_object_or_404
from .data import CATALOGO

def home(request):
    # Catálogo principal: géneros
    generos = [
        {"slug": slug, "nombre": data["nombre"], "bandas_count": len(data.get("bandas", {}))}
        for slug, data in CATALOGO.items()
    ]
    context = {"generos": generos}
    return render(request, "musica/generos.html", context)

def bandas_por_genero(request, genero_slug):
    genero = CATALOGO.get(genero_slug)
    if not genero:
        return render(request, "musica/404.html", status=404)
    bandas = [
        {"slug": slug, "nombre": data["nombre"], "albums": len(data.get("discografia", {}))}
        for slug, data in genero.get("bandas", {}).items()
    ]
    context = {"genero_slug": genero_slug, "genero_nombre": genero["nombre"], "bandas": bandas}
    return render(request, "musica/bandas.html", context)

def discos_por_banda(request, genero_slug, banda_slug):
    genero = CATALOGO.get(genero_slug)
    if not genero or banda_slug not in genero.get("bandas", {}):
        return render(request, "musica/404.html", status=404)
    banda = genero["bandas"][banda_slug]
    discos = [
        {"slug": slug, **data}
        for slug, data in banda.get("discografia", {}).items()
    ]
    context = {
        "genero_slug": genero_slug,
        "genero_nombre": genero["nombre"],
        "banda_slug": banda_slug,
        "banda_nombre": banda["nombre"],
        "discos": discos,
    }
    return render(request, "musica/discos.html", context)

def album_detalle(request, genero_slug, banda_slug, album_slug):
    genero = CATALOGO.get(genero_slug)
    if not genero:
        return render(request, "musica/404.html", status=404)
    banda = genero.get("bandas", {}).get(banda_slug)
    if not banda:
        return render(request, "musica/404.html", status=404)
    album = banda.get("discografia", {}).get(album_slug)
    if not album:
        return render(request, "musica/404.html", status=404)

    context = {
        "genero_slug": genero_slug,
        "genero_nombre": genero["nombre"],
        "banda_slug": banda_slug,
        "banda_nombre": banda["nombre"],
        "album_slug": album_slug,
        "album": album,
    }
    return render(request, "musica/album.html", context)
# Nota: Asegúrate de tener plantillas HTML adecuadas en la carpeta templates/musica/