from django.urls import path, include

from . import views
from rest_framework import routers


router = routers.DefaultRouter()
router.register(r'links', views.UrlViewSet)

# Wire up our API using automatic URL routing.
# Additionally, we include login URLs for the browsable API.
urlpatterns = [
    path('', include(router.urls)),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework'))
]


# urlpatterns = [
#     path('index', views.index, name = 'index'),
#     path('create',views.create, name = 'create'),
#     path('<str:pk>', views.go, name='go')
# ] 