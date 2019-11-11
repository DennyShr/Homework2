from django.db import models

class Pizza_name(models.Model):
	name = models.CharField('Pizza', max_length = 30)
	price = models.DecimalField('Price', max_digits = 5, decimal_places = 2, default = 0)
	weight = models.IntegerField('grams')

	def __str__ (self):
		return 'Pizza: {}'.format(self.name)

class Ingredient(models.Model):
	name = models.CharField('Ingredient', max_length = 30)
	price = models.DecimalField('Price', max_digits = 5, decimal_places = 2, default = 0)
	weight = models.IntegerField('grams')
	Is_vegan = models.BooleanField('Vegan')

	def __str__ (self):
		return 'Ingredient: {}'.format(self.name)

class Pizza(models.Model):
	pizza_name = models.ForeignKey(Pizza_name, on_delete = models.CASCADE)
	ingredients = models.ManyToManyField(Ingredient)

	def __str__(self):
		return str(self.pizza_name)
	
		