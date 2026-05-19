from django.shortcuts import render
from site_setup.models import SiteSetup
# Create your views here.

def index(request):
    site = SiteSetup.objects.first()
    print(site)
    context = {
        'site': site
    }
    return render(
        request,
        'blog/pages/index.html',
        context
    )
        