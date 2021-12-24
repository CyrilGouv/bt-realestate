from django.shortcuts import get_object_or_404, render
from .models import Listing


def listings(request):
    listings = Listing.objects.order_by('-list_date').filter(is_published=True)
    
    context = {
        'listings': listings
    }
    
    return render(request, 'listings/listings.html', context)



def detail(request, listing_id):
    listing = get_object_or_404(Listing, id=listing_id)

    context = {
        'listing': listing
    }

    return render(request, 'listings/listing.html', context)



def search(request):
    return render(request, 'listings/search.html')
