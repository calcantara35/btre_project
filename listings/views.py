from django.shortcuts import get_object_or_404, render
from django.core.paginator import Paginator
from .choices import price_choices, bedroom_choices, state_choices

from .models import Listing


def index(request):

    listings = Listing.objects.order_by('-list_date').filter(is_published=True)
    paginator = Paginator(listings, 6)

    page = request.GET.get('page')
    paged_listings = paginator.get_page(page)

    context = {
        'listings': paged_listings,

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
    queryset_list = Listing.objects.order_by('-list_date')

    # Keywords
    if 'keywords' in request.GET:
        keywords = request.GET['keywords']
        if keywords:
            queryset_list = queryset_list.filter(
                description__icontains=keywords)

    # City, iexact is case insensitive
    if 'city' in request.GET:
        city = request.GET['city']
        if city:
            queryset_list = queryset_list.filter(
                city__iexact=city)

    # State, iexact is case insensitive
    if 'state' in request.GET:
        state = request.GET['state']
        if state:
            queryset_list = queryset_list.filter(
                state__iexact=state)

    # Bedrooms, getting everything up to nth bedrooms, lte is less than or equal to
    if 'bedrooms' in request.GET:
        bedrooms = request.GET['bedrooms']
        if bedrooms:
            queryset_list = queryset_list.filter(
                bedrooms__lte=bedrooms)

    # price, getting everything up to nth price, lte is less than or equal to
    if 'price' in request.GET:
        price = request.GET['price']
        if price:
            queryset_list = queryset_list.filter(
                price__lte=price)

    context = {
        'state_choices': state_choices,
        'bedroom_choices': bedroom_choices,
        'price_choices': price_choices,
        'listings': queryset_list
    }

    return render(request, 'listings/search.html', context)
