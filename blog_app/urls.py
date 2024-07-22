from django.contrib import admin
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from blog_app.views import CategoryViewSet, SubCategoryViewSet, ProductViewSet, ExtraImageViewSet, OrderViewSet, PhoneViewSet, SocialMediaViewSet, ContactViewSet

router = DefaultRouter()
router.register(r'categories', CategoryViewSet)
router.register(r'subcategories', SubCategoryViewSet)
router.register(r'products', ProductViewSet)
router.register(r'extra-images', ExtraImageViewSet)
router.register(r'orders', OrderViewSet)
router.register(r'phones', PhoneViewSet)
router.register(r'social-medias', SocialMediaViewSet)
router.register(r'contacts', ContactViewSet)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include(router.urls)),
]
