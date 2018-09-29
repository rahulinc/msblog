from django.shortcuts import render
from django.utils import timezone
from .models import stories
from .models import fashion
from .models import lifestyle
from .models import music
from .models import art
from .models import glamour
from .models import sliderCard
from .models import trending
from .models import blocks
from .models import topStories
from .models import mostPopular



# Create your views here.

def content(request):
	posts = stories.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
	return render(request, 'blog/content.html', {'posts': posts})
def landing(request):
	return render(request, 'blog/landing.html', {})

# def content(request):
# 	posts = travel.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
# 	return render(request, 'blog/content.html', {'content': content})


# def post_list(request):

# 	return render(request, 'blog/post_list.html', {'posts': posts})