import json

from hackinit.shortcuts import parameter_error, duplicate_error
from .models import *

from django.shortcuts import render
from django.views.decorators.http import require_http_methods
from django.core.exceptions import ValidationError
from django.http import JsonResponse
from django.db import IntegrityError

@require_http_methods(["POST"])
def subscribe_email(request):
    try:
        body = json.loads(request.body)
        email_address = body["email_address"]
    except:
        return parameter_error

    try:
        SubscriptionEmailAddress.objects.create(email_address=email_address)
    except ValidationError:
        return parameter_error
    except IntegrityError:
        return duplicate_error

    return JsonResponse({
        "email_address": email_address,
        "status": 200,
        "message": "email subscribed"
    })

@require_http_methods(["POST"])
def subscribe_sms(request):
    try:
        body = json.loads(request.body)
        cellphone_number = body["cellphone_number"]
    except:
        return parameter_error

    try:
        SubscriptionCellphoneNumber.objects.create(cellphone_number=cellphone_number)
    except ValidationError:
        return parameter_error
    except IntegrityError:
        return duplicate_error

    return JsonResponse({
        "cellphone_number": cellphone_number,
        "status": 200,
        "message": "SMS subscribed"
    })
