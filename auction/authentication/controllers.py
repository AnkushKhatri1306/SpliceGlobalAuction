from .models import *
from .serializers import *
from django.contrib.auth.models import User
from auction.utility import *
from django.db import transaction


def register_user_data(request):
    """
    function to save the data of user.
    1. Getting the data from request
    2. checking the data for validation , we can add more validation to that function as needed.
    3. then first saving the data of user in user table
    4. calling a function to save the other extra information of user to the table
    :param request:  request data
    :return:  message and status
    """
    success = False
    msg = 'Error in user registration. Please try again.'
    try:
        with transaction.atomic():
            post_data = request.data
            if post_data:
                success, msg = check_user_register_data_validation(post_data)
                if success:
                    obj = User.objects.filter(username=post_data.get('email')).first()
                    if obj:
                        return False, 'Error in user registration . Email id already exists.'
                    user_obj = User()
                    user_obj.first_name = post_data.get('firstName')
                    user_obj.last_name = post_data.get('lastName')
                    user_obj.email = post_data.get('email')
                    user_obj.username = post_data.get('email')
                    user_obj.set_password(post_data.get('password'))
                    user_obj.is_active = True
                    user_obj.save()
                    user_id = user_obj.id
                    success = save_user_profile_details(user_id, post_data)
                    if not success:
                        raise Exception('Manual Exception for mapping details of user type.')
                    success = True
                    msg = 'User registered successfully .'
    except Exception as e:
        success = False
        exception_detail(e)
    return success, msg


def check_user_register_data_validation(post_data):
    """
    function to check the validation of the data .
    1. added for few basic fields we can add more
    :param post_data:
    :return:
    """
    success = True
    msg = ''
    try:
        if not post_data.get('firstName'):
            success = False
            msg = 'Error in user registration. Please enter First Name .'
        elif not post_data.get('email'):
            success = False
            msg = 'Error in user registration. Please enter Email .'
        elif post_data.get('email') != post_data.get('confirmEmail'):
            success = False
            msg = 'Error in user registration. Email and Confirm Email is not same.'
        elif not post_data.get('password'):
            success = False
            msg = 'Error in user registration. Please enter Password .'
        elif post_data.get('password') != post_data.get('confirmPassword'):
            success = False
            msg = 'Error in user registration. Password and Confirm Password is not same.'
    except Exception as e:
        exception_detail(e)
    return success, msg


def save_user_profile_details(user_id, post_data):
    """
    function to save the extra profile information of user to the database
    1. first making the object of the model and then mapping all the data to that object
    2. saving the data to database
    :param user_id: user id
    :param post_data: post data containing the extra information
    :return:
    """
    success = False
    try:
        with transaction.atomic():
            user_pro_obj = UserProfileDetails()
            user_pro_obj.user_type = post_data.get('userType')
            user_pro_obj.user_id = user_id
            user_pro_obj.company_name = post_data.get('companyName')
            user_pro_obj.mobile = post_data.get('mobileNumber')
            user_pro_obj.telephone = post_data.get('telephone')
            user_pro_obj.address_lane_1 = post_data.get('addressLaneOne')
            user_pro_obj.address_lane_2 = post_data.get('addressLaneTwo')
            user_pro_obj.city = post_data.get('city')
            user_pro_obj.postal_zip = post_data.get('postalZip')
            user_pro_obj.country = post_data.get('country')
            user_pro_obj.state = post_data.get('state')
            user_pro_obj.save()
            success = True
    except Exception as e:
        exception_detail(e)
    return success


def get_user_details(request):
    """
    function to get the detail of user who login in using token
    1. getting all the data from request and setting into data object
    2. making message as Success and status as True
    :param request: request data containing the info of user
    :return: data object containing the user data.
    """
    data = {}
    success = False
    msg = 'Error in getting user details .'
    try:
        data['firstName'] = request.user.first_name
        data['lastName'] = request.user.last_name
        data['userId'] = request.user.id
        data['username'] = request.user.username
        data['email'] = request.user.email
        success = True
        msg = 'Success in getting user details .'
    except Exception as e:
        exception_detail(e)
    return success, msg, data
