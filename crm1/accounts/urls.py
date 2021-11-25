from django.urls import path
from django.contrib.auth import views as auth_views
from . import views

urlpatterns = [
    path('product/', views.ProductListView.as_view()),
    path('product/<int:pk>/', views.ProductDetailView.as_view()),
    path('order/', views.OrderListView.as_view()),
    path('order/<int:pk>/', views.OrderDetailView.as_view()),
    path('product-create/', views.CreateProduct.as_view())
]