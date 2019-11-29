from django.urls import path
from .views import PizzasList, PizzaTemplateView, MyView, PizzaOrderCreate, FeedbackView

urlpatterns = [
	path('pizzas/', PizzasList.as_view()),
	path('', PizzaTemplateView.as_view()),
	path('feedback/', FeedbackView.as_view()),
	path('view/', MyView.as_view()),
	path('pizza_order/add/', PizzaOrderCreate.as_view(), name='order-add'),
]