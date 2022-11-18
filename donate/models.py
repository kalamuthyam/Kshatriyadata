from django.db import models


class Subscribers(models.Model):
    mobile = models.CharField(db_column='Mobile', max_length=15, blank=True, null=True)  # Field name made lowercase.
    otp = models.CharField(db_column='Otp', max_length=15, blank=True, null=True)  # Field name made lowercase.
    name = models.CharField(db_column='Name', max_length=45, blank=True, null=True)  # Field name made lowercase.
    surname = models.CharField(db_column='Surname', max_length=45, blank=True, null=True)  # Field name made lowercase.
    address1 = models.CharField(db_column='Address1', max_length=250, blank=True, null=True)  # Field name made lowercase.
    email = models.CharField(db_column='Email', max_length=100, blank=True, null=True)  # Field name made lowercase.
    otherinfo = models.CharField(db_column='Otherinfo', max_length=250, blank=True, null=True)  # Field name made lowercase.
    cnfdonate = models.CharField(db_column='Cnfdonate', max_length=45, blank=True, null=True)  # Field name made lowercase.
    amount = models.CharField(db_column='Amount', max_length=45, blank=True, null=True)  # Field name made lowercase.
    datasubmetby = models.CharField(db_column='Datasubmetby', max_length=45, blank=True, null=True)  # Field name made lowercase.
    agentmobile = models.CharField(db_column='Agentmobile', max_length=15, blank=True, null=True)  # Field name made lowercase.
    date = models.DateTimeField(blank=True, null=True)
    address2 = models.CharField(db_column='Address2', max_length=250, blank=True, null=True)  # Field name made lowercase.
    nickname = models.CharField(max_length=45, blank=True, null=True)
    area = models.CharField(max_length=45, blank=True, null=True)
    city = models.CharField(max_length=45, blank=True, null=True)
    state = models.CharField(max_length=45, blank=True, null=True)
    pincode = models.CharField(max_length=45, blank=True, null=True)
    native = models.CharField(max_length=100, blank=True, null=True)
    gotra = models.CharField(max_length=45, blank=True, null=True)
    bloodgroup = models.CharField(max_length=45, blank=True, null=True)
    dob = models.DateTimeField(blank=True, null=True)
    age = models.CharField(max_length=45, blank=True, null=True)
    district = models.CharField(max_length=45, blank=True, null=True)
    image = models.TextField(blank=True, null=True)
    termsandconditions = models.IntegerField(blank=True, null=True)
    relationship = models.CharField(max_length=45, blank=True, null=True)
    membertype = models.CharField(max_length=10, blank=True, null=True)


    class Meta:
        managed = False
        db_table = 'subscribers'


class Login(models.Model):
    di = models.AutoField(primary_key=True)
    mobile = models.CharField(max_length=15, blank=True, null=True)
    password = models.CharField(max_length=45, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'login'


class Surname(models.Model):
    surname = models.CharField(max_length=100, blank=True, null=True)
    gotram = models.CharField(max_length=100, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'surname'

class Image(models.Model):
    imagepk = models.IntegerField(primary_key=True)
    processes = models.CharField(max_length=100)
    userid = models.IntegerField(db_column='userId', blank=True, null=True)  # Field name made lowercase.
    image = models.CharField(max_length=100, blank=True, null=True)
    status = models.CharField(max_length=100, blank=True, null=True)
    comment = models.TextField(blank=True, null=True)
    created_timestamp = models.DateTimeField(blank=True, null=True)
    updated_timestamp = models.DateTimeField(blank=True, null=True)
    descripts = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'image'


# ---------------------grain-------------------------------------

class Supplier(models.Model):
    suppliername = models.CharField(max_length=250, blank=True, null=True)
    address = models.CharField(max_length=250, blank=True, null=True)
    city = models.CharField(max_length=50, blank=True, null=True)
    state = models.CharField(max_length=50, blank=True, null=True)
    dist = models.CharField(max_length=50, blank=True, null=True)
    pin = models.CharField(max_length=10, blank=True, null=True)
    mobile = models.CharField(max_length=15, blank=True, null=True)
    gstno = models.CharField(max_length=20, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'supplier'

class Customers(models.Model):
    customername = models.CharField(max_length=250, blank=True, null=True)
    address = models.CharField(max_length=250, blank=True, null=True)
    city = models.CharField(max_length=45, blank=True, null=True)
    state = models.CharField(max_length=45, blank=True, null=True)
    mobile = models.CharField(max_length=15, blank=True, null=True)
    pin = models.CharField(max_length=10, blank=True, null=True)
    gstnumber = models.CharField(max_length=20, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'customers'

class Products(models.Model):
    productname = models.CharField(max_length=250, blank=True, null=True)
    productcode = models.CharField(max_length=45, blank=True, null=True)
    brand = models.CharField(max_length=45, blank=True, null=True)
    size = models.CharField(max_length=15, blank=True, null=True)
    price = models.CharField(max_length=45, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'products'