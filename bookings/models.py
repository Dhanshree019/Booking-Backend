from django.db import models
from accounts.models import CustomUser

import random, string

# Create your models here.

class BusOperator(models.Model):
    """Bus operator details"""
    name = models.CharField(max_length=128, unique=True)
    contact_number = models.CharField(max_length=16, blank=True, null=True)

    # timestamps
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

    class Meta:
        db_table = 'bus_operator'


class Bus(models.Model):
    """Bus details"""
    TYPE_CHOICES = [
        ('sleeper', 'Sleeper'),
        ('sitting', 'Sitting'),
        ('both', 'Both'),
    ]

    name = models.CharField(max_length=128)
    operator = models.ForeignKey(BusOperator, on_delete=models.CASCADE, related_name='buses')
    bus_type = models.CharField(max_length=10, choices=TYPE_CHOICES)
    sitting_seats = models.PositiveIntegerField()
    sleeper_seats = models.PositiveIntegerField()

    # timestamps
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return f"{self.name} ({self.operator.name})"

    class Meta:
        db_table = 'bus'


class Stop(models.Model):
    """Stores all possible bus stops"""
    name = models.CharField(max_length=128, unique=True)
    latitude = models.DecimalField(max_digits=9, decimal_places=6, null=True, blank=True)
    longitude = models.DecimalField(max_digits=9, decimal_places=6, null=True, blank=True)

    # timestamps
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

    class Meta:
        db_table = 'stop'


class Route(models.Model):
    """Bus route details"""
    source = models.ForeignKey(Stop, on_delete=models.CASCADE, related_name="route_source")
    destination = models.ForeignKey(Stop, on_delete=models.CASCADE, related_name="route_destination")
    stops = models.ManyToManyField(Stop, related_name="routes", help_text="All stops including source & destination")
    duration = models.DurationField(help_text="Duration of the trip in HH:MM:SS format")

    # timestamps
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.source} → {self.destination}"

    class Meta:
        db_table = 'route'


class BusSchedule(models.Model):
    """Schedule for a particular bus on a specific route and date"""
    bus = models.ForeignKey(Bus, on_delete=models.CASCADE, related_name='schedules')
    route = models.ForeignKey(Route, on_delete=models.CASCADE, related_name='schedules')
    departure_time = models.DateTimeField()
    arrival_time = models.DateTimeField()

    # timestamps
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.bus.name} - {self.route.source} → {self.route.destination} ({self.departure_time})"

    class Meta:
        db_table = 'bus_schedule'


class Seat(models.Model):
    """Seat details for a specific bus"""
    SEAT_TYPE_CHOICES = [
        ('sleeper', 'Sleeper'),
        ('sitting', 'Sitting'),
    ]

    bus = models.ForeignKey(Bus, on_delete=models.CASCADE, related_name='seats')
    seat_number = models.CharField(max_length=10)
    seat_type = models.CharField(max_length=10, choices=SEAT_TYPE_CHOICES)

    # timestamps
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"Bus: {self.bus.name}, Seat: {self.seat_number}, Type: {self.seat_type}"

    class Meta:
        db_table = 'seat'


class Booking(models.Model):
    """Ticket booking details"""
    STATUS_CHOICES = [
        ('pending', 'Pending'),
        ('confirmed', 'Confirmed'),
        ('cancelled', 'Cancelled'),
    ]

    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE, related_name='bookings')
    booking_id = models.CharField(max_length=16, unique=True)
    schedule = models.ForeignKey(BusSchedule, on_delete=models.CASCADE, related_name='bookings')
    seats = models.ManyToManyField(Seat, related_name='bookings')
    booking_datetime = models.DateTimeField(auto_now_add=True)
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default='pending')
    total_amount = models.DecimalField(max_digits=10, decimal_places=2)

    # timestamps
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"Booking {self.id} - {self.user.phone_number} - {self.status}"

    class Meta:
        db_table = 'bookings'

    def save(self, *args, **kwargs):
        if not self.booking_id:
            self.booking_id = self.generate_unique_booking_id()

        super().save(*args, **kwargs)

    def generate_unique_wallet_id(self):
        code = ''.join(random.choices(string.ascii_uppercase + string.digits, k=10))
        return f"B{code}"
    


