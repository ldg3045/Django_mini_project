from django.db import models
from sparta_furniture.models import SpartaFurniture

# 상품
class Product(models.Model):
    product_id = models.CharField(max_length=50, primary_key= True) # 상품 id / 질문 : 원래 기본키로 설정이 되는데 굳이 쓰는 이유?
    product_name = models.CharField(max_length=50)                  # 상품명
    product_price = models.IntegerField()                           # 가격
    product_stock = models.IntegerField()                           # 재고
    # 지점 아이디 - 포링키                                     ┌ 삭제시 = 자식 테이블도 삭제  ┌ 역참조 이름
    sparta_furniture_id = models.ForeignKey(SpartaFurniture, on_delete=models.CASCADE, related_name='product') # 외래키는 변수명이 같아야 함.