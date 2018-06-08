from django.urls import path

from . import views

app_name = 'app'
urlpatterns = [
    path('', views.IndexView.as_view(), name='index_view'),
    path('blog', views.BlogView.as_view(), name='blog_view'),
    path('form', views.ContactView.as_view(), name='contact_view'),
]
