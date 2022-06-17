from django.db import models


class Prod_category(models.Model):
    '''Defines the Product Categories model'''

    class Meta:
        verbose_name_plural = 'Product Categories'

    desc = models.CharField(max_length=255, unique=True)
    disp_name = models.CharField(max_length=255, unique=True)

    def __str__(self):
        return self.desc


class Product(models.Model):

    # Billing frequency for recurring licence/subscription services
    RECURRING_BILL = (
        ('A', 'Annual'),
        ('M', 'Monthly'),
        ('Q', 'Quarterly'),
        ('B', 'Biennial'),
        ('Z', 'No'),
    )

    # Rank promoted products for display order on home screen
    DISPLAY_RANK = (
        (0, 'Normal'),
        (10, 'Display Order 1'),
        (20, 'Display Order 2'),
        (30, 'Display Order 3'),
    )

    code = models.CharField(max_length=6, unique=True)
    desc = models.CharField(max_length=255, unique=True)
    long_desc = models.TextField(null=True, blank=True)
    category = models.ForeignKey('Prod_category', null=True, blank=True, on_delete=models.SET_NULL)
    sku = models.CharField(max_length=255, null=True, blank=True)
    sell_price = models.DecimalField(max_digits=6, decimal_places=2, default=0.0)
    image = models.ImageField(null=True, blank=True)
    recurring_bill = models.CharField(max_length=1, choices=RECURRING_BILL, default='Z')
    display_rank = models.IntegerField(choices=DISPLAY_RANK, default=0)

    def __str__(self):
        return self.desc
