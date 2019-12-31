from django.conf import settings
from django.contrib import admin
from django.urls import path, include
from .views import *
from django.conf.urls.static import static

urlpatterns = [
    path(r'accounts/login/', GalleryView.as_view()),
    path(r'register/', ContestantRegistrationView.as_view(), name='register'),
    path(r'gallery/', GalleryView.as_view(), name='gallery'),
    path(r'vote/<str:email>', VoteView.as_view(), name='vote'),
    path(r'oauth/', include('social_django.urls', namespace='social'))
]