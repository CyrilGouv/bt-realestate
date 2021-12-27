from django.shortcuts import render, redirect
from django.contrib import messages
from .models import Contact


def enquiry(request):
    if request.method == 'POST':
        user_id = request.POST.get('user_id')
        listing = request.POST.get('listing')
        listing_id = request.POST.get('listing_id')
        name = request.POST.get('name')
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        message = request.POST.get('message')

        contact = Contact(user_id=user_id, listing=listing, listing_id=listing_id, name=name, email=email, phone=phone, message=message)
        contact.save()

        messages.success(request, 'Thank you for your enquiry !')
        return redirect('/listings/' + listing_id)
