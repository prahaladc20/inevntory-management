from django.urls import path, include
from rest_framework import routers
from . import views
from django.conf.urls import url
from rest_framework.urlpatterns import format_suffix_patterns
from rest_framework.authtoken.views import ObtainAuthToken

app_name = 'inventory'

router = routers.DefaultRouter()
# router.register(r'posts', views.BlogPostViewSet)
# router.register(r'get', views.InventoryViewSet,basename='Inventory')
# router.register(r'post', views.InventoryPostSet,basename='Inventory')
router.register(r'users', views.UserViewSet)

# urlpatterns = [
#     path(r'', include(router.urls)),
#     path(r'', views.index, name='index')
# ]


urlpatterns = [
	url(r'^', include(router.urls)),
	url(r'^auth/', ObtainAuthToken.as_view()),
    path('get/', views.InventoryList.as_view()),
    path('get/<int:pk>/', views.InventoryDetail.as_view()),
]

# urlpatterns = format_suffix_patterns(urlpatterns)