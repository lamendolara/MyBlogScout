import datetime
#
from django.shortcuts import render
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy, reverse

from django.views.generic import (
    TemplateView,
    CreateView
)

# apps entrada
from applications.entrada.models import Entry

# models
from .models import Home

# forms
from .forms import SuscribersForm, ContactForm


class HomePageView(TemplateView):
    template_name = "home/index.html"

    
    def get_context_data(self, **kwargs):
        context = super(HomePageView, self).get_context_data(**kwargs)
        # Cargamos el home
        context["home"] = Home.objects.latest('created')
        # Contexto de portada
        context["portada"] = Entry.objects.entrada_en_portada()
        # Contexto para los articulos en home
        context["entradas_home"] = Entry.objects.entradas_en_home()
        # Contexto para las entradas recientes
        context["entradas_recientes"] = Entry.objects.entradas_recientes()
        # Enviamos formulario de suscripción
        context["form"] = SuscribersForm 
        return context
    


class SuscriberCreateView(CreateView):
    """Permite guardar el mail de suscripcion mediante el formulario SuscribersForm, 
    sin crear el atributo template_name"""
    form_class = SuscribersForm
    success_url = '.'


class ContactCreateView(CreateView):
    form_class = ContactForm
    success_url = '.'
    



