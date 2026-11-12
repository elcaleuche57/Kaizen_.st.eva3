from django.shortcuts import render

from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.messages.views import SuccessMessageMixin
from django.urls import reverse_lazy
from django.views.generic import (
    ListView, DetailView, CreateView, UpdateView, DeleteView,
)
from .forms import PrendaForm
from .models import Prenda


class PrendaListView(ListView):
    model = Prenda
    template_name = "catalogo/lista.html"
    context_object_name = "prendas"

    def get_queryset(self):
        # Un solo JOIN: evita el problema N+1
        return Prenda.objects.select_related("categoria")


class PrendaDetailView(DetailView):
    model = Prenda
    template_name = "catalogo/detalle.html"


class PrendaCreateView(LoginRequiredMixin, SuccessMessageMixin, CreateView):
    model = Prenda
    form_class = PrendaForm
    template_name = "catalogo/form.html"
    success_url = reverse_lazy("lista")
    success_message = "Prenda creada correctamente."


class PrendaUpdateView(LoginRequiredMixin, SuccessMessageMixin, UpdateView):
    model = Prenda
    form_class = PrendaForm
    template_name = "catalogo/form.html"
    success_url = reverse_lazy("lista")
    success_message = "Prenda actualizada correctamente."


class PrendaDeleteView(LoginRequiredMixin, DeleteView):
    model = Prenda
    template_name = "catalogo/confirmar_eliminar.html"
    success_url = reverse_lazy("lista")

    def form_valid(self, form):
        messages.success(self.request, "Prenda eliminada correctamente.")
        return super().form_valid(form)
