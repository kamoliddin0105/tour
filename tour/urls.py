from django.urls import path

from tour.views import TourListAPIView, TourDetailAPIView, TourCreateAPIView, TourUpdateAPIView, TourDeleteAPIView

urlpatterns = [
    path('',TourListAPIView.as_view(), name='tour-list'),
    path('<int:pk>/', TourDetailAPIView.as_view(), name='tour-detail'),
    path('create/', TourCreateAPIView.as_view(), name='tour-create'),
    path('<int:pk>/update/', TourUpdateAPIView.as_view(), name='tour-update'),
    path('<int:pk>/delete/', TourDeleteAPIView.as_view(), name='tour-delete'),
]