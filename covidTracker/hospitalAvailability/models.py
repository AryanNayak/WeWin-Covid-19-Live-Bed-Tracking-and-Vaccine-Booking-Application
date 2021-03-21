from django.db import models

# Create your models here.


# class User(models.Model):
#     userName = models.CharField(max_length=50)
#     userID = models.AutoField(primary_key=True)
#     userLocation = 

class State(models.Model):
    stateName = models.CharField(max_length=20)
    def __str__(self):
        return self.stateName

class Hospitals(models.Model):
    hospitalName = models.CharField(max_length=50)
    hospitalID = models.AutoField(primary_key=True)
    hospitalState = models.ForeignKey(State, on_delete=models.CASCADE)
    hospitalAddress = models.CharField(max_length=200)
    bedsOccupied = models.IntegerField()
    totalBeds = models.IntegerField()
    hospitalPassword = models.CharField(max_length=20)
    numberOfVaccines = models.IntegerField(default=0)
    def getHospitals(state):
        hospitals = Hospitals.objects.all().filter(hospitalState=state)
        return hospitals
    def __str__(self):
        return self.hospitalName
class Patient(models.Model):
    

    patientName = models.CharField(max_length=50)
    patientID = models.IntegerField(primary_key=True)
    hospitalID = models.ForeignKey(Hospitals, on_delete=models.CASCADE)
    lastChecked = models.DateTimeField(  auto_now_add=True)

    bpHigh = models.IntegerField()
    bpLow = models.IntegerField()
    sugar = models.IntegerField()
    heartRate = models.IntegerField()
    oxygenRate = models.IntegerField()
    stability = models.BooleanField()



    def __str__(self):
        return self.patientName, self.hospitalID


class vaccinationAppointment(models.Model):
    patient = models.ForeignKey(Patient, on_delete=models.CASCADE)
    hospital = models.ForeignKey(Hospitals, on_delete=models.CASCADE)
    doseNo = models.IntegerField()  
    firstAppointmentDate = models.DateField()
    #TODO secondAppointmentDate = models.DateField(default=firstAppointmentDate+28 days)

    # TODO emailID = models.EmailField()
    # OTP
    





