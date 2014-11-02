from django.shortcuts import get_object_or_404, render
from apps.donations.models import Donation

def index(request):
    donations_list = Donation.objects.order_by('donation_date')
    context = {'donations_list': donations_list}
    return render(request, 'donations/index.html', context)

def detail(request, donation_id):
    donation = get_object_or_404(Donation, pk=donation_id)
    return render(request, 'donations/detail.html', {'donation': donation})

