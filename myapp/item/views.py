from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import generics
from rest_framework import mixins
from django.http import Http404

# model 과 serializer 임포트
from myapp.item.models import Item
from myapp.item.serializers import ItemSerializer

# 페이지네이션 
from rest_framework.pagination import PageNumberPagination

# 필터
from rest_framework import filters
from django_filters.rest_framework import DjangoFilterBackend



"""
# 성분을 제외하고 싶다면 다음과 같이 쓴다.
SELECT ...
WHERE NOT pub_date > '2005-1-3'
AND NOT headline = 'Hello'

위 쿼리문을 다음과 같이 쓸 수 있다. exclude를 반복하면 된다.
Entry.objects.exclude(pub_date__gt=datetime.date(2005, 1, 3)).exclude(headline='Hello')

"""

class ProductList(generics.ListAPIView):
    queryset = Item.objects.all()
    serializer_class = ItemSerializer
    pagination_class = PageNumberPagination
    
    filter_backends = [DjangoFilterBackend, filters.OrderingFilter]
    filterset_fields = ['category']
    ordering_fields = ['id']


    def get_queryset(self, *args, **kwargs):
        return self.queryset
    

"""
클래스를 생성할 때 generics.ListAPIView 를 주는 것과 generics.GenericAPIView를 주는 등등의 차이는?
mixin 과의 차이가 무엇인지도 잘 모르겠음

OrderingFilter 를 사용했음에도 UnorderedObjectListWarning 발생함

"""

"""
참고자료
1. 필터링 관련 블로그 자료, 잘 작동은 안됨 GenericViewSet을 사용함
https://show-me-the-money.tistory.com/42

2. 필터링 관련 블로그 자료 2, 여기가 그나마 나음, 이 블로그에서 사용한 쿼리를 몰라서 100%활용은 불가
https://uiandwe.tistory.com/1156

3. DRF Filtering 공식문서
https://www.django-rest-framework.org/api-guide/filtering/#setting-filter-backends

"""