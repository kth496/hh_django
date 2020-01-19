from django.db import models

# 성분에 의한 피부타입 점수를 미리 계산했으므로 제품 정보만 DB에 올려서 사용한다
class Item(models.Model):
    id = models.IntegerField(primary_key=True)
    imageId = models.TextField()
    name = models.TextField()
    price = models.IntegerField()
    gender = models.CharField(max_length=8)
    category = models.CharField(max_length=20)
    ingredients = models.TextField()
    monthlySales = models.IntegerField()
    oilyScore = models.IntegerField()
    dryScore = models.IntegerField()
    sensitiveScore = models.IntegerField()

    class Meta:
        db_table = 'item_item'
