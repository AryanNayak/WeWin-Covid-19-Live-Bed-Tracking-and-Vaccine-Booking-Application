from django.db import models

# Create your models here.


# class User(models.Model):
#     userName = models.CharField(max_length=50)
#     userID = models.AutoField(primary_key=True)
#     userLocation = 

class State(models.Model):
    stateName = models.CharField(max_length=20)


class Hospitals(models.Model):
    hospitalName = models.CharField(max_length=50)
    hospitalID = models.AutoField(primary_key=True)
    hospitalState = models.ForeignKey(State, on_delete=models.CASCADE)
    hospitalAddress = models.CharField(max_length=200)
    bedsOccupied = models.IntegerField()
    totalBeds = models.IntegerField()
    hospitalPassword = models.CharField(max_length=20)
    def getHospitals(state):
        hospitals = Hospitals.objects.all().filter(hospitalState=state)
        return hospitals

class Patient(models.Model):
    patientName = models.CharField(max_length=50)
    patientID = models.AutoField(primary_key=True)
    hospitalID = models.ForeignKey(Hospitals, on_delete=models.CASCADE)
    lastChecked = models.DateTimeField()
    bpHigh = models.IntegerField()
    bpLow = models.IntegerField()
    sugar = models.IntegerField()
    heartRate = models.IntegerField()
    oxygenRate = models.IntegerField()
    tability = models.BooleanField()


    



