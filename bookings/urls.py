from django.urls import path
from bookings.views import *

urlpatterns = [
    path('bus_operator', BusOperatorView.as_view()),
    path('bus', BusView.as_view()),
    path('stop', StopView.as_view()),
    path('route', RouteView.as_view()),
    path('bus_schedule', BusScheduleView.as_view()),
    path('seat', SeatView.as_view()),
    path('bus_booking', BookingView.as_view()),
]

