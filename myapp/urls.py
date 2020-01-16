from django.urls import include, path
from rest_framework import routers
from django.contrib import admin

# view 파일 임포트
from myapp.home import views as home_views
from myapp.item import views as item_views

# 라우터 및 URL 설정
router = routers.DefaultRouter()
router.register(r'users', item_views.UserViewSet)
router.register(r'groups', item_views.GroupViewSet)

urlpatterns = [
    path('admin/', admin.site.urls),
    path(r'', home_views.index),
    path('', include(router.urls)),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework'))
]
