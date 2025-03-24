from django.db import models

""" 각 Field 설명
models.Model : 장고에서 제공하는 모델 클래스
 - .대문자 : 클래스 변수
 - 소문자 : 인스턴스 변수(임의로 지정)

1. CharField(캐릭터필드):
- 짧은 문자열을 저장 (최대 길이 지정)

2. TextField(텍스트필드):
- 긴 문자열을 저장 (길이 제한 없음)

3. IntegerField(인티저필드):
- 정수를 저장

4. FloatField(플롯필드):
- 부동 소수점 숫자를 저장

5. BooleanField(부울필드):
- True 또는 False 값을 저장

6. DateField(데이트필드):
- 날짜를 저장 (연도, 월, 일)

7. DateTimeField(데이트타임필드):
- 날짜와 시간을 저장

8. EmailField(이메일필드):
- 이메일 주소를 저장 (유효성 검사 포함)

9. URLField(유알엘필드):
- URL을 저장 (유효성 검사 포함)

10. FileField(파일필드):
- 파일 업로드를 위한 필드

11. ImageField(이미지필드):
- 이미지 파일 업로드를 위한 필드

12. ForeignKey(포린키):
- 다른 모델과의 관계를 정의 (1:N 관계)

13. ManyToManyField(메니투메니필드):
- 다대다 관계를 정의

14. OneToOneField(원투원필드):
- 일대일 관계를 정의

"""

# 스파르타 가구판매점
class SpartaFurniture(models.Model):
    sparta_furniture_id = models.CharField(max_length=50, primary_key= True) # 지점 id / PK
    sparta_furniture_location = models.CharField(max_length=50)              # 지점 위치
    sparta_furniture_manager = models.CharField(max_length=50)               # 지점장
    sparta_furniture_tel = models.CharField(max_length=50)                   # 지점 전화번호
    sparta_furniture_open = models.DateField(auto_now_add=True)              # 개점 날짜
    """                                         └> 마이그레이션 터미널 주석
    auto_now_add : 최초에 추가 될 때 자동으로 시간 추가

    > 마이그레이션 하면 터미널 창에 문구가 뜬다 !

    옵션 1) 하나의 디폴트 값을 주면 그걸로 다 셋팅할래? [Y]
    옵션 2) 나가서 직접 디폴트 값을 세팅할래? [N]

    Y > Enter 누르면 현재 시간으로 셋팅해줄게, 아니면 값 입력해줘.

    """ 
    sparta_staff_num = models.IntegerField()                                 # 총 직원 수
    



