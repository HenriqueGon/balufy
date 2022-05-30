from django.db import models

# Create your models here.

class Playlist(models.Model):
  name = models.CharField(
    max_length=255, help_text="Digite o nome da playlist", default="Minha playlist")

  description = models.CharField(
    max_length=255)

  image = models.CharField(
    max_length=255)

  def __str__(self):
    return f'{self.name} - {self.description}'

class Author(models.Model):
  name = models.CharField(
    max_length=255, help_text="Digite o nome do autor")

  description = models.CharField(
    max_length=255)

  def __str__(self):
    return f'{self.name} - {self.duration}'

class Song(models.Model):
  name = models.CharField(
    max_length=255, help_text="Digite o nome da musica")

  duration = models.TimeField(help_text="Digite o tempo de duração da musica")

  # playlist = models.ForeignKey(Playlists, on_delete=models.PROTECT)

  def __str__(self):
    return f'{self.name} - {self.duration}'
