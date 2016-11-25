from django.conf.urls import url
from .views import product





urlpatterns = [
    url(r'^$', product, name='product'),

]