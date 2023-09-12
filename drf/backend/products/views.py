from rest_framework import authentication,generics,mixins,permissions
from .models import Product
from .serializers import ProductSerializer
from rest_framework.decorators import api_view
from rest_framework.response import Response
#from django.http import Http 404
from django.shortcuts import get_object_or_404



#list
class ProductListCreateAPIView(generics.ListCreateAPIView):
    queryset=Product.objects.all()
    serializer_class=ProductSerializer
    authentication_classes=[authentication.SessionAuthentication]
    permission_classes =[permissions.DjangoModelPermissions]

    def perform_create(self,serializer):
        # serializer.save(user=self.request.user)
        print(serializer.validated_data)
        title=serializer.validated_data.get('title')
        content=serializer.validated_data.get('content')
        None
        if content is None:
            content =title

        serializer.save(content=content)


# class ProductListAPIView(generics.ListAPIView):
#     """Not gonna use this method"""
#     queryset=Product.objects.all()
#     serializer_class=ProductSerializer

#detail view
class ProductDetailAPIView(generics.RetrieveAPIView):
    queryset= Product.objects.all()
    serializer_class=ProductSerializer
    #lookup_field ='pk'


#update
class ProductUpdateAPIView(generics.UpdateAPIView):
    queryset= Product.objects.all()
    serializer_class=ProductSerializer
    #lookup_field ='pk'


    def perform_update(self,serializer):
        #save the updated object
        instance=serializer.save()
        #check if the content field is empty
        if not instance.content:
            instance.content=instance.title

class ProductDestroyAPIView(generics.DestroyAPIView):
    queryset= Product.objects.all()
    serializer_class=ProductSerializer
    #lookup_field ='pk'

    def perform_delete(self,instance):
       super().perform_destroy(instance)

class ProductMixinView(
    mixins.CreateModelMixin,
    mixins.ListModelMixin,
    mixins.RetrieveModelMixin,
    generics.GenericAPIView
    ):

    queryset=Product.objects.all()
    serializer_class=ProductSerializer
    lookup_field ='pk'

    def get(self,request,*args, **kwargs):
        print(args,kwargs)
        pk=kwargs.get("pk")
        if pk is not None:
            return self.retrieve(request, *args, **kwargs)
        return self.list(request,*args,**kwargs)
    
    def post(self,request,*args,**kwargs):
        return self.create(request,*args,**kwargs) #createmixin provides create method
    
    def perform_create(self,serializer):
        # serializer.save(user=self.request.user)
        print(serializer.validated_data)
        title=serializer.validated_data.get('title')
        content=serializer.validated_data.get('content')
        None
        if content is None:
            content ="this is from createmixin"

        serializer.save(content=content)







@api_view(['GET','POST'])
def product_alt_view(request,pk=None,*args,**kwargs):
    method =request.method

    if method=="GET":
        if pk is not None:
            #detail view 
            obj=get_object_or_404(Product, pk=pk)
            data=ProductSerializer(obj, many=False).data 
            return Response(data)
        #list view
        queryset=Product.objects.all()
        data=ProductSerializer(queryset,many =True).data
        return Response(data)
    if method =="POST":
        serializer=ProductSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            title=serializer.validated_data.get('title')
            content=serializer.validated_data.get('content')
            None
            if content is None:
                content =title
            serializer.save(content=content)
            return Response(serializer.data)
        return Response({"invalid":"not good data"}, status=400)
    
