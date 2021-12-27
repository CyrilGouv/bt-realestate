from django.shortcuts import get_object_or_404, render
from .models import Listing
from django.core.paginator import Paginator
from .choices import price_choices, state_choices, bedroom_choices


def listings(request):
    listings_qs = Listing.objects.order_by('-list_date').filter(is_published=True)
    
    paginator = Paginator(listings_qs, 3)
    page = request.GET.get('page')
    listings = paginator.get_page(page)

    context = {
        'listings': listings
    }
    
    return render(request, 'listings/listings.html', context)



def detail(request, listing_id):
    listing = get_object_or_404(Listing, id=listing_id)

    context = {
        'listing': listing,
    }

    return render(request, 'listings/listing.html', context)



def search(request):
    
    listings_qs = Listing.objects.order_by('-list_date').filter(is_published=True)

    if request.method == 'GET':

        if 'keywords' in request.GET:
            keywords = request.GET.get('keywords')

            if keywords:
                listings_qs = listings_qs.filter(description__icontains=keywords)

        
        if 'city' in request.GET:
            city = request.GET.get('city')

            if city:
                listings_qs = listings_qs.filter(city__iexact=city)


        if 'state' in request.GET:
            state = request.GET.get('state')

            if state:
                listings_qs = listings_qs.filter(state__iexact=state)


        if 'bedrooms' in request.GET:
            bedrooms = request.GET.get('bedrooms')

            if bedrooms:
                listings_qs = listings_qs.filter(bedrooms__lte=bedrooms)

        
        if 'price' in request.GET:
            price = request.GET.get('price')

            if price:
                listings_qs = listings_qs.filter(price__lte=price)


    context = {
        'listings': listings_qs,

        'bedrooms': bedroom_choices,
        'states': state_choices,
        'prices': price_choices,
        'values': request.GET,
    }

    return render(request, 'listings/search.html', context)
