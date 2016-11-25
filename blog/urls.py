from django.conf.urls import url, include
import views
urlpatterns = [
    url(r'^$', views.post_list, name='blog'),
    url(r'^(?P<id>\d+)/$', views.post_details, name="post details"),
    url(r'^post/new$', views.new_post, name="new_post"),
]