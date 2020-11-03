from django.db import models

# Create your models here.

class Partner(models.Model):
    company_name = models.CharField(max_length=50)
    logo = models.ImageField(upload_to='partner/logo/', null=True, blank=True)
    email = models.EmailField(unique=True)
    password = models.CharField(max_length=25)
    address = models.TextField(null=True, blank=True)

    class Meta:
        db_table = 'Partners'


class Training(models.Model):
    partner_id = models.CharField(max_length=15)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    name = models.CharField(max_length=50)
    description = models.TextField(null=True, blank=True)
    supporting_file = models.FileField(upload_to='partner/training/', null = True)

    class Meta:
        db_table = 'Trainings'


class Certificate(models.Model):
    partner_id = models.CharField(max_length=15)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    name = models.CharField(max_length=50)
    description = models.TextField(null=True, blank=True)
    supporting_file = models.FileField(upload_to='partner/certificate/', null = True)

    class Meta:
        db_table = 'Certificates'


class Article(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    name = models.CharField(max_length=50)
    description = models.TextField(null=True, blank=True)
    supporting_file = models.FileField(upload_to='help/articles/', null = True)

    class Meta:
        db_table = 'Articles'


class Bug(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    name = models.CharField(max_length=50)
    description = models.TextField(null=True, blank=True)
    supporting_file = models.FileField(upload_to='help/bugs/', null = True)

    class Meta:
        db_table = 'Bugs'


class UserCredit(models.Model):
    user_id = models.CharField(max_length=15)
    card_number = models.CharField(max_length=4,null=True, blank=True)
    name_on_card = models.CharField(max_length=30,null=True, blank=True)
    expiry = models.CharField(max_length=8, null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = 'UserCredits'


class Product(models.Model):
    part_number = models.CharField(max_length=15)
    name = models.CharField(max_length=30)
    monthly_basic_price = models.FloatField()
    monthly_professional_price = models.FloatField()
    yearly_basic_price = models.FloatField()
    yearly_professional_price = models.FloatField()

    class Meta:
        db_table = 'Products'


class Quotation(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    quotation_id = models.CharField(max_length=15)
    customer_id = models.CharField(max_length=15)
    partner_id = models.CharField(max_length=15)
    grand_total = models.FloatField()
    STATUS_CHOICES = (
        ('OR', 'Ordered'),
        ('OP', 'Open'),
    )
    status = models.CharField(max_length=2, choices=STATUS_CHOICES)
    file = models.FileField(upload_to='partner/quotation/', null = True)

    class Meta:
        db_table = 'Quotations'


class Deal(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    expiry_date = models.DateTimeField()
    quotation = models.ForeignKey(Quotation,  on_delete=models.SET_NULL, null=True, default=None, related_name='deal_quotation')
    customer_id = models.CharField(max_length=15)
    partner_id = models.CharField(max_length=15)
    grand_total = models.FloatField()
    STATUS_CHOICES = (
        ('APL', 'Applied'),
        ('APR', 'Approved'),
        ('ORD', 'Ordered'),
        ('CLS', 'Closed'),
        ('EXT', 'Extended'),
        ('EXP', 'Expired'),
        ('MIN', 'More Info Needed'),
    )
    status = models.CharField(max_length=2, choices=STATUS_CHOICES)
    more_info = models.TextField(null=True, blank=True)
    INCENTIVE_TYPE = (
        ('A', 'Type A'),
        ('B', 'Type B'),
    )
    incentive = models.CharField(max_length=2, choices=INCENTIVE_TYPE)
    discount = models.FloatField()

    class Meta:
        db_table = 'Deals'



class QuotationProduct(models.Model):
    quotation = models.ForeignKey(Quotation,  on_delete=models.SET_NULL, null=True, default=None, related_name='dealproduct_quotation')
    deal = models.ForeignKey(Deal,  on_delete=models.SET_NULL, null=True, default=None, related_name='dealproduct_deal')
    part_number = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='deal_product')
    TYPE_CHOICES = (
        ('F', 'Free'),
        ('B', 'Basic'),
        ('P', 'Professional'),
    )
    types_of_licenses = models.CharField(max_length=1, choices=TYPE_CHOICES)
    TERM_CHOICES = (
        ('M', 'Monthly'),
        ('Y', 'Yearly'),
    )
    term_of_licenses = models.CharField(max_length=1, choices=TERM_CHOICES)
    quantity = models.IntegerField(default=1)
    list_price = models.FloatField()
    net_price = models.FloatField()

    class Meta:
        db_table = 'Quotation_Products'


class Invoice(models.Model):
    number = models.CharField(max_length=15)
    customer_id = models.CharField(max_length=15)
    partner_id = models.CharField(max_length=15)
    updated_at = models.DateTimeField(auto_now=True)
    amount = models.FloatField()
    created_at = models.DateTimeField(auto_now_add=True)
    supporting_file = models.FileField(upload_to='customer/invoices/', null = True)

    class Meta:
        db_table = 'Invoices'


class License(models.Model):
    license_id = models.CharField(max_length=20)
    created_at = models.DateTimeField(auto_now_add=True)
    renewed_at = models.DateTimeField(auto_now_add=True)
    expiry_date = models.DateTimeField(auto_now_add=True)
    auto_renew = models.BooleanField(default=False)

    class Meta:
        db_table = 'Licenses'
