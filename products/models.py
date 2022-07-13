from django.db import models


class Prod_category(models.Model):
    '''
    Defines the Product Categories model
    '''
    class Meta:
        verbose_name_plural = 'Product Categories'

    desc = models.CharField(max_length=255, unique=True)
    disp_name = models.CharField(max_length=255, unique=True)

    def __str__(self):
        return self.desc


class Vat_rate(models.Model):
    '''
    Defines the VAT (sales tax) rates.
    Products must have a default VAT rate. VAT code & rate must
    be saved against each invoice line item.
    '''

    # Default VAT Codes
    VAT_CODE = (
        ('S1', 'Sales1'),
        ('S2', 'Sales2'),
        ('S3', 'Sales3'),
        ('S4', 'Sales4'),
    )

    class Meta:
        verbose_name_plural = 'VAT Rates'

    code = models.CharField(max_length=2, choices=VAT_CODE, unique=True)
    rate = models.DecimalField(max_digits=4, decimal_places=2, default=0.0)
    is_default = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    last_modified = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.code + " - " + str(self.rate)


class Product(models.Model):
    '''
    Define the Product model.
    Products are largely digital services with a recurring
    licence revenue model.
    Products can be assigned a ranking to assist the site admin
    with displaying promoted products in a prominent position,
    e.g. an overlay on the home screen or top of the products list.
    Products must have a default VAT code.
    '''

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
    category = models.ForeignKey(Prod_category,
                                 null=True, blank=True,
                                 on_delete=models.SET_NULL,
                                 related_name='products')
    sku = models.CharField(max_length=255, null=True, blank=True)
    sell_price = models.DecimalField(max_digits=6,
                                     decimal_places=2,
                                     default=0.0)
    image = models.ImageField(null=True, blank=True)
    recurring_bill = models.CharField(max_length=1,
                                      choices=RECURRING_BILL,
                                      default='Z')
    display_rank = models.IntegerField(choices=DISPLAY_RANK, default=0)
    unit = models.CharField(max_length=20, null=True, blank=True)
    def_vat_rate = models.ForeignKey('Vat_rate',
                                     on_delete=models.PROTECT,
                                     related_name='products')
    out_of_use = models.BooleanField(default=False)

    def __str__(self):
        return self.desc
