import base64
import datetime
import urllib
from django.db import connection
import os
import json

from rest_framework import status

from .models import Subscribers
from .serializers import *
from rest_framework.decorators import api_view
from django.shortcuts import (get_object_or_404,
                              render,
                              HttpResponseRedirect,redirect)
from rest_framework.response import Response
from django.contrib import messages
# import schedule
# import time

# -------
from django.db.models.expressions import RawSQL, F
# from oauth2_provider.contrib.rest_framework import OAuth2Authentication
from django.shortcuts import render, HttpResponse
from django.contrib.auth.models import User
from django.conf import settings
from rest_framework.pagination import PageNumberPagination
from rest_framework.viewsets import ModelViewSet

# from .fcm_fun import onedevice
from .serializers import *
from django.db import connection
from django.db.models import Q
from rest_framework.response import Response
from rest_framework.renderers import JSONRenderer
# from rest_framework_xml.renderers import XMLRenderer
from rest_framework.decorators import api_view
from rest_framework.views import APIView
import collections
from rest_framework import status
from django.core import serializers
from decimal import *
import base64
# import mysql.connector
# from mysql.connector import MySQLConnection
import json
from rest_framework.decorators import authentication_classes, permission_classes, renderer_classes
from rest_framework import generics
from rest_framework.authtoken.models import Token
import urllib
from django.core.mail import send_mail
# import onetimepass as otp
# from passlib.totp import TOTP
import datetime as dt1
import sched, time
import random
import sched
# import pandas as pd
# from pandas.io import sql
from .models import *
# from .tasks import *
from rest_framework.permissions import IsAuthenticated, IsAuthenticatedOrReadOnly  # OAuth2Authentication
# from rest_framework.authentication import OAuth2Authentication
# import pandas as pd
# import boto3
import sys
import re
from rest_framework.parsers import FileUploadParser
import os
# from boto3.s3.transfer import S3Transfer
from .models import Image as Im
from django.db.models import Avg, Count, Min, Sum
# from rest_framework.renderers import JSONRendere
# from .serializers import TransportMasterserializer
# fgfgdfhgghhg
# from fcm_fun import *

from django.db.models.signals import post_save
# from App.signals import *
# from google_play_scraper import app
from decimal import Decimal
from rest_framework.views import APIView
from rest_framework.parsers import MultiPartParser, FormParser, JSONParser
from rest_framework.response import Response
from rest_framework import status

def create_dict_from_cursor1(cursor):
    rows = cursor.fetchall()
    # DEBUG settings (used to) affect what gets returned.
    return [json.loads(item[0]) for item in rows]

def create_dict_from_cursor(cursor):
    rows = cursor.fetchall()
    # DEBUG settings (used to) affect what gets returned.
    DEBUG = False
    if DEBUG:
        desc = [item[0] for item in cursor.cursor.description]
    else:
        desc = [item[0] for item in cursor.description]
    return [dict(zip(desc, item)) for item in rows]

def exe_an_sp(sp):
    cursor = connection.cursor()
    cursor.execute(sp)
    return create_dict_from_cursor(cursor)

def call_an_sp(sp, var):
    cursor = connection.cursor()
    cursor.callproc(sp, var)
    return create_dict_from_cursor(cursor)

import math, random

def generateOTP():
    digits = "0123456789"
    OTP = ""
    for i in range(4):
        OTP += digits[math.floor(random.random() * 10)]
    return OTP


@api_view(['POST', ])
def drop123(request):
    data = request.data
    # print(data['mobile'])
    # m = Subscribers.objects
    # g = Subscribers.objects.filter(mobile = data['mobile'])
    # if g.exists():
    #     x = """select * from Subscribers where mobile = '{}' order by id desc""".format(data['mobile'])
    #     otp = ''
    #     y = '0'
    # else:
        # sc = Subscribers.objects.create(mobile = data['mobile'],otp = generateOTP())
    otp = generateOTP()
    x = """select * from Subscribers where mobile = '{}' and membertype = 'primary' order by id desc""".format(data['mobile'])
    y = '1'
    # msg = "{0} is OTP for Data updating of Vanabhojana Committee, Hyderabad.".format(otp)
    msg = "Dear {0}, Thanks for the Donation of {0} Rupees to Kshatriya Vanabhojanalu-2022.".format(otp)
    print('2')
    url = "https://2factor.in/API/R1/"
    values = {'module': 'TRANS_SMS',
              'apikey': '0f045e86-fca4-11ea-9fa5-0200cd936042',
              'to': data['mobile'],
              'from': 'KKVHYD',
              'msg': msg
              }
    data = urllib.parse.urlencode(values)
    data = data.encode('utf-8')
    print(data)
    f = urllib.request.urlopen(url, data)
    print(f, 'totalurl')
    fe = f.read().decode('utf-8')
    return Response({'data':exe_an_sp(x),'status' : y,'otp':otp})

from datetime import datetime

@api_view(['POST', ])
def inssubcribers(request):
    data = request.data
    # print(data)
    if data['membertype'] == 'Primary':
        print('1')
        g = Subscribers.objects.filter(mobile=data['mobile'],name=data['name'])
        if g.exists():
            print('2')
            sc = g.update(mobile=data['mobile'], name=data['name'], surname=data['surname'],
                                            address1=data['address1'],
                                            email=data['email'], otherinfo=data['otherinfo'],
                                            cnfdonate=data['cnfdonate'], amount=data['amount'],
                                            datasubmetby=data['datasubmetby'], agentmobile=data['agentmobile'],
                                            date=datetime.now(),
                                            address2=data['address2'], nickname=data['nickname'], area=data['area'],
                                            city=data['city'],
                                            state=data['state'], pincode=data['pincode'], native=data['native'],
                                            gotra=data['gotra'], bloodgroup=data['bloodgroup'],
                                            dob=data['dob'], age=data['age'], district=data['district'],
                                            image=data['image'],
                                            termsandconditions=data['termsandconditions'],
                                            relationship=data['relationship'], membertype=data['membertype'])
        else:
            print('3')
            sc = Subscribers.objects.create(mobile=data['mobile'],name = data['name'],surname = data['surname'],address1 = data['address1'],
                                        email = data['email'],otherinfo = data['otherinfo'],cnfdonate = data['cnfdonate'],amount = data['amount'],
                                        datasubmetby = data['datasubmetby'],agentmobile = data['agentmobile'],date = datetime.now(),
                                        address2 = data['address2'],nickname = data['nickname'],area = data['area'],city = data['city'],
                                        state = data['state'],pincode = data['pincode'],native = data['native'],gotra = data['gotra'],bloodgroup = data['bloodgroup'],
                                        dob = data['dob'],age = data['age'],district = data['district'],image = data['image'],
                                        termsandconditions = data['termsandconditions'],relationship = data['relationship'],membertype = data['membertype'])
    if data['membertype'] == 'Secondary':
        print('4')
        g = Subscribers.objects.filter(mobile=data['mobile'],name = data['name'])
        if g.exists():
            print('5')
            sc = g.update(mobile=data['mobile'], name=data['name'], surname=data['surname'],
                                            address1=data['address1'],
                                            email=data['email'], otherinfo=data['otherinfo'],
                                            cnfdonate=data['cnfdonate'], amount=data['amount'],
                                            datasubmetby=data['datasubmetby'], agentmobile=data['agentmobile'],
                                            date=datetime.now(),
                                            address2=data['address2'], nickname=data['nickname'], area=data['area'],
                                            city=data['city'],
                                            state=data['state'], pincode=data['pincode'], native=data['native'],
                                            gotra=data['gotra'], bloodgroup=data['bloodgroup'],
                                            dob=data['dob'], age=data['age'], district=data['district'],
                                            image=data['image'],
                                            termsandconditions=data['termsandconditions'],
                                            relationship=data['relationship'], membertype=data['membertype'])
        else:
            sc = Subscribers.objects.create(mobile=data['mobile'], name=data['name'], surname=data['surname'],
                                            address1=data['address1'],
                                            email=data['email'], otherinfo=data['otherinfo'],
                                            cnfdonate=data['cnfdonate'], amount=data['amount'],
                                            datasubmetby=data['datasubmetby'], agentmobile=data['agentmobile'],
                                            date=datetime.now(),
                                            address2=data['address2'], nickname=data['nickname'], area=data['area'],
                                            city=data['city'],
                                            state=data['state'], pincode=data['pincode'], native=data['native'],
                                            gotra=data['gotra'], bloodgroup=data['bloodgroup'],
                                            dob=data['dob'], age=data['age'], district=data['district'],
                                            image=data['image'],
                                            termsandconditions=data['termsandconditions'],
                                            relationship=data['relationship'], membertype=data['membertype'])
    if data['cnfdonate'] == 'Yes':
        msg = "Dear {}, Thanks for the Donation of {} Rupees to Kshatriya Vanabhojanalu-2022.".format(data['name'],data['amount'])
        print('2')
        url = "https://2factor.in/API/R1/"
        values = {'module': 'TRANS_SMS',
                  'apikey': '0f045e86-fca4-11ea-9fa5-0200cd936042',
                  'to' : data['mobile'],
                  'from' : 'KKVHYD',
                  'msg': msg
                  }
        data = urllib.parse.urlencode(values)
        data = data.encode('utf-8')
        print(data)
        f = urllib.request.urlopen(url, data)
        print(f,'totalurl')
        fe = f.read().decode('utf-8')
    return Response({'status':'Done'})

@api_view(['GET', ])
def getsurname(request):
    x = """SELECT distinct surname as Surname FROM surname"""
    return Response(exe_an_sp(x))

@api_view(['GET', ])
def drop12(request):
    x = """SELECT distinct surname as Surname,gotram FROM surname"""
    return Response(exe_an_sp(x))

@api_view(['GET', ])
def getareaname(request):
    x = """SELECT distinct area,city,state,pincode FROM subscribers"""
    return Response(exe_an_sp(x))

@api_view(['POST', ])
def login(request):
    data = request.data
    g = Login.objects.filter(mobile = data['mobile'],password = data['password'])
    if g.exists():
        # otp = generateOTP()
        # msg = "Dear {0}, Thanks for the Donation of {0} Rupees to Kshatriya Vanabhojanalu-2022.".format(otp)
        # url = "https://2factor.in/API/R1/"
        # values = {'module': 'TRANS_SMS',
        #           'apikey': '0f045e86-fca4-11ea-9fa5-0200cd936042',
        #           'to': data['mobile'],
        #           'from': 'KKVHYD',
        #           'msg': msg
        #           }
        # data = urllib.parse.urlencode(values)
        # data = data.encode('utf-8')
        # print(data)
        # f = urllib.request.urlopen(url, data)
        # print(f, 'totalurl')
        # fe = f.read().decode('utf-8')
        x = "Success"
    else:
        x = "Failed"
        # otp = ''
    return Response({'status' : x})

@api_view(['GET', ])
def getreport(request):
    xdate = request.query_params.get('param_other1')
    ydate = request.query_params.get('param_other2')
    xarea = request.query_params.get('param_other3')
    xcity = request.query_params.get('param_other4')
    xstate = request.query_params.get('param_other5')
    xsurname = request.query_params.get('param_other6')
    xnickname = request.query_params.get('param_other7')
    x = call_an_sp('get_report',(xdate,ydate,xarea,xcity,xstate,xsurname,xnickname,))
    return Response({'data' : x })

@api_view(['GET', ])
def getarea(request):
    x = call_an_sp('get_area',())
    return Response({'data' : x })

@api_view(['GET', ])
def getcity(request):
    x = call_an_sp('get_city',())
    return Response({'data' : x })

@api_view(['GET', ])
def getstate(request):
    x = call_an_sp('get_state',())
    return Response({'data' : x })

@api_view(['POST', ])
def gsupplierins(request):
    data = request.data
    p = Supplier.objects.create(**data)
    return Response({'Status' : 'success' })


@api_view(['POST', ])
def gcustomerins(request):
    data = request.data
    p = Customers.objects.create(**data)
    return Response({'Status' : 'success' })

@api_view(['POST', ])
def gproductins(request):
    data = request.data
    p = Products.objects.create(**data)
    return Response({'Status' : 'success' })

@api_view(['GET', ])
def ggetcustomer(request):
    x = """select * from customers"""
    return Response({'data' : exe_an_sp(x) })


# @api_view(['POST', ])
# def FileUploadView(request):
#     data = request.data
#     try:
#         if 'data:' in data['image'] and ';base64,' in data['image']:
#             header, data2 = data['image'].split(';base64,')
#             if header.split('/')[1] in (
#             "jpg", "jpeg", "png", "doc", "docx", "pdf", "txt","vnd.openxmlformats-officedocument.wordprocessingml.document",
#             "vnd.ms-excel", "vnd.openxmlformats-officedocument.spreadsheetml.sheet","plain"):
#                 try:
#                     import uuid
#                     extension = header.split('/')[1]
#                     if extension == "vnd.ms-excel":
#                         extension = "xls"
#                     elif extension == "vnd.openxmlformats-officedocument.wordprocessingml.document":
#                         extension = "docx"
#                     elif extension == "vnd.openxmlformats-officedocument.spreadsheetml.sheet":
#                         extension = "xlsx"
#                     elif extension == "msword":
#                         extension = "doc"
#                     elif extension == "plain":
#                         extension = "txt"
#                     print(uuid)
#                     print(str(uuid.uuid4())[:12])
#                     file_name = 'media/' + str(uuid.uuid4())[:12] + '.' + extension
#                     decoded_file = base64.b64decode(data2)
#                     # f = open(file_name, 'wb')
#                     # f.write(decoded_file)
#                     # f.close()
#                     with open(file_name, 'wb') as f:
#                         f.write(decoded_file)
#                     data['image'] = '/' + file_name
#                     serializer = ImageSerializer(data=data)
#                     if serializer.is_valid():
#                         serializer.save()
#                         return Response(serializer.data)
#                     else:
#                         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
#                 except TypeError:
#                     return Response('Invalid file')
#             else:
#                 return Response({"status": 0, "msg": "Invalid file format"}, status=status.HTTP_400_BAD_REQUEST)
#     except Exception as e:
#         print(e)
#         return Response(e)

@api_view(['GET', ])
def getseclist(request):
    param_other1 = request.query_params.get('param_other1')
    x = """SELECT * FROM subscribers where mobile = '{}' and membertype = 'Secondary'""".format(param_other1)
    return Response(exe_an_sp(x))