from django.shortcuts import render
from django.http import JsonResponse

from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import HospitalSerializer, PatientSerializer, StateSerializer

from .models import Hospitals, State, Patient, State
# Create your views here.


# Create your views here.

@api_view(['GET'])
def apiOverview(request):
    api_urls = {
        'HospitalList': '/hospital-list/',
        'Hospital Detail ': '/Hospital-detail/<str:pk>/',
        'hospital': '/hospitalCreate/',
        'hospitalUpdate': '/hospital-update/<str:pk>/',
    }

    return Response(api_urls)




@ api_view(['GET'])
def hospitalLogin(request, hospitalID, password):
    try:
        print('hospitalID=', hospitalID, 'password=', password)
        hospital = Hospitals.objects.get(hospitalID=hospitalID)
    except ObjectDoesNotExist:
        return Response(False)
    except:
        print("EXCEPTION")

    request.session['hospitalID'] = hospitalID
    print(request.session['hospitalID'])
    if(hospital.hospitalPassword == password):
        print("Password right")
        serializer = HospitalSerializer(hospital)
        if(serializer.is_valid):
            return Response(serializer.data)
        else:
            print("SERIALIZER NOT VALID")
    else:
        print("Password wrong")
        return Response(False)
    
    return Response(True)

@ api_view(['POST'])
def hospitalRegistration(request):
    import json
    print("HELLO")
    print(request.data)
    serializer = HospitalSerializer(data=request.data)
    print(serializer)
    if serializer.is_valid():
        request.session['hospitalID'] = serializer.data['hospitalID']

        
        serializer.save()
    else:
        print("SERIALIZER VALID:",serializer.is_valid())
        print("SERIA",serializer.errors)
    # serializer.data.id
    return Response(serializer.data)


# {
#     "hospitalName": "BKC",
#     "hospitalAddress": "BANDRA",
#     "bedsOccupied": 100,
#     "totalBeds": 1000,
#     "hospitalPassword": "password",
#     "hospitalState": "Maharashtra"
# }



@api_view(['GET'])
def hospitalList(request, state):
    # username = User.objects.get(username=username)
    # print(username)
    # usernameOfFollowing = Follow.objects.get(follower=username)
    # print(type(username))
    # print(username.append(usernameOfFollowing))

#  or username = usernameOfFollowing
    # posts = Posts.objects.all().filter(username=username)
    hospitals = Hospitals.getHospitals(state)
    # print("username3:",username,"Posts are:")
    # print("HELLO",i)
    # for i in hospitals:
        # print(i.hospitalName)
    serializer = HospitalSerializer(hospitals, many=True)
    # print(serializer.data)
    return Response(serializer.data)





@api_view(['GET'])
def hospitalDetail(request, hospitalID):
    # posts = Posts.objects.all().filter(username=username)
    hospital = Hospitals.objects.filter(hospitalID=hospitalID)
    # for i in hospitals:
        # print(i.hospitalName)
    serializer = HospitalSerializer(hospital    , many=True)
    return Response(serializer.data)










@api_view(['POST'])
def hospitalUpdate(request, hospitalID, added):
    # patient added/dischared
    # if patient is added register him
    # decrmenent total beds
    if(int(added)==1):
        # print(request.data)
        serializer = PatientSerializer(data=request.data)
        print(serializer) 
        serializer.is_valid()
        # new_dict={"patientID":Patient.objects.all().order_by("-patientID")[0].patientID+1}
        # new_dict.update(serializer)
        patientID=Patient.objects.all().order_by("-patientID")[0].patientID+1
        print(serializer.data)
        # serializer = new_dict
        import datetime
        hospital = Hospitals.objects.get(hospitalID= serializer.data['hospitalID'])
        patient = Patient.objects.create(patientName=serializer.data['patientName'], 
        patientID=patientID,
        
        hospitalID= hospital,
        lastChecked=datetime.datetime.now(),
         bpHigh=serializer.data['bpHigh'],
         bpLow= serializer.data['bpLow'],
         sugar= serializer.data['sugar'],
         heartRate= serializer.data['heartRate'],
         oxygenRate= serializer.data['oxygenRate'],
         stability= serializer.data['stability'])
        patient.save()
    #     if serializer.is_valid():
    #         serializer.save()
    #         # hospitalID=serializer.data.hospitalID
    #         # update hospital beds
    #         Hospitals.objects.filter(hospitalID=hospitalID).update(bedsOccupied= Hospitals.objects.filter(hospitalID=hospitalID)[0].bedsOccupied+1)

    #     else:
    #         print("SERIALIZER VALID:",serializer.is_valid())
    #         print("SERIA",serializer.errors)
    #     # serializer.data.id
    #     return Response(serializer.data)
    # print("Not saved")
    return Response(1)
#     {
# "patientName":"Sushant Mehta",
# "hospitalID":1,
# "bpHigh":100,
# "bpLow":100,
# "sugar":100,
# "heartRate":100,
# "oxygenRate":100,
# "stability":true
# }




@api_view(['POST'])
def patientHealthUpdate(request):
    serializer = PatientSerializer(data=request.data)
    if serializer.is_valid():
        print(serializer.data['patientID'])
        # TODO UPDATE THE ROW
        patient = serializer.data['patientID']
        
        Patient.objects.filter(patientID=patient).delete()
        serializer.save()
        
    # else:
    #     print("SERIALIZER VALID:",serializer.is_valid())
    #     print("SERIA",serializer.errors)
    # # serializer.data.id
    return Response(serializer.data)
    

# @api_view(['POST'])
# def vaccinationBook(request):
    

@api_view(['GET'])
def updateBeds(request, hospitalID, incr):
    # if(incr
    # )
    # currentBeds = Hospitals.objects.filter(hospitalID=hospitalID)[0].bedsOccupied
    # Hospitals.objects.
    hospital = Hospitals.objects.get(hospitalID=hospitalID)
    hospital.bedsOccupied+=incr
    hospital.save(update_fields=['bedsOccupied'])
    serializer=HospitalSerializer(hospital)
    return Response(serializer.data)

    












