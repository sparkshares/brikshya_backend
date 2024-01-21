from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from rest_framework.decorators import api_view, parser_classes
from rest_framework.parsers import MultiPartParser

import requests
from urllib.parse import quote

from rest_framework.permissions import IsAuthenticated

from app.services.accept_donation import accept_donation_service
from app.services.firebase.readSensors import get_sensor_data
from app.services.list_accepted_donation_service import list_accepted_donation_service
from app.services.list_all_donations import list_all_donation_service
from app.services.update_tree_donation_status import update_tree_donation_status_service

@api_view(['POST'])
@permission_classes([IsAuthenticated])
def accept_donation_view(request):
    data, status_code = accept_donation_service(request.user, request.data)
    return Response(data, status=status_code)

@api_view(['GET'])
@permission_classes([IsAuthenticated])
def list_accepted_donation_view(request):
    data, status_code = list_accepted_donation_service(request.user)
    return Response(data, status=status_code)

@api_view(['GET'])
def get_firebase_data(request):
    data = get_sensor_data()

    # base_url = 'https://user.rojekosms.com/smsapi/index.php?key=3638C5E929E700&campaign=7187&routeid=164&type=text&contacts=9813820488&senderid=SMSBit&msg='
    # warning = data.get('warning')

    # if warning == 1:
    #     message = 'Hey! Its time for watering the plan.'
    # elif warning == 2:
    #     message = 'Its too much heat for plan, please shade the plant or water them.'
    # elif warning == 3:
    #     message = 'Hurryup! Emergency watering to the plan is needed.'
    # else:
    #     return Response(data)

    # # Encode the message for URL
    # message = quote(message)

    # # Perform a GET request
    # response = requests.get(base_url + message)

    # # Check if the request was successful
    # if response.status_code != 200:
    #     return Response({'error': 'GET request failed'}, status=response.status_code)

    return Response(data)

@api_view(['GET'])
@permission_classes([IsAuthenticated])
def list_all_donation_view(request):
    data, status_code = list_all_donation_service()
    return Response(data, status=status_code)

@api_view(['POST'])
@permission_classes([IsAuthenticated])
def update_tree_donation_status_view(request, tree_accept_id):
    data, http_status = update_tree_donation_status_service(request.user, request.data, tree_accept_id)
    return Response(data, status=http_status)