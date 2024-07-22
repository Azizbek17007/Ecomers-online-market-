from rest_framework import serializers
from .models import Category, SubCategory, Product, ExtraImage, Order, Phone, SocialMedia, Contact

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ['id', 'name', 'image', 'created_at', 'updated_at']

class SubCategorySerializer(serializers.ModelSerializer):
    category = CategorySerializer()

    class Meta:
        model = SubCategory
        fields = ['id', 'name', 'image', 'created_at', 'updated_at', 'category']

class ExtraImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = ExtraImage
        fields = ['id', 'image', 'product']

class ProductSerializer(serializers.ModelSerializer):
    subcategory = SubCategorySerializer()
    extra_images = ExtraImageSerializer(many=True, read_only=True)

    class Meta:
        model = Product
        fields = ['id', 'name', 'image', 'price', 'description', 'category', 'phone', 'subcategory', 'extra_images']

class OrderSerializer(serializers.ModelSerializer):
    product = ProductSerializer()

    class Meta:
        model = Order
        fields = ['id', 'name', 'phone', 'product']

class PhoneSerializer(serializers.ModelSerializer):
    class Meta:
        model = Phone
        fields = ['id', 'number']

class SocialMediaSerializer(serializers.ModelSerializer):
    class Meta:
        model = SocialMedia
        fields = ['id', 'link']

class ContactSerializer(serializers.ModelSerializer):
    phone = PhoneSerializer()
    links = SocialMediaSerializer(many=True)

    class Meta:
        model = Contact
        fields = ['id', 'phone', 'links', 'address', 'created_at', 'updated_at']
