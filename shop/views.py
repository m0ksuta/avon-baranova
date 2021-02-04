from django.shortcuts import get_object_or_404, render

from .models import Actual, Paragraph

# from ..static.media import actual_images
# Create your views here.


def home(request):
    actuals = Actual.objects.all()
    paragraph = Paragraph.objects.all()
    return render(request, 'home.html', {'actuals': actuals, 'paragraph': paragraph})


def catalogue(request):
    return render(request, 'catalogue.html')
