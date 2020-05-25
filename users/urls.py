from django.conf.urls import url
from .views import UserRegistrationView

urlpatterns = [
    url(r'^signup', UserRegistrationView.as_view()),
    ]