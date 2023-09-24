from django.urls import path, include
from rest_framework.routers import DefaultRouter
from Task import views

router = DefaultRouter()
router.register(r'authors', views.AuthorViewSet)
router.register(r'magazines', views.MagazineViewSet)
router.register(r'articles', views.ArticleViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path("api/", include("Task.swagger")),
]
