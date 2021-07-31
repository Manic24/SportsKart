"""sportskart URL Configuration

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
from django.contrib import admin
from django.urls import path
from django.conf.urls.static import static
from sk import views
urlpatterns = [
    path('admin/', admin.site.urls),
    path('home/', views.home),
    path('products/', views.product),
    path('account/', views.account,name='account'),
    path('', views.login,name='login'),
    path('sneakers/', views.sneakers),
    path('supplements/', views.supplement),
    path('apparel/', views.apparel),
    path('about/', views.abt),
    path('cart/', views.cart),
    path('cash/', views.cash,name='cash'),
    path('card/', views.card,name='card'),
    path('accessories/', views.access),
    path('kits/', views.kits),
    path('equipments/', views.equip)
]

urlpatterns = urlpatterns + static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)