from django.urls import path
from myapp.item import views

urlpatterns = [
    path('products/', views.ProductList.as_view()),
    path('product/<int:pk>', views.ProductListWithMainId)
]
