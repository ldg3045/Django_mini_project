from django.shortcuts import render, redirect
from .models import Customer
from .forms import CustomerForm, Customer_UpdateForm


""" 변수 설정 구분

    profile = Customer 조회
    customer = pk 값이 있을 때

"""

# 회원 목록
def customer_list(request):
    if request.method == "GET":
        profile = Customer.objects.all()
        context = {"profile":profile }
        return render(request, "customer_list.html", context)
    return redirect("customers:customer_list")

# 회원 상세
def customer_detail(request, pk):
    if request.method == "GET":
        profile = Customer.objects.get(pk=pk)
        context = {"profile":profile }
        return render(request, "customer_detail.html", context)
    return redirect("market_info.html")

# 회원 가입
def customer_create(request):
    if request.method == "POST":
        profile = CustomerForm(request.POST)
        if profile.is_valid():
            profile.save()
            return redirect("customers:customer_list")
    else:  # GET 요청
        profile = CustomerForm()
    context = {"form": profile} 
    return render(request, "customer_create.html", context)

# 회원 수정
def customer_update(request, pk):
    customer = Customer.objects.get(pk=pk)
    if request.method == "POST":
        profile = Customer_UpdateForm(request.POST, instance=customer)
        if profile.is_valid():
            profile.save()
            return redirect("customers:customer_list")
    else:
        profile = Customer_UpdateForm(instance=customer)
    context = {
        "profile": profile,
        }
    return render(request, "customer_update.html", context)



# 회원 탈퇴
def customer_delete(request, pk):
    if request.method == "POST":
        customer = Customer.objects.get(pk=pk)
        customer.delete()
        return redirect("customers:customer_list")
    return redirect("customers:customer_list")

