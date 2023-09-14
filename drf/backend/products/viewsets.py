from rest_framework import viewsets

from .models import Product
from .serializers import ProductSerializer


class ProductViewSet(viewsets.ModelViewSet):

    queryset=Product.objects.all()
    serializer_class=ProductSerializer
    lookup_field='pk'

    '''
    get-> list -> Queryset
    get-> retrieve-> Product Instance Detail View
    post->create->New Instance
    put ->Update
    patch->Patial Update
    delete ->destroy
    '''