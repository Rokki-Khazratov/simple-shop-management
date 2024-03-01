from django.db import models as m


class Product(m.Model):
    name = m.CharField(max_length=250)
    quantity = m.PositiveSmallIntegerField()
    price = m.DecimalField(max_digits=11, decimal_places=5)

    def __str__(self):
        return self.name

class Debtors(m.Model):
    full_name = m.CharField(max_length=250)
    phone_numuber = m.CharField(max_length=250)
    product = m.ManyToManyField(Product)
    date = m.DateField(auto_now_add=True)
    price = m.DecimalField(max_digits=11, decimal_places=5)

    def __str__(self):
        return self.full_name