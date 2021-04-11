from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.forms import formset_factory  
from django.http.response import HttpResponseRedirect
from shelter.models import Animal
from django.http import HttpResponse
from django.template import loader
from django.views.generic import ListView, DetailView, CreateView
from shelter.forms import AddPostForm
# Create your views here.
menu = [{'title': "О питомнике", 'url_name': 'about'},
        {'title': "Забрать домой", 'url_name': 'add_page'},
        {'title': "Обратная связь", 'url_name': 'contact'},
        {'title': "Войти", 'url_name': 'login'}
]

class AnimalView(ListView):
	model = Animal
	template_name = "shelter.html"
	context_object_name = 'posts'
	def get_context_data(self, *, object_list=None, **kwargs):
		context = super().get_context_data(**kwargs)
		context['title'] = 'Главная страница'
		context['menu'] = menu
		context['cat_selected'] = 0
		return context
class ShowAnimal(DetailView):
    model = Animal
    template_name = 'show.html'
    context_object_name = 'post'
    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['menu'] = menu
        return context
class AddAnimal(CreateView):
    form_class = AddPostForm
    template_name = 'addpage.html'
    success_url = reverse_lazy('home')

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Добавление животного'
        context['menu'] = menu
        return context