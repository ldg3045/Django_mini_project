from django import forms
from .models import SpartaFurniture

""" 코드 편집기 핵꿀팁 
- cntl + Tap : 누르면 원하는 스크립트 이동
- alt + 방향키 좌우 : 마지막 커서 위치 이동
- 가상환경 명령어 단축시키기 (다음에 해보기) : nano ~/.bashrc ◀ 구글링

""" 
# 정보 폼
class SpartaFurniture_Form(forms.ModelForm):
    class Meta: 
        model = SpartaFurniture # models.py의 클래스
        fields = ["sparta_furniture_id", # 마켓 아이디
                   "sparta_furniture_location", # 마켓 위치
                   "sparta_furniture_manager", # 마켓 관리자
                   "sparta_furniture_tel", # 마켓 전화번호
                   "sparta_staff_num", # 마켓 직원 수
            ]

        # 제외할 필드 : 마켓 오픈한 날짜 여부 제외
        exclude = ["sparta_furniture_open",
            ]

# 업데이트 폼
class SpartaFurniture_UpdateForm(forms.ModelForm): 
    class Meta: 
        model = SpartaFurniture # models.py의 클래스
        fields = [ "sparta_furniture_location", # 마켓 위치
                   "sparta_furniture_manager", # 마켓 관리자
                   "sparta_furniture_tel", # 마켓 전화번호
                   "sparta_staff_num", # 마켓 직원 수
            ]

        # 제외할 필드 : 마켓 오픈한 날짜 여부 제외
        exclude = ["sparta_furniture_open", # 오픈 날짜
                   "sparta_furniture_id", # 마켓 아이디
            ]