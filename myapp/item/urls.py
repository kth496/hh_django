from django.urls import path
from myapp.item import views

urlpatterns = [
    path('products/', views.ProductList.as_view()),
    path('products/<int:pk>', views.ProductListWithId.as_view())
]
