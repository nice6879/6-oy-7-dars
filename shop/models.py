from django.db import models



class Cotegory(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return f"{self.name}"


class Product(models.Model):
    name = models.CharField(max_length=100)
    price = models.IntegerField()
    cotegory = models.ForeignKey(Cotegory, on_delete=models.CASCADE, related_name='products')
    image = models.ImageField(upload_to='product_image', null=True)

    def __str__(self):
        return f"{self.name}"

class About(models.Model):
    ABOUT_PLACE = (
        ('HTML', 'HTML'),
        ('DJANGO', 'DJANGO'),
        ('PYTHON', 'PYTHON'),
        ('CSS', 'CSS'),
    )
    f_name = models.CharField(max_length=100)
    l_name = models.CharField(max_length=100)
    place = models.CharField(max_length=100, choices=ABOUT_PLACE, default='PYTHON')

    def __str__(self) -> str:
        return f"{self.f_name}"