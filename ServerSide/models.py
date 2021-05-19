from django.db import models

# Create your models here.
# Station
class Stations(models.Model):
    stationName     = models.CharField(max_length=100)
    stationLocation = models.CharField(max_length=100)
    stationStaffId  = models.CharField(max_length=100)
    date  = models.DateTimeField(auto_now_add=True)

    def __str_(self):
        return self.stationName

# Customers
class Customers(models.Model):
    customerName     = models.CharField(max_length=100)
    customerPhone    = models.CharField(max_length=100)
    customerId       = models.CharField(max_length=100)
    customerStartLoc = models.CharField(max_length=100)
    customerDestinationLoc = models.CharField(max_length=100)
    stationStaffId  = models.CharField(max_length=100)
    date            = models.DateTimeField(auto_now_add=True)

    def __str_(self):
        return self.customerName

# Items
class Items(models.Model):
    itemName = models.CharField(max_length=100)
    itemType = models.CharField(max_length=100)
    Quantity = models.CharField(max_length=100)
    originStation = models.CharField(max_length=100)
    originCounty = models.CharField(max_length=100)
    receiverName = models.CharField(max_length=100)
    receiverPhone = models.CharField(max_length=100)
    destinationAddress = models.CharField(max_length=100)
    destinationCounty = models.CharField(max_length=100)
    dateSend= models.CharField(max_length=100)
    dateExpected = models.CharField(max_length=100)

    def __str__(self):
        return self.itemName

# Payments
class Payments(models.Model):
    customerPhone        = models.CharField(max_length=100)
    paymentAmount        = models.CharField(max_length=100)
    paymentMeans         = models.EmailField(max_length=100)
    code                 =  models.CharField(max_length=100)
    date                 = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.customerPhone





