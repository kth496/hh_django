from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework.views import APIView
from rest_framework import generics
from itertools import chain

# model 과 serializer 임포트
import myapp.item.models as ItemModels
from myapp.item.serializers import ItemSerializer
from myapp.item.serializers import DetailPageModelMainSerializer
from myapp.item.serializers import DetailPageModelSubSerializer

# 페이지네이션 
from rest_framework.pagination import PageNumberPagination
class PageNumberPaginationDataOnly(PageNumberPagination):
    def get_paginated_response(self, data):
        return Response(data)


class ProductList(generics.ListAPIView):
    # 시리얼라이저와 페이지네이션 설정
    serializer_class = ItemSerializer
    pagination_class = PageNumberPaginationDataOnly

    def get_queryset(self, *args, **kwargs):
        # 필요한 데이터 초기화 initialize data
        queryset = ItemModels.Item.objects.all()
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
        
        return queryset


# 서로 다른 형태의 데이터를 조합해서 보내기위해 부득이하게 함수형으로 view 작성
@api_view(['GET'])
def ProductListWithMainId(request, pk):
    if request.method == 'GET':
        # 주어진 ID값을 pk로 필터링, 서브로 주어지는 3개 데이터는 요구사항에 맞게 필터링
        mainItem = ItemModels.Item.objects.filter(id = pk)
        subList = ItemModels.Item.objects.all().order_by('-' + request.query_params['skin_type'] + 'Score', 'price')[:3]

        # Response의 형태가 다르기 때문에 각 데이터에 맞는 시리얼라이저를 따로 만들어서 사용
        mainSerializer =  DetailPageModelMainSerializer(mainItem, many=True)
        subSerializer = DetailPageModelSubSerializer(subList, many=True)

        # 구한 데이터를 합쳐서 리턴
        return Response(mainSerializer.data + subSerializer.data)
