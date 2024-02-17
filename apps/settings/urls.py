from django.urls import  path

from  apps.settings.views import  index, about, coming, gallery, contact_view, where, blog, blog_post

urlpatterns = [
    path("", index, name="index"),
    path("about", about, name='about'),
    path("coming", coming, name='coming'),
    path("gellary", gallery, name='gellary'),
    path('contacts', contact_view, name='contacts'),
    path('where', where, name='where'),
    path('blog', blog, name='blog'),
    path('blog_post', blog_post, name='blog_post'),
]