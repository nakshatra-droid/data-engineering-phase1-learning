from django.contrib import admin
from django.urls import path
from ninja import NinjaAPI
from .schemas.add import AddRequest, AddResponse

api = NinjaAPI()


# @api.get("/add",response=AddResponse)
# def add(request, a: int, b: int) -> AddResponse:
#     return {"result": a + b}

@api.post("/add",response=AddResponse)
def add(request, payload:AddRequest) -> AddResponse:
    return {"result": payload.a + payload.b}


urlpatterns = [
    path("admin/", admin.site.urls),
    path("api/", api.urls),
]