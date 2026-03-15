from django.shortcuts import render
from django.http import HttpResponse
from django.core.mail import send_mail,EmailMessage
# Create your views here.

# def email_Sent(request):
#    subject = 'Welcome to my Blog'
#   message = "Thank you for using my website"
#    from_email = 'quddous@gmail.com'
#    recipient_list = ['quddous@gmail.com']

#    send_mail(subject , message, from_email , recipient_list)
#    return HttpResponse("Email sent Successfully") 
