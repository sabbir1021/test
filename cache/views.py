from rest_framework.views import APIView
from .models import Product
from .serializers import ProductSerializer
from django.core.cache import cache
from rest_framework.generics import ListAPIView
from rest_framework.permissions import IsAuthenticated
from .permissions import HasRequiredPermissionForMethod

# Create your views here.

class ProductListAPIView(ListAPIView):
    permission_classes = (HasRequiredPermissionForMethod,)
    serializer_class = ProductSerializer
    queryset = Product.objects.all()
    search_fields = ['name','detials']
    permission_required = ["cache.view_product"]