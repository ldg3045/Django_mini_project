from django.shortcuts import render,redirect
from sparta_furniture.models import SpartaFurniture
from sparta_furniture.foms import SpartaFurniture_Form, SpartaFurniture_UpdateForm


""" 변수 설정 구분

단일 객체 : furniture
복수 객체 : furniture_list


"""


# 생성
def market_create(request):
    if request.method == "POST": # POST 요청일 경우
        form = SpartaFurniture_Form(request.POST) # 폼 생성
        if form.is_valid(): # 폼이 유효한 경우
            furniture = form.save() # 폼 저장
            return redirect("market_info", furniture) # 수정 후 조회 페이지로 리다이렉트
    else: # GET 요청일 경우
        form = SpartaFurniture_Form() # 폼 생성
    
    context = {"form": form} # 폼과 이전 글 내용을 컨텍스트에 저장
    return render(request, "market_create.html", context) # GET 요청일 경우 폼과 이전 글 내용을 불러옴


# 조회
def market_info(request):
    if request.method == "GET":
        furniture_list = SpartaFurniture.objects.all() # 가구 리스트로 조회 후
        context = {"furniture_list": furniture_list} # 컨텍스트에 저장
        return render(request, "market_info.html", context)  # 조회 페이지로 이동


# 수정
def market_update(request, pk):  # 수정할 객체(pk) 조회
    furniture = SpartaFurniture.objects.get(pk=pk)  # 수정할 객체 조회
    
    if request.method == "POST": # POST 요청일 경우
        form = SpartaFurniture_UpdateForm(request.POST, instance=furniture) # instance=furniture : 이전 글 내용을 불러옴
        if form.is_valid(): # 폼이 유효한 경우
            form.save() # 폼 저장
            return redirect("market_info") # 수정 후 조회 페이지로 리다이렉트

    else: # GET 요청일 경우
        form = SpartaFurniture_UpdateForm(instance=furniture) # instance=furniture : 이전 글 내용을 불러옴

    context = {
         "form": form, 
         "furniture": furniture,
         } # 폼과 이전 글 내용을 컨텍스트에 저장
    return render(request, "market_update.html", context) # GET 요청일 경우 폼과 이전 글 내용을 불러옴


# 삭제          
def market_delete(request, pk):# 삭제할 객체(pk) 조회
    if request.method == "POST": # POST 요청일 경우
        furniture = SpartaFurniture.objects.get(pk=pk) # 삭제할 객체 조회
        furniture.delete() # 객체 삭제
    return redirect("market_info") # 삭제 후 조회 페이지로 리다이렉트


