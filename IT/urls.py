"""IT URL Configuration

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
from django.conf.urls import url
from django.contrib import admin
from django.conf import settings

from Assets.views import tables_laptop_view, tables_staffs_view, dashboard_view, tables_owners_view, login_view, \
    logout_view

app_name = 'it_assets'

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url('tables/laptops', tables_laptop_view, name='table_laptops_view'),
    url('tables/owners', tables_owners_view, name='table_owners_view'),
    url('tables/staffs', tables_staffs_view, name='table_staffs_view'),
    url('dashboard/', dashboard_view, name='dashboard_view'),
    url('login/', login_view, name='login_view'),
    url('logout/', logout_view, name='logout_view'),
]
if settings.DEBUG:
    from django.conf.urls.static import static

    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
