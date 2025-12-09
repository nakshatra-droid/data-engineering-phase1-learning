from django.contrib import admin
from django.urls import path
from ninja import NinjaAPI

api = NinjaAPI()


@api.get("/add")
def add(request, a: int, b: int) -> dict:
    return {"result": a + b}


urlpatterns = [
    path("admin/", admin.site.urls),
    path("", api.urls),
]