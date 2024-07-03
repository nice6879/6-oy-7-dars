"""
URL configuration for config project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
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
from django.urls import path
from shop.views import home, cotegory,about, detail, product_create, product_update, product_delete

from django.conf import settings  
from django.conf.urls.static import static  

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home, name='home'),
    path('cotegory/<int:id>/', cotegory, name='cotegory'),
    path('detail/<int:id>/', detail, name='detail'),
    path('about/', about, name='about'),

    path('product-create/', product_create, name='product_create'),
    path('product-update/<int:id>/', product_update, name='product_update'),
    path('product-delete/<int:id>/', product_delete, name='product_delete'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
