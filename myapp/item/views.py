from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import generics
from rest_framework import mixins
from django.http import Http404

# model 과 serializer 임포트
from myapp.item.models import Item
from myapp.item.serializers import ItemSerializer

# 페이지네이션 커스터마이징
from rest_framework.pagination import PageNumberPagination

class PageNumberPaginationDataOnly(PageNumberPagination):
    def get_paginated_response(self, data):
        return Response(data)


class ProductList(generics.ListAPIView):
    serializer_class = ItemSerializer
    pagination_class = PageNumberPaginationDataOnly

    def get_queryset(self, *args, **kwargs):
        # 필요한 데이터 초기화 initialize data
        queryset = Item.objects.all()
        givenPrameter = self.request.query_params
        
        # 필수사항 필터링 necessary filtering
        queryset = queryset.order_by('-' + givenPrameter['skin_type'] + 'Score', 'price') 
        
        # 선택사항 필터링 selective filtering
        if 'category' in givenPrameter:
            queryset = queryset.filter(category = givenPrameter['category'])

        if 'include_ingredient' in givenPrameter:
            myChoice = givenPrameter['include_ingredient'].split(',')
            for eachIngredient in myChoice:
                queryset = queryset.filter(ingredients__contains = eachIngredient)

        if 'exclude_ingredient' in givenPrameter:
            myChoice = givenPrameter['exclude_ingredient'].split(',')
            for eachIngredient in myChoice:
                queryset = queryset.exclude(ingredients__contains = eachIngredient)
        

        baseURL = "https://grepp-programmers-challenges.s3.ap-northeast-2.amazonaws.com/2020-birdview/thumbnail/"
        for e in queryset:
            # print(baseURL + e.imageId)
            e.imgUrl = baseURL + e.imageId
        return queryset


"""
클래스를 생성할 때 generics.ListAPIView 를 주는 것과 generics.GenericAPIView를 주는 등등의 차이는?
mixin 과의 차이가 무엇인지 잘 모르겠음

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