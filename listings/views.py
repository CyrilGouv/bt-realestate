from django.shortcuts import render
from .models import Listing


def listings(request):
    listings = Listing.objects.order_by('-list_date').filter(is_published=True)
    
    context = {
        'listings': listings
    }
    
    return render(request, 'listings/listings.html', context)



def detail(request, listing_id):
    return render(request, 'listings/listing.html')



def search(request):
    return render(request, 'listings/search.html')
