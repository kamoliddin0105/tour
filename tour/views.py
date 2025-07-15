from rest_framework import permissions, status
from rest_framework.response import Response
from rest_framework.views import APIView

from tour.models import Tour
from tour.serializers import TourSerializer


class TourListAPIView(APIView):
    permission_classes = [permissions.AllowAny]

    def get(self, request):
        tours = Tour.objects.all()
        serializer = TourSerializer(tours, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)


class TourDetailAPIView(APIView):
    permission_classes = [permissions.AllowAny]

    def get(self, request, pk):
        try:
            tour = Tour.objects.get(pk=pk)
        except Tour.DoesNotExist:
            return Response({'error': 'Tur topilmadi'}, status=status.HTTP_404_NOT_FOUND)
        serializer = TourSerializer(tour)
        return Response(serializer.data)


class TourCreateAPIView(APIView):
    permission_classes = [permissions.IsAdminUser]

    def post(self, request):
        serializer = TourSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class TourUpdateAPIView(APIView):
    permission_classes = [permissions.IsAdminUser]

    def put(self, request, pk):
        try:
            tour = Tour.objects.get(pk=pk)
        except Tour.DoesNotExist:
            return Response({'error': 'Tur topilmadi'}, status=status.HTTP_404_NOT_FOUND)
        serializer = TourSerializer(tour, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class TourDeleteAPIView(APIView):
    permission_classes = [permissions.IsAdminUser]

    def delete(self, request, pk):
        try:
            tour = Tour.objects.get(pk=pk)
        except Tour.DoesNotExist:
            return Response({'error': 'Tur topilmadi'}, status=status.HTTP_404_NOT_FOUND)
        tour.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
