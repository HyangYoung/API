from django.urls import path, include
from rest_framework.routers import DefaultRouter
from . import views


router = DefaultRouter()
router.register('post', views.PostViewSet)
# router.urls

urlpatterns = [
    # path('mypost/<int:pk>', views.PublicPostListAPIView.as_view()),
    path('public/', views.public_post_list),
    path('', include(router.urls)),
]
