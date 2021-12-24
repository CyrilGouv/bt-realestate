from django.shortcuts import render
from listings.models import Listing
from realtors.models import Realtor


def index(request):
    listings = Listing.objects.order_by('-list_date').filter(is_published=True)[:3]

    context = {
        'listings': listings
    }

    return render(request, 'pages/index.html', context)


def about(request):
    realtors = Realtor.objects.order_by('-hire_date')
    realtor_mvp = Realtor.objects.filter(is_mvp=True)

    context = {
        'realtors': realtors,
        'realtor_mvp': realtor_mvp
    }

    return render(request, 'pages/about.html', context)
