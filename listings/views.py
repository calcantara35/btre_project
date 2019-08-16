from django.shortcuts import get_object_or_404, render
from django.core.paginator import Paginator
from .models import Listing


def index(request):

    listings = Listing.objects.order_by('-list_date').filter(is_published=True)
    paginator = Paginator(listings, 6)

    page = request.GET.get('page')
    paged_listings = paginator.get_page(page)

    context = {
        'listings': paged_listings
    }

    return render(request, 'listings/listings.html', context)


def listing(request, listing_id):
    listing = get_object_or_404(Listing, pk=listing_id)

    # getting internal photos
    internal_photos = []
    for i in range(1, 7):
        if getattr(listing, 'photo_%d' % i):
            photo = getattr(listing, 'photo_%d' % i)
            internal_photos.append(photo)

    context = {
        'listing': listing,
        'internal_photos': internal_photos
    }

    return render(request, 'listings/listing.html', context)


def search(request):
    return render(request, 'listings/search.html')
