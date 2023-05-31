"""apteka URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
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
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path

from online_store.views import IndexListView, CatalogListView, GoodDetailView, about_view, info_view, sales_view

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', IndexListView.as_view()),
    path('catalog/', CatalogListView.as_view()),
    path('good/<int:pk>/', GoodDetailView.as_view()),
    path('sales/', sales_view),
    path('info/', info_view),
    path('about/', about_view)
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
