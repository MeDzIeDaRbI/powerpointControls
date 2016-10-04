# import the necessary packages
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse
import urllib
import json
import pyautogui



def activate(action):
    if action == 'next':
        pyautogui.press('space')
        print 'next'
        pass
    elif action == 'previous':
        pyautogui.press('backspace')
        print 'previous'
        pass
    elif action == 'goto':
        pass
    pass


@csrf_exempt
def activ(request):
    # initialize the data dictionary to be returned by the request
    data = {"success": False}

    # check to see if this is a post request
    if request.method == "POST":
        # assume that a username was passed in
        if request.POST.get("action", None) is not None:
            # grab the URL from the request
            action = request.POST.get("action", None)

            # if the username is None, then return an error
            if action is None:
                data["error"] = "No action provided."
                return JsonResponse(data)
            else:
                data["success"] = True
                # TEST BLOCk ##################################################
                activate(action)

                # TEST BLOCk ##################################################
                pass
    # return a JSON response
    return JsonResponse(data)
