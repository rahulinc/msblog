from django.urls import path
from . import views


urlpatterns = [
path('', views.landing, name='landing_page')
#path('maistory/posts', views.post_list, name='post_list'),
]
