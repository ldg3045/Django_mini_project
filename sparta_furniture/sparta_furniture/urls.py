from django.contrib import admin
from django.urls import include, path
from . import views 


urlpatterns = [
    path("admin/", admin.site.urls),
    path("",views.market_info, name="market_info"),
    path("market_create/",views.market_create, name="market_create"),
    path("market_update/<str:pk>/",views.market_update, name="market_update"),
    path("market_delete/<str:pk>/",views.market_delete, name="market_delete"),
    path("customers/", include("customers.urls")),
    path("products/",include("products.urls")),
]
