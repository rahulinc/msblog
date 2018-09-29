from django.contrib import admin

# Register your models here.

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


admin.site.register(stories)
admin.site.register(fashion)
admin.site.register(lifestyle)
admin.site.register(music)
admin.site.register(art)
admin.site.register(glamour)
admin.site.register(sliderCard)
admin.site.register(trending)
admin.site.register(blocks)
admin.site.register(topStories)
admin.site.register(mostPopular)
