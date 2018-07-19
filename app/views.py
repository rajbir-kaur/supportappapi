# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from .models import *
from rest_framework.views import APIView
from rest_framework import permissions
from rest_framework.response import Response
from rest_framework import status
from .helpers import *

# Create your views here.

class Register(APIView):
    permissions = (permissions.AllowAny,)

    def get(self, request):
	try:
	    qp = {x.split("=")[0]:x.split("=")[-1] for x in self.request.META["QUERY_STRING"].split("&") if x};logger.info(qp)
	    if not qp: raise
	    elif not "imei" in qp.keys(): raise
	    elif "latest" in qp.keys() and qp["latest"]: 
		obj=RegisterModel.objects(device_imei=qp["imei"]).order_by("-time_stamp").first();obj = [obj]
	    else: obj=RegisterModel.objects(device_imei=qp["imei"])
	    return Response(clean(obj),status=status.HTTP_200_OK)
	except:
	    return Response(sf,status=status.HTTP_400_BAD_REQUEST)

    def post(self, request):
	try:
	    logger.info(request.data)
	    data = request.data.copy()
	    RegisterModel(**data).save()
	    return Response(st,status=status.HTTP_200_OK)
	except:
	    return Response(sf,status=status.HTTP_400_BAD_REQUEST)
