from django.urls import path

from accounts.views import RegisterApiView, UserProfileAPIView

urlpatterns = [
    path('register/', RegisterApiView.as_view(), name='register'),
    path('profile/', UserProfileAPIView.as_view(), name='profile'),
    path('profile/update/', UserProfileAPIView.as_view(), name='update_profile'),
]
