from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('breaking_bad/', views.breaking_bad, name='breaking_bad'),
    path('breaking_bad/<int:season_number>/', views.temporada_bb, name='temporada_bb'),
    path('breaking_bad/<int:season_number>/<int:episode_number>/', views.episodio_bb, name='episodio_bb'),
    path('better_call_saul/', views.better_call_saul, name='better_call_saul'),
    path('better_call_saul/<int:season_number>/', views.temporada_bcs, name='temporada_bcs'),
    path('better_call_saul/<int:season_number>/<int:episode_number>/', views.episodio_bcs, name='episodio_bcs'),
    path('<str:pers_name>/', views.personaje_esp, name='personaje_esp'),
]
