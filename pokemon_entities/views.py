from django.utils import timezone
import folium

from django.http import HttpResponseNotFound
from django.shortcuts import get_object_or_404, render
from pokemon_entities.models import Pokemon,PokemonEntity


MOSCOW_CENTER = [55.751244, 37.618423]
DEFAULT_IMAGE_URL = (
    'https://vignette.wikia.nocookie.net/pokemon/images/6/6e/%21.png/revision'
    '/latest/fixed-aspect-ratio-down/width/240/height/240?cb=20130525215832'
    '&fill=transparent'
)


def add_pokemon(folium_map, lat, lon, image_url=DEFAULT_IMAGE_URL):
    icon = folium.features.CustomIcon(
        image_url,
        icon_size=(50, 50),
    )
    folium.Marker(
        [lat, lon],
        icon=icon,
    ).add_to(folium_map)


def show_all_pokemons(request):

    folium_map = folium.Map(location=MOSCOW_CENTER, zoom_start=12)

    current_time = timezone.localtime()
    pokemonentities = PokemonEntity.objects.filter(disappeared_at__gte=current_time, appeared_at__lte=current_time)
    for pokemon_entity in pokemonentities:
        add_pokemon(
            folium_map, pokemon_entity.lat,
            pokemon_entity.lon,
            request.build_absolute_uri(pokemon_entity.pokemon.photo.url)
        )

    pokemons_on_page = []
    pokemons = Pokemon.objects.all()
    for pokemon in pokemons:
        pokemons_on_page.append({
            'pokemon_id': pokemon.id,
            'img_url': request.build_absolute_uri(pokemon.photo.url),
            'title_ru': pokemon.title,
        })

    return render(request, 'mainpage.html', context={
        'map': folium_map._repr_html_(),
        'pokemons': pokemons_on_page,
    })


def show_pokemon(request, pokemon_id):

    requested_pokemon = get_object_or_404(Pokemon,id=pokemon_id)

    pokemon = {
            'title_ru': requested_pokemon.title,
            'title_en': requested_pokemon.title_en,
            'title_jp': requested_pokemon.title_jp,
            'description': requested_pokemon.description,
            'img_url': request.build_absolute_uri(requested_pokemon.photo.url),
            }
   
    next_evolution = requested_pokemon.ancestor_pokemon.first()
    if next_evolution:
        pokemon ['next_evolution'] = {
            'title_ru': next_evolution.title,
            'pokemon_id': next_evolution.id,
            'img_url': request.build_absolute_uri(next_evolution.photo.url)
            }

    if requested_pokemon.parent:
        pokemon ['previous_evolution'] = {
            'title_ru': requested_pokemon.parent.title,
            'pokemon_id': requested_pokemon.parent.id,
            'img_url': request.build_absolute_uri(requested_pokemon.parent.photo.url)
            }

    folium_map = folium.Map(location=MOSCOW_CENTER, zoom_start=12)

    for pokemon_entity in PokemonEntity.objects.filter(pokemon=requested_pokemon):
        add_pokemon(
            folium_map, pokemon_entity.lat,
            pokemon_entity.lon,
            request.build_absolute_uri(pokemon_entity.pokemon.photo.url)
        )

    return render(request, 'pokemon.html', context={
        'map': folium_map._repr_html_(), 'pokemon': pokemon
    })