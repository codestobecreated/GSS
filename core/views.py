from django.shortcuts import render, redirect
from django.http import JsonResponse
from .forms import InquiryForm

def home(request):
    form = InquiryForm()
    return render(request, 'home.html', {'form': form})

def services(request):
    return render(request, 'services.html')

def gallery(request):
    return render(request, 'gallery.html')

def about(request):
    return render(request, 'about.html')

def contact_page(request):
    form = InquiryForm()
    return render(request, 'contact.html', {'form': form})



def contact_submit(request):
    if request.method == 'POST':
        form = InquiryForm(request.POST)
        if form.is_valid():
            inquiry = form.save()
            booking_date = inquiry.booking_date.strftime('%B %d, %Y') if inquiry.booking_date else 'Soon'
            return JsonResponse({
                'status': 'success', 
                'message': 'Booking Request Received!',
                'booking_date': booking_date,
                'client_name': inquiry.name
            })
        else:
            return JsonResponse({'status': 'error', 'errors': form.errors}, status=400)
    return redirect('home')
