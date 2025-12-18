from django.urls import path
from users import views as UserViews
from rest_framework_simplejwt.views import TokenObtainPairView,TokenRefreshView
from products import views as ProductViews
from carts import views as CartViews
from orders import views as OrderViews

urlpatterns = [
    #User URLs
    path('register/',UserViews.RegisterView.as_view()),
    path('profile/',UserViews.ProfileView.as_view()),
    path('token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),

    #Product URLs
    path('products/',ProductViews.ProductListView.as_view()),
    path('product/<int:pk>',ProductViews.ProductDetailsView.as_view()),

    #Cart URLs
    path('cart/',CartViews.CartView.as_view()),
    path('cart/add/',CartViews.AddToCartView.as_view()),
    path('cart/items/<int:item_id>/',CartViews.ManageCartItemView.as_view()),

    #Orders URLs
    path('orders/place/',OrderViews.PlaceOrderView.as_view()),
    path('orders/',OrderViews.OrdersView.as_view()),
    path('orders/<int:pk>/',OrderViews.OrderDetailsView.as_view())
]