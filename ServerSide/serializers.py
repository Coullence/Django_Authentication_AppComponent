from rest_framework import serializers
from .models import Stations,Customers, Items, Payments

# Stations
class StationsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Stations
        fields = ['id','stationName','stationLocation','stationStaffId','date']

# Customers
class CustomersSerializer(serializers.ModelSerializer):
    class Meta:
        model = Customers
        fields = ['id','customerName','customerPhone','customerId','customerStartLoc','customerDestinationLoc','stationStaffId','date' ]           

# Items
class ItemsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Items
        fields = ['id','itemName','itemType','Quantity','originStation','originCounty','receiverName','receiverPhone','destinationAddress','destinationCounty','dateSend','dateExpected']
    
    

# Payments
class PaymentsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Payments
        fields = ['id','customerPhone','paymentAmount','paymentMeans','code','date' ]


                  


    

    # def __str__(self):
    #     return 

    # def __unicode__(self):
    #     return 

