from django.db import models
from django.contrib.auth.models import User

# Create your models here.


class Playlist(models.Model):
    name = models.CharField(
        max_length=255, help_text="Digite o nome da playlist", default="Minha playlist", verbose_name='Nome:')

    description = models.CharField(
        max_length=255, help_text="Descrição da playlist", verbose_name='Descrição:')

    # image = models.ImageField(upload_to='') // adicionar na pasta que será criada futuramente.

    user = models.ForeignKey(User, on_delete=models.PROTECT)

    created_at = models.DateTimeField(auto_now_add=True)

    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'{self.name}'


class Author(models.Model):
    name = models.CharField(
        max_length=255, help_text="Digite o nome do autor", verbose_name='Nome')

    description = models.CharField(
        max_length=255, help_text='Descrição do autor', verbose_name='Descrição:')

    created_at = models.DateTimeField(auto_now_add=True)

    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'{self.name}'


class Song(models.Model):
    name = models.CharField(
        max_length=255, help_text="Digite o nome da musica", verbose_name='Nome:')

    duration = models.TimeField(
        help_text="Digite o tempo de duração da musica", verbose_name='Duração:')

    url = models.URLField(max_length=255)

    author = models.ForeignKey(Author, on_delete=models.PROTECT)

    created_at = models.DateTimeField(auto_now_add=True)

    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'{self.name}'


class Playlist_Songs(models.Model):
    playlist = models.ForeignKey(Playlist, on_delete=models.PROTECT)
    song = models.ForeignKey(Song, on_delete=models.PROTECT)
