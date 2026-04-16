from django.shortcuts import render
from django.conf import settings
import razorpay
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
import json

# Initialize Razorpay client
razorpay_client = razorpay.Client(auth=(settings.RAZORPAY_KEY_ID, settings.RAZORPAY_KEY_SECRET))

# Homepage
def home(request):
    return render(request, 'courses/home.html')

# Login page
def login_view(request):
    return render(request, "courses/login.html")

# About page
def about(request):
    return render(request, "courses/about.html")

# Courses list
def courses_list(request):
    return render(request, 'courses/courses.html')

# Individual course pages
def generative_ai(request):
    return render(request, 'courses/generative_ai.html')

def data_science(request):
    return render(request, 'courses/data_science.html')

def web_development(request):
    return render(request, 'courses/web_development.html')

def cyber_security(request):
    return render(request, 'courses/cyber_security.html')

def cloud_computing(request):
    return render(request, 'courses/cloud_computing.html')

def python_data_analytics(request):
    return render(request, 'courses/python_data_analytics.html')

# Razorpay Payment Integration
@csrf_exempt
def create_order(request):
    if request.method == "POST":
        try:
            amount = int(request.POST.get("amount", 0)) * 100  # Convert to paise
            currency = "INR"

            order_data = {
                "amount": amount,
                "currency": currency,
                "payment_capture": 1
            }

            razorpay_order = razorpay_client.order.create(data=order_data)

            return JsonResponse({
                "order_id": razorpay_order["id"],
                "razorpay_key": settings.RAZORPAY_KEY_ID,
                "amount": amount
            })
        except Exception as e:
            return JsonResponse({"error": str(e)}, status=400)

    return JsonResponse({"error": "Invalid request"}, status=400)

@csrf_exempt
def verify_payment(request):
    if request.method == "POST":
        try:
            data = json.loads(request.body)
            params_dict = {
                "razorpay_order_id": data.get("order_id"),
                "razorpay_payment_id": data.get("payment_id"),
                "razorpay_signature": data.get("signature"),
            }

            razorpay_client.utility.verify_payment_signature(params_dict)
            return JsonResponse({"status": "Payment verified successfully"})
        except razorpay.errors.SignatureVerificationError:
            return JsonResponse({"status": "Payment verification failed"}, status=400)

    return JsonResponse({"error": "Invalid request"}, status=400)
