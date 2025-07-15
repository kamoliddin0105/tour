from rest_framework import permissions, status
from rest_framework.response import Response
from rest_framework.views import APIView

from bookings.models import Booking
from bookings.permissions import IsOwnerOrAdmin
from bookings.serializers import BookingSerializer


class BookingListCreateAPIView(APIView):
    permission_classes = [permissions.IsAuthenticated]

    def get(self, request):
        if request.user.is_staff:
            bookings = Booking.objects.all()
        else:
            bookings = Booking.objects.filter(user=request.user)
        serializer = BookingSerializer(bookings, many=True)
        return Response(serializer.data)


class BookingDetailAPIView(APIView):
    permission_classes = [permissions.IsAuthenticated, IsOwnerOrAdmin]

    def get_object(self, pk):
        try:
            return Booking.objects.get(pk=pk)
        except Booking.DoesNotExist:
            return None

    def get(self, request, pk):
        booking = self.get_object(pk)
        if not booking:
            return Response({'error': 'Bron Topilmadi'}, status=status.HTTP_404_NOT_FOUND)
        self.check_object_permissions(request, booking)
        serializer = BookingSerializer(booking)
        return Response(serializer.data)

    def put(self, request, pk):
        booking = self.get_object(pk)
        if not booking:
            return Response({'error': 'Bron Topilmadi'}, status=status.HTTP_404_NOT_FOUND)

        self.check_object_permissions(request, booking)
        serializer = BookingSerializer(booking, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        booking = self.get_object(pk)
        if not booking:
            return Response({'error': 'Bron Topilmadi'}, status=status.HTTP_404_NOT_FOUND)
        self.check_object_permissions(request, booking)
        booking.delete()
        return Response({'message': "Bron o'chirildi"}, status=status.HTTP_204_NO_CONTENT)
