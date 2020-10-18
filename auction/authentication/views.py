from auction.utility import *
from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view, permission_classes
from .controllers import *
from rest_framework.permissions import IsAuthenticated


@api_view(['POST'])
def register_user_details(request):
    """
    METHOD : POST
    PERMISSION : ANYONE
    BODY TO SEND : {

    }
    RESPONSE (SUCCESS) : {
        "status": "success",
        "message": "User registered successfully ."
    }
    URL : "user/auth/register/"
    :param request:
    :return:
    """
    try:
        success, msg = register_user_data(request)
        response_data = get_response_object(success, msg)
    except Exception as e:
        print(e.args)
        response_data = get_response_object(False, 'Error in user registration. Please try again.')
    return Response(data=response_data, status=status.HTTP_200_OK)


@api_view(['GET'])
@permission_classes((IsAuthenticated,))
def get_user_data(request):
    """
    METHOD : GET
    PERMISSION : IsAuthenticated
    HEADERS TO SEND : {
        Authorization: Bearer + <token>
    }
    RESPONSE (SUCCESS) : {
        "status": "success",
        "message": "User Login Successfully ."
    }
    URL : "user/auth/get_user_data/"
    :param request:
    :return:
    """
    try:
        success, msg, data = get_user_details(request)
        response_data = get_response_object(success, msg, data)
    except Exception as e:
        print(e.args)
        response_data = get_response_object(False, 'Error in user login. Please try again.')
    return Response(data=response_data, status=status.HTTP_200_OK)

