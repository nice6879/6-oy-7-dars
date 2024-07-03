from django.contrib import admin
from .models import Cotegory, Product, About
# Register your models here.


admin.site.register([Cotegory, Product, About])