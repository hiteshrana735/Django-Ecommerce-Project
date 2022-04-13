from django.shortcuts import get_object_or_404
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import Cart
from .serializers import CartSerializer
from rest_framework import status

# Create your views here.
class CartAPI(APIView):
    def post(self, request):
        serializer = CartSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({"status" : "Success", "data" : serializer.data}, status=status.HTTP_200_OK)
        else:
            return Response({"status" : "Error", "data" : serializer.errors}, status=status.HTTP_400_BAD_REQUEST)

    def get(self, request, id=None):
        if id:
            item = Cart.objects.get(id=id)
            serializer = CartSerializer(item)
            return Response({"status": "Success", "data" : serializer.data}, status=status.HTTP_200_OK)
        else:
            items = Cart.objects.all()
            serializer = CartSerializer(items, many=True)
            return Response({"status" : "Success", "data": serializer.data}, status=status.HTTP_200_OK)

    def patch(self, request, id=None):
        item = Cart.objects.get(id=id)
        serializer = CartSerializer(item, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response({"status" : "Success", "data" : serializer.data})
        else:
            return Response({"status" : "Error Occured", "data" : serializer.errors})

    def delete(self, request, id=None):
        item = get_object_or_404(Cart, id=id)
        item.delete()
        return Response({"status": "Success", "data" : "Item Deleted"})