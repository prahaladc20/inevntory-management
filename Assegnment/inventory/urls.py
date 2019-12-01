from django.urls import path, include
from rest_framework import routers
from . import views

from inventory.views import UserViewSet,HelloView
from django.conf.urls import url
from rest_framework.urlpatterns import format_suffix_patterns
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)

# from rest_framework_simplejwt import views as jwt_views

app_name = 'inventory'

# router = routers.DefaultRouter()
# router.register(r'users', views.UserViewSet)

router = routers.DefaultRouter()
router.register('users', UserViewSet)

urlpatterns = [
	path('', include(router.urls)),
	path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    path('api/login/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),

	# url(r'^auth/', ObtainAuthToken.as_view()),
    path('get/', views.InventoryList.as_view()),
    path('get/<int:pk>/', views.InventoryDetail.as_view()),
    path('home/', HelloView.as_view(), name='hello'),
]

# urlpatterns = format_suffix_patterns(urlpatterns)