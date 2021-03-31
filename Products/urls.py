from django.urls import path
from Products import views as Product_views

urlpatterns = [
    path('', Product_views.HomeListView.as_view(), name='home'),
    path('category', Product_views.CategoryListView.as_view(), name='category'),
    path('category/<int:id>/products', Product_views.CategoryByProductsView, name='category-by-products'),
    path('products', Product_views.ProductListView.as_view(), name='products'),
    path('products/<int:pk>/product-detail', Product_views.ProductDetailView.as_view(), name='product-detail'),
    path('My-Orders', Product_views.OrderListView.as_view(), name='my-orders'),
    path('My-Wishlist', Product_views.Wishlist, name='my-wishlist'),
    path('cart', Product_views.cart, name='cart'),
    path('deleteCart/<int:id>', Product_views.DeleteItem, name='delete-item'),
    path('deleteWishlist/<int:id>', Product_views.DeleteWishlist, name='delete-wishlist'),
]