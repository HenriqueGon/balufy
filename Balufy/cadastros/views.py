from django.shortcuts import render
from django.shortcuts import get_object_or_404

# Create your views here.

from dataclasses import field
from pyexpat import model
from django.urls import reverse_lazy
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic.list import ListView
from django.views.generic import TemplateView

from django.contrib.auth.mixins import LoginRequiredMixin
from braces.views import GroupRequiredMixin

from .models import Playlist, Author, Song

# Create your views here.
class IndexView(TemplateView):
    template_name = 'cadastros/index.html'

class PlaylistCreate(LoginRequiredMixin, CreateView):
    model = Playlist
    fields = ['name', 'description']
    template_name = 'cadastros/form.html'
    success_url = reverse_lazy('listar-playlist')
    # login_url = reverse_lazy('login')

class AuthorCreate(GroupRequiredMixin, CreateView):
    model = Author
    fields = ['name', 'description']
    group_required = u"Administrador"
    template_name = 'cadastros/form.html'
    success_url = reverse_lazy('index')

class SongCreate(GroupRequiredMixin, CreateView):
    model = Song
    fields = ['name', 'duration', 'url']
    group_required = u"Administrador"
    template_name = 'cadastros/form.html'
    success_url = reverse_lazy('index')


###################################


class PlaylistUpdate(LoginRequiredMixin, UpdateView):
    model = Playlist
    fields = ['name', 'description']
    template_name = 'cadastros/form.html'
    success_url = reverse_lazy('listar-playlist')

    def get_object(self, queryset=None):
        self.object = get_object_or_404(
            PlaylistUpdate, pk=self.kwargs['pk'], user=self.request.user)

        return self.object



class AuthorUpdate(GroupRequiredMixin, UpdateView):
    model = Author
    fields = ['name', 'description']
    group_required = u"Administrador"
    template_name = 'cadastros/form.html'
    success_url = reverse_lazy('index')


class SongUpdate(GroupRequiredMixin, UpdateView):
    model = Song
    fields = ['name', 'description', 'url']
    group_required = u"Administrador"
    template_name = 'cadastros/form.html'
    success_url = reverse_lazy('index')

####################################


class PlaylistDelete(LoginRequiredMixin, DeleteView):
    model = Playlist
    template_name = 'cadastros/form-delete.html'
    success_url = reverse_lazy('listar-playlist')

    def get_object(self, queryset=None):
        self.object = get_object_or_404(
            PlaylistDelete, pk=self.kwargs['pk'], user=self.request.user)
        return self.object

class AuthorDelete(GroupRequiredMixin, DeleteView):
    model = Author
    group_required = u"Administrador"
    template_name = 'cadastros/form-delete.html'
    success_url = reverse_lazy('index')


class SongDelete(GroupRequiredMixin, DeleteView):
    model = Song
    group_required = u"Administrador"
    template_name = 'cadastros/form-delete.html'
    success_url = reverse_lazy('index')


#################################

class PlaylistList(LoginRequiredMixin, ListView):
    model = Playlist
    template_name = 'listas/playlist.html'

    def get_queryset(self):
        self.object_list = Playlist.objects.filter(user=self.request.user)

        return self.object_list


class AuthorList(GroupRequiredMixin, ListView):
    model = Author
    group_required = u"Administrador"
    template_name = 'listas/author.html'

    # def get_queryset(self):
    #     self.object_list = Author.objects.filter(user=self.request.user)

    #     return self.object_list


class SongList(GroupRequiredMixin, ListView):
    model = Song
    group_required = u"Administrador"
    template_name = 'listas/song.html'

    # def get_queryset(self):
    #     self.object_list = Song.objects.filter(user=self.request.user)

    #     return self.object_list
