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


# {
# hospitalName: "BKC",
# hospitalState:"Maharashtra",
# hospitalAddress:"BANDRA",
# bedsOccupied:100,
# hospitalPassword:"password",
# totalBeds:1000,
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
    # username = User.objects.get(username=username)
    # print(username)
    # usernameOfFollowing = Follow.objects.get(follower=username)
    # print(type(username))
    # print(username.append(usernameOfFollowing))

#  or username = usernameOfFollowing
    # posts = Posts.objects.all().filter(username=username)
    hospital = Hospitals.objects.filter(hospitalID=hospitalID)
    # print("username3:",username,"Posts are:")
    # print("HELLO",i)
    # for i in hospitals:
        # print(i.hospitalName)
    serializer = HospitalSerializer(hospital    , many=True)
    # print(serializer.data)
    return Response(serializer.data)