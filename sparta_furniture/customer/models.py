from django.db import models

# 고객
class Customer(models.Model):
    customer_id = models.CharField(max_length=50, primary_key= True) # 고객 id
    customer_name = models.CharField(max_length=50)                  # 고객 이름
    customer_create_at = models.DateField(auto_now_add=True)         # 고객 등록 날짜
    customer_tel = models.CharField(max_length=50)                   # 고객 전화번호