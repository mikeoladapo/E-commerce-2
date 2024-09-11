from rest_framework.views import APIView
from .serializers import ProfileSerializer,ProductSerializer,CategorySerializer
from .models import Profile,Product,Category
from rest_framework.response import Response
from rest_framework import status

class ProfileList(APIView):
    def get(self,request):
        profiles = Profile.objects.all()
        serializer = ProfileSerializer(profiles,many=True)
        return Response(serializer.data)
    def post(self,request):
        serializer = ProfileSerializer(data=request.data,many=False)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status= status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class ProfileDetail(APIView):
    def get(self,request,pk):
        try:
            profile = Profile.objects.get(pk)
            serializer = ProfileSerializer(profile)
            return Response(serializer.data)
        except Profile.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)
        
    def put(self,request,pk):
        try:
            profile = Profile.objects.get(pk)
            serializer = ProfileSerializer(profile,data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data)
            return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
        except Profile.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)

    def delete(self,request,pk):
        try:
            profile = Profile.objects.get(pk)
            profile.delete()
            return Response(status=status.HTTP_204_NO_CONTENT)
        except Profile.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)

    
class CategoryList(APIView):
    def get(self,request):
            categorys = Category.objects.all()
            serializer = CategorySerializer(categorys,many=True)
            return Response(serializer.data)

    def post(self,request):
        serializer = CategorySerializer(data=request.data,many=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=status.HTTP_201_CREATED)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
    
class CategoryDetail(APIView):
    def get(self,request,pk):
        try:
            category = Category.objects.get(pk)
            serializer = CategorySerializer(category)
            return Response(serializer.data)
        except Category.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)
    def put(self,request,pk):
        try:
            category = Category.objects.get(pk)
            serializer = CategorySerializer(category,data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data)
            return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
        except Category.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)
    def delete(self,request,pk):
        try:
            category = Category.objects.get(pk)
            category.delete()
            return Response(status=status.HTTP_204_NO_CONTENT)
        except Category.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND) 
            
class ProductList(APIView):
    def get(self,request):
        products = Product.objects.all()
        serializer = ProductSerializer(products,many=True)
        return Response(serializer.data)
    def post(self,request):
        serializer = ProductSerializer(data=request.data,many=False)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status= status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class ProductDetail(APIView):
    def get(self,request,pk):
        try:
            product = Product.objects.get(pk)
            serializer = ProductSerializer(product)
            return Response(serializer.data)
        except Product.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)
    def put(self,request,pk):
        try:
            product = Product.objects.get(pk)
            serializer = ProductSerializer(product,data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data)
            return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
        except Product.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)
    def delete(self,request,pk):
        try:
            product = Product.objects.get(pk)
            product.delete()
            return Response(status=status.HTTP_204_NO_CONTENT)
        except Product.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)