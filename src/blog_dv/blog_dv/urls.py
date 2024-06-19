from article import views
from common.views import CommentViewSet
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import include, path
# from jwt_token.views import CustomTokenObtainPairView, CustomTokenRefreshView
from rest_framework.routers import DefaultRouter
from user_info.views import UserViewSet

router = DefaultRouter()
router.register(r"article", views.ArticleViewSet)
router.register(r"category", views.CategoryViewSet)
router.register(r"tag", views.TagViewSet)
router.register(r"avatar", views.AvatarViewSet)
router.register(r"comment", CommentViewSet)
router.register(r"user", UserViewSet)

urlpatterns = [
    path("admin/", admin.site.urls),
    path("api-auth/", include("rest_framework.urls")),
    path("api/", include(router.urls)),
    # path("api/token/",
    #      CustomTokenObtainPairView.as_view(),
    #      name="token_obtain_pair"),
    # path("api/token/refresh/",
    #      CustomTokenRefreshView.as_view(),
    #      name="token_refresh"),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT)
