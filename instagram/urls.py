from django.urls import path, include
from rest_framework.routers import DefaultRouter
from . import views


router = DefaultRouter()
router.register('post', views.PostViewSet) # 2개의 url을 만들어줌.
# router.urls # list 형태로 urls 가 들어와 있음.

urlpatterns =[
    path('', include(router.urls)),
    path('get/', views.post_list),
    path('detail/<int:pk>/', views.post_detail),
]