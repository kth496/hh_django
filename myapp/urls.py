from django.urls import include, path
from myapp.home import views as home_views

urlpatterns = [
    path(r'', home_views.index),
    path('', include('myapp.item.urls')),
]
