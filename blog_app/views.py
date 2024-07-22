from rest_framework import viewsets
from .models import Category, SubCategory, Product, ExtraImage, Order, Phone, SocialMedia, Contact
from .serializer import CategorySerializer, SubCategorySerializer, ProductSerializer, ExtraImageSerializer, OrderSerializer, PhoneSerializer, SocialMediaSerializer, ContactSerializer

class CategoryViewSet(viewsets.ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer

class SubCategoryViewSet(viewsets.ModelViewSet):
    queryset = SubCategory.objects.all()
    serializer_class = SubCategorySerializer

class ProductViewSet(viewsets.ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

class ExtraImageViewSet(viewsets.ModelViewSet):
    queryset = ExtraImage.objects.all()
    serializer_class = ExtraImageSerializer

class OrderViewSet(viewsets.ModelViewSet):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer

class PhoneViewSet(viewsets.ModelViewSet):
    queryset = Phone.objects.all()
    serializer_class = PhoneSerializer

class SocialMediaViewSet(viewsets.ModelViewSet):
    queryset = SocialMedia.objects.all()
    serializer_class = SocialMediaSerializer

class ContactViewSet(viewsets.ModelViewSet):
    queryset = Contact.objects.all()
    serializer_class = ContactSerializer
