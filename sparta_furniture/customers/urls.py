from django.urls import path
from . import views

app_name = "customers"
urlpatterns = [         # <str:pk> 랑 <str:customer_id> 랑 같다.
    path("customer_list/", views.customer_list, name="customer_list"),
    path("customer_create/", views.customer_create, name= "customer_create"),
    path("customer_update/<str:pk>/",views.customer_update, name= "customer_update"),
    path("customer_detail/<str:pk>/",views.customer_detail, name= "customer_detail"),
    path("customer_delete/<str:pk>/",views.customer_delete, name="customer_delete"),


]
