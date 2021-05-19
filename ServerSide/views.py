from django.views.decorators.csrf import csrf_exempt
from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from rest_framework.parsers import JSONParser
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from rest_framework.views import APIView 
from rest_framework import generics
from rest_framework import mixins
from rest_framework.authentication import BaseAuthentication, SessionAuthentication, TokenAuthentication
from rest_framework.permissions import IsAuthenticated

from .serializers import StationsSerializer,CustomersSerializer, ItemsSerializer, PaymentsSerializer
from .models import Stations,Customers, Items, Payments



# Create your views here.

class GenericAPIView(generics.GenericAPIView, mixins.ListModelMixin, mixins.CreateModelMixin, mixins.UpdateModelMixin, mixins.RetrieveModelMixin, mixins.DestroyModelMixin):
    serializer_class = StationsSerializer
    queryset = Stations.objects.all()
    lookup_field = 'id'

    # authentication_class = [SessionAuthentication, BaseAuthentication, TokenAuthentication]
    authentication_class = [TokenAuthentication]
    permission_classes = [IsAuthenticated]

    def get(self, request, id = None): 
        if id:
            return self.retrieve(request)
        else:
            return self.list(request)
    
    def post(self, request):
        return self.create(request)
    
    def put(self, request, id=None):
        return self.update(request, id)
        
    def delete(self, request, id):
        return self.destroy(request, id)

# Stations,Customers, Items, Payments
class StationsAPIView(generics.GenericAPIView, mixins.ListModelMixin, mixins.CreateModelMixin, mixins.UpdateModelMixin, mixins.RetrieveModelMixin, mixins.DestroyModelMixin):
    serializer_class = StationsSerializer
    queryset = Stations.objects.all()
    lookup_field = 'id'

    # authentication_class = [SessionAuthentication, BaseAuthentication, TokenAuthentication]
    authentication_class = [TokenAuthentication]
    permission_classes = [IsAuthenticated]

    def get(self, request, id = None): 
        if id:
            return self.retrieve(request)
        else:
            return self.list(request)
    
    def post(self, request):
        return self.create(request)
    
    def put(self, request, id=None):
        return self.update(request, id)
        
    def delete(self, request, id):
        return self.destroy(request, id)


class CustomersAPIView(generics.GenericAPIView, mixins.ListModelMixin, mixins.CreateModelMixin, mixins.UpdateModelMixin, mixins.RetrieveModelMixin, mixins.DestroyModelMixin):
    serializer_class = CustomersSerializer
    queryset = Customers.objects.all()
    lookup_field = 'id'

    # authentication_class = [SessionAuthentication, BaseAuthentication, TokenAuthentication]
    authentication_class = [TokenAuthentication]
    permission_classes = [IsAuthenticated]

    def get(self, request, id = None): 
        if id:
            return self.retrieve(request)
        else:
            return self.list(request)
    
    def post(self, request):
        return self.create(request)
    
    def put(self, request, id=None):
        return self.update(request, id)
        
    def delete(self, request, id):
        return self.destroy(request, id)

class ItemsAPIView(generics.GenericAPIView, mixins.ListModelMixin, mixins.CreateModelMixin, mixins.UpdateModelMixin, mixins.RetrieveModelMixin, mixins.DestroyModelMixin):
    serializer_class = ItemsSerializer
    queryset = Items.objects.all()
    lookup_field = 'id'

    # authentication_class = [SessionAuthentication, BaseAuthentication, TokenAuthentication]
    authentication_class = [TokenAuthentication]
    permission_classes = [IsAuthenticated]

    def get(self, request, id = None): 
        if id:
            return self.retrieve(request)
        else:
            return self.list(request)
    
    def post(self, request):
        return self.create(request)
    
    def put(self, request, id=None):
        return self.update(request, id)
        
    def delete(self, request, id):
        return self.destroy(request, id)

class PaymentsAPIView(generics.GenericAPIView, mixins.ListModelMixin, mixins.CreateModelMixin, mixins.UpdateModelMixin, mixins.RetrieveModelMixin, mixins.DestroyModelMixin):
    serializer_class = PaymentsSerializer
    queryset = Payments.objects.all()
    lookup_field = 'id'

    # authentication_class = [SessionAuthentication, BaseAuthentication, TokenAuthentication]
    authentication_class = [TokenAuthentication]
    permission_classes = [IsAuthenticated]

    def get(self, request, id = None): 
        if id:
            return self.retrieve(request)
        else:
            return self.list(request)
    
    def post(self, request):
        return self.create(request)
    
    def put(self, request, id=None):
        return self.update(request, id)
        
    def delete(self, request, id):
        return self.destroy(request, id)
    


# # @api_view(['GET','POST'])
# class ArticlesMain(APIView):

#     def get(self, request):
#         articles = Article.objects.all()
#         serializer = ArticleSerializer(articles, many=True)
#         return Response(serializer.data)

#     def post(self, request):
#         serializer = ArticleSerializer(data=request.data) 
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data, status=status.HTTP_201_CREATED)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
# # @api_view(['GET','PUT','DELETE']) 
# class ArticleDetail(APIView):

#     def get_object(self, id):
#         try:
#             return Article.objects.get(id=id)        
#         except Article.DoesNotExist:
#             return HttpResponse(status=status.HTTP_404_NOT_FOUND)
    
#     def get(self, request, id):
#         article = self.get_object(id)
#         serializer = ArticleSerializer(article)
#         return Response(serializer.data)
    
#     def put(self, request, id):
#         article = self.get_object(id)
#         serializer = ArticleSerializer(article, data=request.data) 
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
#     def delete(self, request, id):
#         article = self.get_object(id)
#         article.delete()
#         return Response(status=status.HTTP_204_NO_CONTENT)

# # Only for postman testing exempt csrf_toke
# @api_view(['GET','POST'])
# def articles_data(request):

#     if request.method =='GET':
#         articles = Article.objects.all()
#         serializer = ArticleSerializer(articles, many=True)
#         return Response(serializer.data)

#     elif request.method =='POST': 

#         serializer = ArticleSerializer(data=request.data) 
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data, status=status.HTTP_201_CREATED)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
# @csrf_exempt
# def article_detail(request, pk):
#     try:
#          article = Article.objects.get(pk=pk)
#     except Article.DoesNotExist:
#         return HttpResponse(status=404)

#     if request.method == 'GET':
#         serializer = ArticleSerializer(article)
#         return JsonResponse(serializer.data)

#     elif request.method == 'PUT':
#         data = JSONParser().parse(request)
#         serializer = ArticleSerializer(article, data=data) 
#         if serializer.is_valid():
#             serializer.save()
#             return JsonResponse(serializer.data)
#         return JsonResponse(serializer.errors, status=400)


#     elif request.method == 'DELETE':
#         article.delete()
#         return HttpResponse(status=204 )


    

 
