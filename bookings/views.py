from django.db import transaction

from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework.permissions import IsAuthenticated
import rest_framework.status as HttpStatusCode

from accounts.models import CustomUser
from bookings.models import *
from bookings.serializers import *

class BusOperatorView(APIView):
    def post(self, request):
        try:
            rd = request.data
            bus_operator_details = BusOperatorSerializer(data=rd)

            if bus_operator_details.is_valid():
                bus_operator_details.save()
                return Response({"Success":True,"Message":"Data created successfully","Data":bus_operator_details.data}, status=HttpStatusCode.HTTP_201_CREATED)
            else:
                return Response({"Success":False,"Message":"Please provide proper data","Error":bus_operator_details.errors}, status=HttpStatusCode.HTTP_400_BAD_REQUEST)
        except Exception as err:
            print("Error -",err)
            return Response({"Success":False,"Message":"Unexcpected error occurs"}, status=HttpStatusCode.HTTP_500_INTERNAL_SERVER_ERROR)

    def get(self, request):
        try:
            
            bus_operator_data = BusOperator.objects.all()
            bus_operator_serialize_data = BusOperatorSerializer(bus_operator_data, many=True)

            if bus_operator_serialize_data:
                return Response({"Success":True,"Message":"Data fetch successfully","Data":bus_operator_serialize_data.data}, status=HttpStatusCode.HTTP_200_OK)
            else:
                return Response({"Success":False,"Message":"Data not found"}, status=HttpStatusCode.HTTP_404_NOT_FOUND)
            
        except Exception as err:
            print("Error -",err)
            return Response({"Success":False,"Message":"Unexcpected error occurs"}, status=HttpStatusCode.HTTP_500_INTERNAL_SERVER_ERROR)


class BusView(APIView):
    def post(self, request):
        try:
            rd = request.data
            bus_data = BusSerializer(data= rd)

            if bus_data.is_valid():
                bus_data.save()
                return Response({"Success":True,"Message":"Data created successfully","Data":bus_data.data}, status=HttpStatusCode.HTTP_201_CREATED)
            else:
                return Response({"Success":False,"Message":"Please provide proper data","Error":bus_data.errors}, status=HttpStatusCode.HTTP_400_BAD_REQUEST)
            
        except Exception as err:
            print("Error -",err)
            return Response({"Success":False,"Message":"Unexcpected error occurs"}, status=HttpStatusCode.HTTP_500_INTERNAL_SERVER_ERROR)

    def get(self, request):
        try:
            
            bus_data = Bus.objects.all()
            bus_serialize_data = BusSerializer(bus_data, many=True)

            if bus_serialize_data:
                return Response({"Success":True,"Message":"Data fetch successfully","Data":bus_serialize_data.data}, status=HttpStatusCode.HTTP_200_OK)
            else:
                return Response({"Success":False,"Message":"Data not found"}, status=HttpStatusCode.HTTP_404_NOT_FOUND)
            
        except Exception as err:
            print("Error -",err)
            return Response({"Success":False,"Message":"Unexcpected error occurs"}, status=HttpStatusCode.HTTP_500_INTERNAL_SERVER_ERROR)


class StopView(APIView):
    def post(self, request):
        try:
            rd = request.data
            stop_data = StopSerializer(data= rd)

            if stop_data.is_valid():
                stop_data.save()
                return Response({"Success":True,"Message":"Data created successfully","Data":stop_data.data}, status=HttpStatusCode.HTTP_201_CREATED)
            else:
                return Response({"Success":False,"Message":"Please provide proper data","Error":stop_data.errors}, status=HttpStatusCode.HTTP_400_BAD_REQUEST)
            
        except Exception as err:
            print("Error -",err)
            return Response({"Success":False,"Message":"Unexcpected error occurs"}, status=HttpStatusCode.HTTP_500_INTERNAL_SERVER_ERROR)

    def get(self, request):
        try:
            
            stop_data = Stop.objects.all()
            stop_serialize_data = StopSerializer(stop_data, many=True)

            if stop_serialize_data:
                return Response({"Success":True,"Message":"Data fetch successfully","Data":stop_serialize_data.data}, status=HttpStatusCode.HTTP_200_OK)
            else:
                return Response({"Success":False,"Message":"Data not found"}, status=HttpStatusCode.HTTP_404_NOT_FOUND)
            
        except Exception as err:
            print("Error -",err)
            return Response({"Success":False,"Message":"Unexcpected error occurs"}, status=HttpStatusCode.HTTP_500_INTERNAL_SERVER_ERROR)

class RouteView(APIView):
    def post(self, request):
        try:
            rd = request.data
            route_data = RouteSerializer(data= rd)

            if route_data.is_valid():
                route_data.save()
                return Response({"Success":True,"Message":"Data created successfully","Data":route_data.data}, status=HttpStatusCode.HTTP_201_CREATED)
            else:
                return Response({"Success":False,"Message":"Please provide proper data","Error":route_data.errors}, status=HttpStatusCode.HTTP_400_BAD_REQUEST)
            
        except Exception as err:
            print("Error -",err)
            return Response({"Success":False,"Message":"Unexcpected error occurs"}, status=HttpStatusCode.HTTP_500_INTERNAL_SERVER_ERROR)

    def get(self, request):
        try:
            
            route_data = Route.objects.all()
            route_serialize_data = RouteSerializer(route_data, many=True)

            if route_serialize_data:
                return Response({"Success":True,"Message":"Data fetch successfully","Data":route_serialize_data.data}, status=HttpStatusCode.HTTP_200_OK)
            else:
                return Response({"Success":False,"Message":"Data not found"}, status=HttpStatusCode.HTTP_404_NOT_FOUND)
            
        except Exception as err:
            print("Error -",err)
            return Response({"Success":False,"Message":"Unexcpected error occurs"}, status=HttpStatusCode.HTTP_500_INTERNAL_SERVER_ERROR)
        
class BusScheduleView(APIView):
    def post(self, request):
        try:
            rd = request.data
            bus_schedule_data = BusScheduleSerializer(data= rd)

            if bus_schedule_data.is_valid():
                bus_schedule_data.save()
                return Response({"Success":True,"Message":"Data created successfully","Data":bus_schedule_data.data}, status=HttpStatusCode.HTTP_201_CREATED)
            else:
                return Response({"Success":False,"Message":"Please provide proper data","Error":bus_schedule_data.errors}, status=HttpStatusCode.HTTP_400_BAD_REQUEST)
            
        except Exception as err:
            print("Error -",err)
            return Response({"Success":False,"Message":"Unexcpected error occurs"}, status=HttpStatusCode.HTTP_500_INTERNAL_SERVER_ERROR)

    def get(self, request):
        try:
            
            bus_schedule_data = BusSchedule.objects.all()
            bus_schedule_serialize_data = BusScheduleSerializer(bus_schedule_data, many=True)

            if bus_schedule_serialize_data:
                return Response({"Success":True,"Message":"Data fetch successfully","Data":bus_schedule_serialize_data.data}, status=HttpStatusCode.HTTP_200_OK)
            else:
                return Response({"Success":False,"Message":"Data not found"}, status=HttpStatusCode.HTTP_404_NOT_FOUND)
            
        except Exception as err:
            print("Error -",err)
            return Response({"Success":False,"Message":"Unexcpected error occurs"}, status=HttpStatusCode.HTTP_500_INTERNAL_SERVER_ERROR)


class SeatView(APIView):
    def post(self, request):
        try:
            rd = request.data
            seat_data = SeatSerializer(data= rd)

            if seat_data.is_valid():
                seat_data.save()
                return Response({"Success":True,"Message":"Data created successfully","Data":seat_data.data}, status=HttpStatusCode.HTTP_201_CREATED)
            else:
                return Response({"Success":False,"Message":"Please provide proper data","Error":seat_data.errors}, status=HttpStatusCode.HTTP_400_BAD_REQUEST)
            
        except Exception as err:
            print("Error -",err)
            return Response({"Success":False,"Message":"Unexcpected error occurs"}, status=HttpStatusCode.HTTP_500_INTERNAL_SERVER_ERROR)

    def get(self, request):
        try:
            
            seat_data = Seat.objects.all()
            seat_serialize_data = SeatSerializer(seat_data, many=True)

            if seat_serialize_data:
                return Response({"Success":True,"Message":"Data fetch successfully","Data":seat_serialize_data.data}, status=HttpStatusCode.HTTP_200_OK)
            else:
                return Response({"Success":False,"Message":"Data not found"}, status=HttpStatusCode.HTTP_404_NOT_FOUND)
            
        except Exception as err:
            print("Error -",err)
            return Response({"Success":False,"Message":"Unexcpected error occurs"}, status=HttpStatusCode.HTTP_500_INTERNAL_SERVER_ERROR)

class BookingView(APIView):
    def post(self, request):
        try:
            rd = request.data
            booking_data = BookingSerializer(data= rd)

            if booking_data.is_valid():
                booking_data.save()
                return Response({"Success":True,"Message":"Data created successfully","Data":booking_data.data}, status=HttpStatusCode.HTTP_201_CREATED)
            else:
                return Response({"Success":False,"Message":"Please provide proper data","Error":booking_data.errors}, status=HttpStatusCode.HTTP_400_BAD_REQUEST)
            
        except Exception as err:
            print("Error -",err)
            return Response({"Success":False,"Message":"Unexcpected error occurs"}, status=HttpStatusCode.HTTP_500_INTERNAL_SERVER_ERROR)

    def get(self, request):
        try:
            
            booking_data = Seat.objects.all()
            booking_serialize_data = SeatSerializer(booking_data, many=True)

            if booking_serialize_data:
                return Response({"Success":True,"Message":"Data fetch successfully","Data":booking_serialize_data.data}, status=HttpStatusCode.HTTP_200_OK)
            else:
                return Response({"Success":False,"Message":"Data not found"}, status=HttpStatusCode.HTTP_404_NOT_FOUND)
            
        except Exception as err:
            print("Error -",err)
            return Response({"Success":False,"Message":"Unexcpected error occurs"}, status=HttpStatusCode.HTTP_500_INTERNAL_SERVER_ERROR)











