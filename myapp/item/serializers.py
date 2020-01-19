from .models import *
from django.contrib.auth.models import User, Group
from rest_framework import serializers

# 요구사항에서 제시하는 API Response는 전체적으로 매우 흡사하며 디테일한 부분에서 약간의 차이만 존재함
# 따라서 하나의 아이템 시리얼라이저 클래스를 만들고 이를 상속받아 필드구성 및 필요한 변수만 일부분 수정하는 방식으로 구현

class ItemSerializer(serializers.ModelSerializer):
    imgUrl = serializers.SerializerMethodField()
    baseURL = "https://grepp-programmers-challenges.s3.ap-northeast-2.amazonaws.com/2020-birdview/"
    folderName = "thumbnail/"

    def get_imgUrl(self, obj):
        return self.baseURL + self.folderName + obj.imageId + '.jpg'

    class Meta:
        model = Item
        fields = ['id', 'imgUrl', 'name', 'price', 'ingredients', 'monthlySales']


class DetailPageModelMainSerializer(ItemSerializer):
    folderName = "image/"
    class Meta(ItemSerializer.Meta):
        fields = ['id', 'imgUrl', 'name', 'price', 'gender', 'category', 'ingredients', 'monthlySales']


class DetailPageModelSubSerializer(ItemSerializer):
    class Meta(ItemSerializer.Meta):
        fields = ['id', 'imgUrl', 'name', 'price']