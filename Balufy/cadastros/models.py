from django.db import models

# Create your models here.

class Playlist(models.Model):
  name = models.CharField(
    max_length=255, help_text="Digite o nome da playlist", default="Minha playlist")

  description = models.CharField(
    max_length=255, help_text="Descrição da playlist")

  # image = models.ImageField(upload_to='') // adicionar na pasta que será criada futuramente.

  created_at = models.DateTimeField(auto_now_add=True)

  updated_at = models.DateTimeField(auto_now=True)

  def __str__(self):
    return f'{self.name} - {self.description}'

class Author(models.Model):
  name = models.CharField(
    max_length=255, help_text="Digite o nome do autor")

  description = models.CharField(
    max_length=255, help_text='Descrição do autor')

  created_at = models.DateTimeField(auto_now_add=True)

  updated_at = models.DateTimeField(auto_now=True)

  def __str__(self):
    return f'{self.name} - {self.description}'

class Song(models.Model):
  name = models.CharField(
    max_length=255, help_text="Digite o nome da musica")

  duration = models.TimeField(help_text="Digite o tempo de duração da musica")

  url = models.URLField(max_length=255)

  created_at = models.DateTimeField(auto_now_add=True)

  updated_at = models.DateTimeField(auto_now=True)

  def __str__(self):
    return f'{self.name} - {self.duration}'

class Playlist_Songs(models.Model):
  playlist = models.ForeignKey(Playlist, on_delete=models.PROTECT)
  author = models.ForeignKey(Author, on_delete=models.PROTECT)
