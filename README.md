# Django_mini_project

<br>

## 1일 차, 프로젝트 생성 및 설정

1. 가상환경 활성 및 패키지 설치
2. requirements.txt 파일 생성
3. sparta_furniture 프로젝트 생성
4. apps 생성
   - sparta_furniture : 스파르타 가구판매점(메인 앱)
   - customer : 고객 앱
   - product : 상품 앱

5. git 레포지토리 연동

<br>


## 2일 차, 모델 생성

1. models.py 파일 생성
   - SpartaFurniture 모델
   - Customer 모델
   - Product 모델

2. 마이그레이션 적용
   - sparta_furniture : 스파르타 가구판매점(메인 앱)
   - customers : 고객 앱
   - products : 상품 앱
   > customer와 product 앱의 이름을 구별하기 쉽게 복수형`'s'`로 수정


<br>

## 3일 차, 폼 생성 및 CRUD 구현

1. foms.py 파일 생성 후, 모델 폼 생성
- SpartaFurniture_Form 클래스
   - model.py에 있는 SpartaFurniture 모델
     - 지점 id
     - 지점 위치
     - 지점장
     - 지점 전화번호
     - 개점 날짜
     - 총 직원 수



2. views.py 파일에 CRUD 구현

   - Create(생성) : market_create(생성) 
   - Read(조회) : market_info(조회)
   - Update(수정) : market_update(수정)
   - Delete(삭제) : market_delete(삭제)

> view 함수의 각 변수명을 `furniture`로 설정함.
> ⛔ Read(조회)는 여러 목록을 조회하는 복수형 객체이기 때문에 변수명을 `furniture_list`로 설정함.

3. 나머지 app들도 동일하게 적용(4일 차에 추가 예정)

<br>


## 4일 차, template과 url 생성 및 테스트

1. template 파일 생성 및 구성
   - base.html: 공통 레이아웃 템플릿
   - 각 앱별 템플릿 구성:
     - sparta_furniture
       - market_list.html: 지점 목록 페이지
       - market_detail.html: 지점 상세 정보 페이지
       - market_form.html: 지점 생성/수정 폼 페이지
       - market_confirm_delete.html: 지점 삭제 확인 페이지
     - customers
       - customer_list.html: 고객 목록 페이지
       - customer_detail.html: 고객 상세 정보 페이지
       - customer_form.html: 고객 생성/수정 폼 페이지
       - customer_confirm_delete.html: 고객 삭제 확인 페이지
     - products
       - product_list.html: 상품 목록 페이지
       - product_detail.html: 상품 상세 정보 페이지
       - product_form.html: 상품 생성/수정 폼 페이지
       - product_confirm_delete.html: 상품 삭제 확인 페이지

2. URL 패턴 설정
   - urls.py 파일 설정
     - 프로젝트 메인 urls.py: 각 앱으로 라우팅
     - 각 앱별 urls.py 생성 및 설정:
       - sparta_furniture/urls.py
       - customers/urls.py
       - products/urls.py

3. CRUD 기능 테스트
   - 각 모델별 CRUD 기능 테스트 진행
     - 지점 생성, 조회, 수정, 삭제 기능
     - 고객 생성, 조회, 수정, 삭제 기능
     - 상품 생성, 조회, 수정, 삭제 기능

<br>

## 5일 차, 추가 기능 구현 및 디자인 개선

1. 사용자 인증 기능 구현
   - 로그인/로그아웃 기능
   - 사용자 권한에 따른 접근 제어

2. 검색 기능 구현
   - 지점, 고객, 상품 검색 기능
   - 필터링 옵션 추가

3. 페이지네이션 구현
   - 목록 페이지에 페이지네이션 추가
   - 페이지당 항목 수 조절 기능

4. 디자인 및 UI 개선
   - Bootstrap 프레임워크 적용
   - 반응형 디자인 구현
   - 사용자 경험(UX) 개선

<br>

## 6일 차, 테스트 및 배포 준비

1. 단위 테스트 작성
   - 모델 테스트
   - 뷰 테스트
   - 폼 테스트

2. 통합 테스트 진행
   - 기능 간 상호작용 테스트
   - 사용자 흐름 테스트

3. 버그 수정
   - 발견된 오류 수정
   - 코드 리팩토링

4. 배포 준비
   - 배포 설정 구성
   - 정적 파일 최적화
   - 보안 설정 점검

<br>

## 7일 차, 최종 점검 및 프로젝트 마무리

1. 최종 테스트
   - 전체 기능 테스트
   - 성능 테스트
   - 크로스 브라우저 테스트

2. 문서화
   - API 문서 작성
   - 사용자 매뉴얼 작성
   - 설치 및 배포 가이드 작성

3. 프로젝트 발표 준비
   - 발표 자료 작성
   - 시연 시나리오 준비

4. 회고 및 향후 계획
   - 프로젝트 회고
   - 개선점 도출
   - 향후 개발 계획 수립








