from django import forms
from .models import SpartaFurniture

""" 코드 편집기 핵꿀팁 
- cntl + Tap : 누르면 원하는 스크립트 이동
- alt + 방향키 좌우 : 마지막 커서 위치 이동
- 가상환경 명령어 단축시키기 (다음에 해보기) : nano ~/.bashrc ◀ 구글링

""" 
#
class SpartaFurniture_Form(forms.ModelForm):
    class Meta: 
        model = SpartaFurniture
        fields = ["sparta_furniture_id",
                   "sparta_furniture_location",
                   "sparta_furniture_manage",
                   "sparta_furniture_tel",
                   "sparta_furniture_open",
                   "sparta_staff_num",

                ]
 