
from django.urls import reverse_lazy
from django.views.generic.edit import CreateView

# Create your views here.

class SignUpView(CreateView):
    success_url = reverse_lazy("login")
    template_name = "usuarios/cadastro.html"
