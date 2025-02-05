from django.shortcuts import render
from django.core.mail import send_mail
from django.conf import settings
from django.http import JsonResponse
from credentials.models import user_table
from employer.models import employer_table
import requests,json
import random
# Create your views here.

def validate_email(email):
    response = requests.get("https://emailvalidation.abstractapi.com/v1/?api_key=e99c10accc354433a8509425479e7eef&email="+email)
    print(response.status_code)
    data = json.loads(response.content)
    is_disposable = data["is_disposable_email"]["value"]
    is_invalid = (
        data["deliverability"] == "UNDELIVERABLE"
        or not data["is_smtp_valid"]["value"]
        or float(data["quality_score"]) == 0.0
    )
    is_not_free = (
        data["is_free_email"]["value"]
    )
    # Output results
    if is_disposable:
        print(f"The email {data['email']} is disposable.")
        False
    if is_not_free:
        print(f"The email {data['email']} is not free.")
    elif is_invalid:
        print(f"The email {data['email']} is invalid.")
        return False
    else:
        return True

def email_auth(request):
    print('inside email_auth')
    if request.method == 'POST':
        receipent_type = request.POST.get('type')
        recipient_email = request.POST.get('email')  # Extract email from the request
        if (receipent_type == 'user'):
            if not recipient_email:
                
                return JsonResponse({"message": "Email is required", "status": "error"}, status=400)
            user = user_table.objects.filter(email=recipient_email)
            
            if user:
                return JsonResponse({"message": "Email already exists", "status": "error"}, status=400)
        else:
            if not recipient_email:
                return JsonResponse({"message": "Email is required", "status": "error"}, status=400)
            emp = employer_table.objects.filter(email=recipient_email)
            if emp:
                return JsonResponse({"message": "Email already exists", "status": "error"}, status=400)
            
        response = requests.get("https://emailvalidation.abstractapi.com/v1/?api_key=e99c10accc354433a8509425479e7eef&email="+recipient_email)
        print(response.status_code)
        data = json.loads(response.content)
        print(data["is_free_email"]["value"])
        is_disposable = data["is_disposable_email"]["value"]
        is_invalid = (
            data["deliverability"] == "UNDELIVERABLE"
            or not data["is_smtp_valid"]["value"]
            or float(data["quality_score"]) == 0.0
        )
        is_not_free = (
            not data["is_free_email"]["value"]
        )
        # Output results
        if is_disposable or is_invalid:
            error_msg = (f"Email is disposable or invalid.")
            return JsonResponse({"message": error_msg, "status": "error"}, status=400)
        if is_not_free:
            error_msg = (f"Email is not free.")
            return JsonResponse({"message": error_msg, "status": "error"}, status=400)
        
        otp = random.randint(1000, 9999)  # Generate a 6-digit OTP
        print('otp is ',otp)
        # Save OTP to session (can be replaced with DB storage)
        request.session['email_verification_otp'] = otp
        request.session['email_to_verify'] = recipient_email

        # Send email with OTP
        subject = 'Email Verification'
        message = f'Your  OTP for verification is: {otp} \n Dont Share with any one'

        try:
            print(subject, message, settings.DEFAULT_FROM_EMAIL, [recipient_email])
            send_mail(subject, message, settings.DEFAULT_FROM_EMAIL, [recipient_email])
            print('Otp send to ',recipient_email)
            return JsonResponse({"message": "OTP sent successfully", "status": "success"})
        except Exception as e:
            print(e)
            return JsonResponse({"message": "Failed to send OTP", "status": "error"}, status=500)
    else:
        return JsonResponse({"message": "Invalid request method", "status": "error"}, status=405)
def verify_otp(request):
    if request.method == 'POST':
        entered_otp = request.POST.get('otp')
        session_otp = request.session.get('email_verification_otp')
        session_email = request.session.get('email_to_verify')
        
        if str(entered_otp) == str(session_otp):
            request.session['email_verified'] = True
            return JsonResponse({"message": "Email verified successfully", "status": "success"})
        else:
            return JsonResponse({"message": "Invalid OTP", "status": "error"}, status=400)
    else:
        return JsonResponse({"message": "Invalid request method", "status": "error"}, status=405)
