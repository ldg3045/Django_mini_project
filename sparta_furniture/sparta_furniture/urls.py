from django.contrib import admin
from django.urls import include, path
from . import views 


urlpatterns = [
    path("admin/", admin.site.urls),
    path("market_create/",include("market_create.urls")),
    path("market_info/", include("market_info.urls")),
    path("market_update/",include("market_update.urls")),
    path("market_delete/",include("market_delete.urls")),
     
]
