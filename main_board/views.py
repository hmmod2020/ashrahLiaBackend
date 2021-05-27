from django.shortcuts import render
from django.contrib.auth.models import User
from django.http.response import JsonResponse
from django.contrib import auth
from rest_framework.decorators import api_view, authentication_classes, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from django.http import HttpResponse
from .models import *
from rest_framework.authtoken.models import Token
from .serializers import user_infoSerializer,order_upSerializer
from rest_framework.authentication import BaseAuthentication, TokenAuthentication, SessionAuthentication,BasicAuthentication

from django.db.models import Q
# Create your views here.
my_token=None
def create_new_user(request):
    return render(request, 'login.html')


def create_new_user_backEnd(request):
    usre_name = request.POST['username']
    password = request.POST['password']
    email = request.POST['email']
    fristName = request.POST.get('fristName')
    lastName = request.POST.get('lastName')
    phone = request.POST.get('numpperPhone')
    place = request.POST.get('place')
    book1 = request.POST.get('book1')
    book2 = request.POST.get('book2')
    book3 = request.POST.get('book3')
    book4 = request.POST.get('book4')
    gender = request.POST.get('gender')

    user = User.objects.create_user(username=usre_name, password=password, email=email)
    user.save()
    myInfo = user_info(user=user, fristName=fristName,
                       lastName=lastName, numpper=phone,
                       place=place, book1=book1, book2=book2
                       , book3=book3, book4=book4, emile=email
                       , gender=gender)

    myInfo.save()
    token = Token.objects.create(user=user)
    return render(request, 'done.html')


def login_show(request):
    my_info = user_info.objects.all()
    con = {'data': my_info}

    return render(request, 'enter.html')


def show_user(request):
    crruntuser = request.user.id
    info = user_info.objects.get(user_id=crruntuser)
    email = info.emile
    return render(request, 'done.html', {'user': user_info.objects.get(user_id=crruntuser)})


def login(request):
    user_name = request.POST.get('username')
    password = request.POST.get('password')
    user = auth.authenticate(username=user_name, password=password)
    if user is not None:
        auth.login(request, user)
    return render(request, 'done.html')


def order_back(request):
    user_id = request.user.id
    my_info = user_info.objects.get(user_id=user_id)
    name = my_info.fristName + " " + my_info.lastName
    numperOrder = my_info.numpper
    placeO = my_info.place
    book1 = my_info.book1
    book2 = my_info.book2
    book3 = my_info.book3
    book4 = my_info.book4
    sup_want = request.POST.get('subject')
    setOrder = order_up(supject=sup_want, user=request.user, raelName_order=name
                        , place_order=placeO,
                        book1_order=book1, book2_order=book2, book3_order=book3, book4_order=book4
                        , nummper_order=numperOrder
                        )
    setOrder.save()

    return render(request, 'done.html')


def order_up_go(request):
    return render(request, 'UP_order.html')


def logout(request):
    auth.logout(request)

    return render(request, 'done.html')


def home(request):
    id = request.user
    my_info = user_info.objects.get(user=id)
    objects = order_up.objects.filter(supject=my_info.book1)
    objects2 = order_up.objects.all().filter(supject=my_info.book2)
    objects3 = order_up.objects.all().filter(supject=my_info.book3)
    objects4 = order_up.objects.all().filter(supject=my_info.book4)

    return render(request, 'home.html',
                  {'contnet1': objects, 'contnet2': objects2, 'contnet3': objects3, 'contnet4': objects4})


# api
@api_view(['GET'])
@authentication_classes([SessionAuthentication, BasicAuthentication])
@permission_classes([IsAuthenticated])
def homeapi(request):
    id = request.user
    my_info = user_info.objects.get(user=id)
    objects = order_up.objects.filter(Q(supject=my_info.book1)|Q(supject=my_info.book2)|Q(supject=my_info.book3)|Q(supject=my_info.book4))
    serializer1 = order_upSerializer(objects,many=True)
    return Response(serializer1.data)
    #return Response

@api_view(['GET','POST'])
@authentication_classes([SessionAuthentication, BasicAuthentication])
@permission_classes([IsAuthenticated])
def order_backapi(request):
    if request.method=='GET':
       quiry=order_up.objects.all()
       Serializer=order_upSerializer(quiry,many=True)
       return Response(Serializer.data)
    elif request.method=='POST':
       Serializer = order_upSerializer(data=request.data)
       if Serializer.is_valid():
           Serializer.save()
           return Response(Serializer.data)


@api_view(['GET'])
@authentication_classes([SessionAuthentication, BasicAuthentication])
@permission_classes([IsAuthenticated])
def showToken(request):
    content = {
        'user': str(request.user),  # `django.contrib.auth.User` instance.
        'auth': str(request.auth),  # None
    }
    return Response(content)

@api_view(['POST'])
def loginapi(request):
    user_name = request.data['username']
    password = request.data['password']
    user = auth.authenticate(username=user_name, password=password)
    if user is not None:
        token= Token.objects.get_or_create(user=user)
        my_token=token
        auth.login(request, user)
        print(token)
        return Response("successful login")
    else:
        return Response("wrong username or password")

@api_view(['POST'])
def create_new_user_backEndapi(request):
    usre_name = request.data['username']
    password = request.data['password']
    email = request.data['email']
    fristName = request.data['fristName']
    lastName = request.data['lastName']
    phone = request.data['numpperPhone']
    place = request.data['place']
    book1 = request.data['book1']
    book2 = request.data['book2']
    book3 = request.data['book3']
    book4 = request.data['book4']
    gender = request.data['gender']

    user = User.objects.create_user(username=usre_name, password=password, email=email)
    user.save()
    myInfo = user_info(user=user, fristName=fristName,
                       lastName=lastName, numpper=phone,
                       place=place, book1=book1, book2=book2
                       , book3=book3, book4=book4, emile=email
                       , gender=gender)

    myInfo.save()
    Token.objects.create(user=user)
    return Response(request.data)
@api_view(['GET'])
@authentication_classes([SessionAuthentication, BasicAuthentication])
@permission_classes([IsAuthenticated])
def show_my_info_api(request):
    id = request.user.id
    print(id)
    my_info = user_info.objects.get(user_id=id)
    serrializer=user_infoSerializer(my_info)
    data=serrializer.data
    return Response(data)



@api_view(['POST','GET'])
@authentication_classes([SessionAuthentication, BasicAuthentication])
@permission_classes([IsAuthenticated])
def search_api(request):
    if request.method=='POST':
        subject=request.data['subject']
        quiry = order_up.objects.filter(~Q(user=request.user.id)&Q(book1_order=subject)|Q(book2_order=subject)|Q(book3_order=subject)|Q(book4_order=subject))
        Serializer = order_upSerializer(quiry, many=True)

        if not quiry:
            user_id = request.user.id
            my_info = user_info.objects.get(user_id=user_id)
            name = my_info.fristName + " " + my_info.lastName
            numperOrder = my_info.numpper
            placeO = my_info.place
            book1 = my_info.book1
            book2 = my_info.book2
            book3 = my_info.book3
            book4 = my_info.book4
            data = {
                "supject": subject,
                "user": user_id,
                "raelName_order": name,
                "place_order": placeO,
                "book1_order": book1,
                "book2_order": book2,
                "book3_order": book3,
                "book4_order": book4,
                "nummper_order": numperOrder,
            }

            Serializer = order_upSerializer(data=data)
            if Serializer.is_valid():
                Serializer.save()
            return Response(Serializer.data)

        else:

            return Response(Serializer.data)
    else:
        return Response('you can search')


@api_view(['POST','GET','PUT'])
@authentication_classes([SessionAuthentication, BasicAuthentication])
@permission_classes([IsAuthenticated])
def updat_my_inf(request):
    user_id = request.user.id
    my_info = user_info.objects.get(user_id=user_id,)
    serializer = user_infoSerializer(my_info,many=False)

    if request.method=='PUT':

        data = {
            "id":my_info.id ,
            "lastName": my_info.lastName,
            "fristName":request.data['fristName'],
            "emile":request.data['emile'] ,
            "numpper": request.data['numpper'],
            "book1": request.data['book1'],
            "book2":request.data['book2'],
            "book3": request.data['book3'],
            "book4": request.data['book4'],
            "gender": my_info.place,
            "place":  my_info.gender,
            "image": None,
            "user": user_id
        }
        serializer = user_infoSerializer(my_info,data=data)
        if serializer.is_valid():
            serializer.save()
        else:
            return Response(serializer.errors)
        return Response(serializer.data)

    elif request.method=='GET':
        print(my_info.id)
        return Response(serializer.data)