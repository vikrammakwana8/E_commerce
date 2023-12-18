from rest_framework import serializers
from .models import Customer, Product, Order, OrderItem
from django.utils import timezone

class CustomerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Customer
        fields = '__all__'

    def validate_name(self, value):
        if Customer.objects.filter(name=value).exists():
            raise serializers.ValidationError("Customer name already exists.")
        return value

class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = '__all__'

    def validate_name(self, value):
        if Product.objects.filter(name=value).exists():
            raise serializers.ValidationError("Product name already exists.")
        return value

    def validate_weight(self, value):
        if value <= 0 or value > 25:
            raise serializers.ValidationError("Weight must be 0< or >25 kg")
        return value

class OrderItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = OrderItem
        fields = '__all__'

class OrderSerializer(serializers.ModelSerializer):
    order_item = OrderItemSerializer(many=True)

    class Meta:
        model = Order
        fields = '__all__'

    def validate_order_date(self, value):
        if value < timezone.now().date():
            raise serializers.ValidationError("Order Date can't be in the past.")
        return value

    def validate(self, data):
        order_items = data.get('order_item', [])



        individual_weights = []

      
        for i in order_items:
            
            iteam_weight = i['product'].weight * i['quantity']
            individual_weights.append(iteam_weight)

        
        total_weight = sum(individual_weights)


        
        if total_weight > 150:
            raise serializers.ValidationError("Order weight must be under 150kg.")
        return data
