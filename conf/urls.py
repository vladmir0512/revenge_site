"""conf URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from django.conf.urls import (handler400, handler403, handler404, handler500)
from main import views
from django.conf.urls.static import static
from django.conf import settings

handler404 = 'main.views.custom_page_not_found_view'
handler500 = 'main.views.custom_error_view'
handler403 = 'main.views.custom_permission_denied_view'
handler400 = 'main.views.custom_bad_request_view'

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',  include('main.urls'),  name='home')
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
