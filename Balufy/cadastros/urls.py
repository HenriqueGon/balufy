from django.urls import path

from .views import IndexView, PlaylistCreate, AuthorCreate, SongCreate
from .views import PlaylistUpdate, AuthorUpdate, SongUpdate
from .views import PlaylistDelete, AuthorDelete, SongDelete

urlpatterns = [
    path('', IndexView.as_view(),
         name='index'),
    path('cadastrar/playlist/', PlaylistCreate.as_view(),
         name='cadastrar-playlist'),
    path('cadastrar/autor/', AuthorCreate.as_view(), 
          name='cadastrar-autor'),
    path('cadastrar/musica/', SongCreate.as_view(),
         name='cadastrar-musica'),

    path('editar/playlist/<int:pk>/',
         PlaylistUpdate.as_view(), name='editar-playlist'),
    path('editar/autor/<int:pk>/',
         AuthorUpdate.as_view(), name='editar-autor'),
    path('editar/musica/<int:pk>/',
         SongUpdate.as_view(), name='editar-musica'),

    path('excluir/playlist/<int:pk>/',
         PlaylistDelete.as_view(), name='excluir-playlist'),
    path('excluir/autor/<int:pk>/',
         AuthorDelete.as_view(), name='excluir-autor'),
    path('excluir/musica/<int:pk>/',
         SongDelete.as_view(), name='excluir-musica'),
]
