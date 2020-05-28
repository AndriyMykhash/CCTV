from django.urls import path
from django.conf.urls import include
from rest_framework import routers
from record.views import RecordView

router = routers.SimpleRouter()
router.register(r'record', RecordView, basename='record')
urlpatterns = router.urls

urlpatterns += [
    path('api-auth/', include('rest_framework.urls')),
    path('api/', include('users.urls')),
]