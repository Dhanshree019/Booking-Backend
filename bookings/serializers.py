from rest_framework.serializers import ModelSerializer, SerializerMethodField, ValidationError
from bookings.models import *

class BusOperatorSerializer(ModelSerializer):
    class Meta:
        model = BusOperator
        fields = "__all__"
    
    def validate_contact_number(self, value):
        if len(value) < 10:
            raise ValidationError("Bus operator contact number should not be less than 10 digits")
        if BusOperator.objects.filter(contact_number=value).exists():
            raise ValidationError("Bus operator contact number already exists")
        return value

class BusSerializer(ModelSerializer):
    class Meta:
        model = Bus
        fields = "__all__"

class StopSerializer(ModelSerializer):
    class Meta:
        model = Stop
        fields = "__all__"

class RouteSerializer(ModelSerializer):
    class Meta:
        model = Route
        fields = "__all__"

class BusScheduleSerializer(ModelSerializer):
    class Meta:
        model = BusSchedule
        fields = "__all__"

class SeatSerializer(ModelSerializer):
    class Meta:
        model = Seat
        fields = "__all__"

class BookingSerializer(ModelSerializer):
    class Meta:
        model = Booking
        fields = "__all__"

