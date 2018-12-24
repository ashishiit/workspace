from django.shortcuts import render, HttpResponse
from django.views.decorators.csrf import csrf_exempt
from twilio.twiml.messaging_response import MessagingResponse

# Create your views here.
@csrf_exempt
def sms_response(request):
    # Start our TwiML response
    resp = MessagingResponse()
    # Add a text message
    msg = resp.message("How you doin !!")
    
    return HttpResponse(str(resp))