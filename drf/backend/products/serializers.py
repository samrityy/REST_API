from rest_framework import serializers

from .models import Product

class ProductSerializer(serializers.ModelSerializer):
    my_discount=serializers.SerializerMethodField(read_only =True)
    class Meta:
        model=Product
        fields=[
            'title',
            'content',
            'price',
            'sale_price',
            'my_discount',
        ]
    def get_my_discount(self,obj):
        
        if not hasattr(obj, 'id'):  # hasattr check if obj has an attribute id
            return None
        if not isinstance(obj,Product):  #checks if obj is instance of Product
            return obj.get_discount()
        