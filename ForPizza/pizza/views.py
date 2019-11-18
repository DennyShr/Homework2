from django.views.generic import ListView, TemplateView
from django.views import View
from .models import Pizza_name
from django.http import HttpResponse


class PizzasList(ListView):
	model = Pizza_name
	template_name = 'pizza/pizza.html' #template_name = '(modelname)_list.html' - by default

class PizzaTemplateView(TemplateView):
	template_name = 'pizza/pizza_template.html'

class MyView(View):
	def get(self, request):
		return HttpResponse("Hello, it's view")

	

# Create your views here.
