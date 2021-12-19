from django.urls import path
from . import views
from django.contrib.auth.views import LoginView, LogoutView

urlpatterns = [
	path('', views.store, name="store"),
	path('cart/', views.cart, name="cart"),
	path('checkout/', views.checkout, name="checkout"),
	path('update_item/', views.updateItem, name="update_item"),
	path('about/', views.about, name="about"),
	path('contact/', views.contact, name="contact"),
	path('checkout/success/', views.success, name="success"),
	path('login/', LoginView.as_view(template_name="store/login.html"), name="login"),
	path('logout/', LogoutView.as_view(), name="logout"),
	path('books/', views.books, name="books"),
	path('<int:obj_id>/product', views.product, name='product'),


]