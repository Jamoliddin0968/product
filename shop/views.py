from rest_framework.generics import ListAPIView
from rest_framework.response import Response
from rest_framework.serializers import ModelSerializer
from rest_framework.views import APIView

from .models import Product


class hello(APIView):
    def get(self, request):
        return Response({"hello": "world"})


class ProductSerializer(ModelSerializer):
    class Meta:
        model = Product
        fields = "__all__"


class ProductList(ListAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
