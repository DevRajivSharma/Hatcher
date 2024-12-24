from django.shortcuts import render
from django.core.mail import send_mail
from django.conf import settings
from django.http import JsonResponse
import random
# Create your views here.
def email_auth(request):
    if request.method == 'POST':
        recipient_email = request.POST.get('email')  # Extract email from the request
        if not recipient_email:
            return JsonResponse({"message": "Email is required", "status": "error"}, status=400)
        
        otp = random.randint(100000, 999999)  # Generate a 6-digit OTP
        
        # Save OTP to session (can be replaced with DB storage)
        request.session['email_verification_otp'] = otp
        request.session['email_to_verify'] = recipient_email

        # Send email with OTP
        subject = 'Email Verification'
        message = f'Your OTP for verification is: {otp}'
        try:
            send_mail(subject, message, settings.DEFAULT_FROM_EMAIL, [recipient_email])
            return JsonResponse({"message": "OTP sent successfully", "status": "success"})
        except Exception as e:
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