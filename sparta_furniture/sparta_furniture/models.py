from django.db import models

# 스파르타 가구판매점
class SpartaFurniture(models.Model):
    sparta_furniture_id = models.CharField(max_length=50, primary_key= True) # 지점 id
    sparta_furniture_location = models.CharField(max_length=50)              # 지점 위치
    sparta_furniture_manager = models.CharField(max_length=50)               # 지점장
    sparta_furniture_tel = models.CharField(max_length=50)                   # 지점 전화번호
    sparta_furniture_open = models.DateField(auto_now_add=True)              # 개점 날짜
    sparta_staff_num = models.IntegerField()                                 # 총 직원 수
    



