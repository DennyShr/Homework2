from django.contrib import admin
from .models import  Pizza_name, Ingredient, Pizza, Every, PizzaOrdered

class AdminPizza_name(admin.ModelAdmin):
	list_display = ('name', 'price', 'weight')

class AdminIngredients(admin.ModelAdmin):
	list_display = ('name', 'price', 'weight', 'Is_vegan')

admin.site.register(Pizza_name, AdminPizza_name)
admin.site.register(Ingredient, AdminIngredients)
admin.site.register(Pizza)
admin.site.register(Every)
admin.site.register(PizzaOrdered)