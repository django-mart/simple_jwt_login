from django.conf.urls import url
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
    TokenVerifyView
)
from .views import Register, HelloWorld

urlpatterns = [
    url(r'^api/token$', TokenObtainPairView.as_view()),
    url(r'^api/verify$', TokenVerifyView.as_view()),
    url(r'^register$', Register.as_view()),
    url(r'^hello$', HelloWorld.as_view())
]