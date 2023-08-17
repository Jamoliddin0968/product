from django.urls import path

from shop.views import hello

from . import views

urlpatterns = [
    path('list/', views.ProductList.as_view()),
]
