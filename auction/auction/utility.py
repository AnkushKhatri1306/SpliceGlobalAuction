# Here is all the utility function access for common purpose
import traceback

def get_response_object(success=False, msg='', data=None):
    """
    function to make the response data after making a dict containing data, message and the status
    :param success: True or False
    :param msg: message to be returned in the dict 'message'
    :param data: put into data key of dict and return
    :return: dict containing the status, message and data
    NOTE : data only if the data is present and need to return
    """
    res_dict = {
        'status': 'error',
        'message': msg
    }
    try:
        if success:
            res_dict['status'] = 'success'
            if data is not None:
                res_dict['data'] = data
    except Exception as e:
        print(e.args)
    return res_dict

def exception_detail(error):
    """
    function to get the exception detail with line
    :return:
    """
    try:
        print('Exception Occur : ', traceback.format_exc())
    except Exception as e:
        print(e.args)