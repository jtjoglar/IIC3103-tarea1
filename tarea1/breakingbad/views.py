from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
import requests

url_episodes = 'https://tarea-1-breaking-bad.herokuapp.com/api/episodes'
response = requests.get(url_episodes)
list_episodes = response.json()
dict_bb = {'1': {}, '2': {}, '3': {}, '4': {}, '5': {}}
dict_bcs = {'1': {}, '2': {}, '3': {}, '4': {}}

for ep_actual in list_episodes:
    if ep_actual['series'] == 'Breaking Bad':
        dict_bb[ep_actual['season']][str(ep_actual['episode'])] = ep_actual
    else:
        dict_bcs[ep_actual['season']][str(ep_actual['episode'])] = ep_actual


def index(request):
    context = {'series': ['Breaking Bad', 'Better Call Saul']}
    return render(request, 'breakingbad/index.html', context)

def breaking_bad(request):
    context = {'diccionario_bb': dict_bb}
    return render(request, 'breakingbad/breaking_bad.html', context)

def better_call_saul(request):
    context = {'diccionario_bcs': dict_bcs}
    return render(request, 'breakingbad/better_call_saul.html', context)

def temporada_bb(request, season_number):
    context = {'diccionario_season': dict_bb[str(season_number)]}
    return render(request, 'breakingbad/temporada_bb.html', context)

def episodio_bb(request, season_number, episode_number):
    context = {'diccionario_ep': dict_bb[str(season_number)][str(episode_number)]}
    return render(request, 'breakingbad/episodio_bb.html', context)

def temporada_bcs(request, season_number):
    context = {'diccionario_season': dict_bcs[str(season_number)]}
    return render(request, 'breakingbad/temporada_bcs.html', context)

def episodio_bcs(request, season_number, episode_number):
    context = {'diccionario_ep': dict_bcs[str(season_number)][str(episode_number)]}
    return render(request, 'breakingbad/episodio_bcs.html', context)

def personaje_esp(request, pers_name):
    if pers_name == "buscador":
        p_buscado = request.POST[pers_name]
        p_buscado = p_buscado.replace(" ", "+")
        url_buscado = 'https://tarea-1-breaking-bad.herokuapp.com/api/characters?name='+p_buscado
        response_b = requests.get(url_buscado)
        dict_buscado = response_b.json()
        context = {'personaje_b': dict_buscado}
        return render(request, 'breakingbad/buscador.html', context)

    else:
        payload = {'name': pers_name}
        url_p = 'https://tarea-1-breaking-bad.herokuapp.com/api/characters'
        response_p = requests.get(url_p, params=payload)
        dict_personaje = response_p.json()

        payload2 = {'author': pers_name}
        url_quotes = 'https://tarea-1-breaking-bad.herokuapp.com/api/quote'
        response_q = requests.get(url_quotes, params=payload2)
        dict_quotes = response_q.json()
        context = {'personaje': [dict_personaje, dict_quotes]}
        return render(request, 'breakingbad/personaje_esp.html', context)
