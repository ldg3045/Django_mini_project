from django.db import models
from sparta_furniture.models import SpartaFurniture

# 상품
class Product(models.Model):
    product_id = models.CharField(max_length=50, primary_key= True) # 상품 id
    product_name = models.CharField(max_length=50)                  # 상품명
    product_price = models.IntegerField()                           # 가격
    product_stock = models.IntegerField()                           # 재고
    # 지점 아이디 - 포링키
    sparta_furniture_id = models.ForeignKey(SpartaFurniture, on_delete=models.CASCADE, related_name='product')