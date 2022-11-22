from django.urls import path
from . import views

app_name = "cache"

urlpatterns = [
    path('', views.ProductListAPIView.as_view() , name="product")
]
