from django.urls import path 
from .views import ProfileList,ProfileDetail,CategoryList,CategoryDetail,ProductDetail,ProductList

urlpatterns = [
    path('Profile',ProfileList.as_view(),name='Profile-list'),
    path('Profile/<str:pk>',ProfileDetail.as_view(),name='Profile-detail'),
    path('Category',CategoryList.as_view(),name='Category-list'),
    path('Category/<str:pk>',CategoryDetail.as_view(),name='Category-detail'),
    path('Product',ProductList.as_view(),name='Product-list'),
    path('Product/<str:pk>',ProductDetail.as_view(),name='Product-list'),
]
