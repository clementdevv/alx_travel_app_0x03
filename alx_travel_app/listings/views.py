from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Listing, Booking
from rest_framework import viewsets
from .serializers import ListingSerializer, BookingSerializer


@api_view(['GET'])
def test_view(request):
    return Response({"message": "ALX Travel App is working!"})

class ListingViewSet(viewsets.ModelViewSet):
    queryset = Listing.objects.all()
    serializer_class = ListingSerializer

class BookingViewSet(viewsets.ModelViewSet):
    queryset = Booking.objects.all()
    serializer_class = BookingSerializer