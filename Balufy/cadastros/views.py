from django.shortcuts import get_object_or_404

# Create your views here.

from django.urls import reverse_lazy
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic.list import ListView
from django.views.generic import TemplateView

from django.contrib.auth.mixins import LoginRequiredMixin
from braces.views import GroupRequiredMixin

from .models import Playlist, Author, Song

# Create your views here.


class PlaylistContext(object):
    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)

        if self.request.user.is_authenticated:
            context['playlists'] = Playlist.objects.filter(user=self.request.user)
        else:
            context['playlists'] = None

        return context


class IndexView(PlaylistContext, TemplateView):
    template_name = 'cadastros/index.html'

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)

        context['songs'] = Song.objects.all()

        return context


class PlaylistCreate(LoginRequiredMixin, PlaylistContext, CreateView):
    model = Playlist
    fields = ['name', 'description']
    template_name = 'cadastros/form.html'
    # success_url = reverse_lazy('cadastros/form.html')
    # login_url = reverse_lazy('login')

    def form_valid(self, form):

        form.instance.user = self.request.user

        return super().form_valid(form)


class AuthorCreate(GroupRequiredMixin, PlaylistContext, CreateView):
    model = Author
    fields = ['name', 'description']
    group_required = u"Administrador"
    template_name = 'cadastros/form.html'
    success_url = reverse_lazy('listar-autor')


class SongCreate(GroupRequiredMixin, PlaylistContext, CreateView):
    model = Song
    fields = ['name', 'duration', 'url', 'author']
    group_required = u"Administrador"
    template_name = 'cadastros/form.html'
    success_url = reverse_lazy('listar-musica')


###################################


class PlaylistUpdate(LoginRequiredMixin, PlaylistContext, UpdateView):
    model = Playlist
    fields = ['name', 'description']
    template_name = 'cadastros/form.html'
    success_url = reverse_lazy('listar-playlist')

    def get_object(self, queryset=None):
        self.object = get_object_or_404(
            Playlist, pk=self.kwargs['pk'], user=self.request.user)

        return self.object


class AuthorUpdate(GroupRequiredMixin, PlaylistContext, UpdateView):
    model = Author
    fields = ['name', 'description']
    group_required = u"Administrador"
    template_name = 'cadastros/form.html'
    success_url = reverse_lazy('listar-autor')


class SongUpdate(GroupRequiredMixin, PlaylistContext, UpdateView):
    model = Song
    fields = ['name', 'duration', 'url', 'author']
    group_required = u"Administrador"
    template_name = 'cadastros/form.html'
    success_url = reverse_lazy('listar-musica')

####################################


class PlaylistDelete(LoginRequiredMixin, DeleteView):
    model = Playlist
    template_name = 'cadastros/form-delete.html'
    success_url = reverse_lazy('listar-playlist')

    def get_object(self, queryset=None):
        self.object = get_object_or_404(
            Playlist, pk=self.kwargs['pk'], user=self.request.user)
        return self.object

class AuthorDelete(GroupRequiredMixin, DeleteView):
    model = Author
    group_required = u"Administrador"
    template_name = 'cadastros/form-delete.html'
    success_url = reverse_lazy('listar-autor')


class SongDelete(GroupRequiredMixin, DeleteView):
    model = Song
    group_required = u"Administrador"
    template_name = 'cadastros/form-delete.html'
    success_url = reverse_lazy('listar-musica')


#################################

class PlaylistList(LoginRequiredMixin, PlaylistContext, ListView):
    model = Playlist
    template_name = 'listas/playlist.html'

    def get_queryset(self):
        playlists = Playlist.objects.get(user=self.request.user)

        self.object_list = playlists.songs.all()
        
        return self.object_list


class AuthorList(GroupRequiredMixin, PlaylistContext, ListView):
    model = Author
    group_required = u"Administrador"
    template_name = 'listas/author.html'

    # def get_queryset(self):
    #     self.object_list = Author.objects.filter(user=self.request.user)

    #     return self.object_list


class SongList(GroupRequiredMixin, PlaylistContext, ListView):
    model = Song
    group_required = u"Administrador"
    template_name = 'listas/song.html'

    # def get_queryset(self):
    #     self.object_list = Song.objects.filter(user=self.request.user)

    #     return self.object_list
