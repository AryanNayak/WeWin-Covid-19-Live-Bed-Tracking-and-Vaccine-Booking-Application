from django.shortcuts import render

# Create your views here.

@api_view(['GET'])
def apiOverview(request):
    api_urls = {
        'HospitalList': '/hospital-list/',
        'Hospital Detail ': '/Hospital-detail/<str:pk>/',
        'hospital': '/subject-hospital/',
        'hospitalUpdate': '/hospital-update/<str:pk>/',
        # 'Delete': '/subject-delete/<str:pk>/',
    }

    return Response(api_urls)




@ api_view(['POST'])
def userLogin(request, username, password):
    try:
        print('username=', username, 'password=', password)
        user = User.objects.get(username=username)
    except ObjectDoesNotExist:
        return Response(False)
    except:
        print("EXCEPTION")

    if(user.password == password):
        print("Password right")
        serializer = UserSerializer(user)
        if(serializer.is_valid):
            return Response(serializer.data)
        else:
            print("SERIALIZER NOT VALID")
    else:
        print("Password wrong")
        return Response(False)
    return Response(True)
