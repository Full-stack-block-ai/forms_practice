from django.shortcuts import render


# Create your views here.
def thank_you(request):
    return render(request, 'cars/thankyou.html')

def rental_review(request):
    return render(request, 'cars/rentalreview.html')