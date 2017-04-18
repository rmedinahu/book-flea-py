"""bookflea URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url, include
from django.contrib import admin

from bookstore.views import HomeView, UpdateBookView, ItemCreateView, ItemCategoryView, ItemDetail, DetailItemCategoryView


urlpatterns = [
    url(r'^$', HomeView.as_view(), name='home'),
    url(r'^admin/', admin.site.urls),

    url(r'^item/(?P<pk>\d+)/$', ItemDetail.as_view(), name='item_detail'),
    url(r'^category/add/$', ItemCategoryView.as_view(), name='category_add'),
    url(r'^update/(?P<pk>\d+)/$', UpdateBookView.as_view(), name='update'),
    url(r'^item/add/$', ItemCreateView.as_view(), name='item_add'),
    url(r'^itemcategory/(?P<pk>\d+)/$', DetailItemCategoryView.as_view(), name='itemcategory_detail'),

]
