from django.urls import path

from payment import views

urlpatterns = [
    path("cart/", views.cart),
    path("purchase/", views.purchase),
    path("complete/", views.complete),
]
