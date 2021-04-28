import datetime
import string
import random

from django.shortcuts import render
import requests
from rest_framework import viewsets
from rest_framework.response import Response

from swlab4.swlab4.models import Client
from swlab4.swlab4.models import Admin

from swlab4.swlab4.client_views import *
from swlab4.swlab4.admin_views import *

services_unavailability = {"client-login": 0,
                           "client-register": 0,
                           "client-view": 0,
                           "client-update": 0,
                           "admin-login": 0,
                           "admin-register": 0,
                           "admin-view": 0,
                           "admin-update": 0,
                           }


class GatewayAPI(viewsets.ViewSet):
    """
    Sample input:

    """

    def list(self, request):
        request_type = request.data["type"]

        if request_type == 'client-register':
            try:
                return self.client_register(request.data)
            except:
                services_unavailability['client-register'] += 1
                if services_unavailability['client-register'] >= 3:
                    return Response("service unavailable")
        if request_type == 'client-login':
            try:
                return self.client_login(request.data)
            except:
                services_unavailability['client-login'] += 1
                if services_unavailability['client-login'] >= 3:
                    return Response("service unavailable")
        if request_type == 'client-profile-view':
            try:
                return self.client_profile_view(request.data)
            except:
                services_unavailability['client-view'] += 1
                if services_unavailability['client-view'] >= 3:
                    return Response("service unavailable")
        if request_type == 'client-profile-update':
            try:
                return self.client_profile_update(request.data)
            except:
                services_unavailability['client-update'] += 1
                if services_unavailability['client-update'] >= 3:
                    return Response("service unavailable")
        if request_type == 'admin-register':
            try:
                return self.admin_register(request.data)
            except:
                services_unavailability['admin-register'] += 1
                if services_unavailability['admin-register'] >= 3:
                    return Response("service unavailable")
        if request_type == 'admin-login':
            try:
                return self.admin_login(request.data)
            except:
                services_unavailability['admin-login'] += 1
                if services_unavailability['admin-login'] >= 3:
                    return Response("service unavailable")
        if request_type == 'admin-profile-view':
            try:
                return self.admin_profile_view(request.data)
            except:
                services_unavailability['admin-view'] += 1
                if services_unavailability['admin-view'] >= 3:
                    return Response("service unavailable")
        if request_type == 'admin-profile-update':
            try:
                return self.admin_profile_update(request.data)
            except:
                services_unavailability['admin-update'] += 1
                if services_unavailability['admin-update'] >= 3:
                    return Response("service unavailable")

        return Response("")

    def client_register(self, data):
        url = 'http://127.0.0.1:12345/api/client-register'
        x = requests.post(url, data=data)
        return Response(x.text)

    def client_login(self, data):
        url = 'http://127.0.0.1:12345/api/client-login'
        x = requests.post(url, data=data)
        return Response(x.text)

    def client_profile_view(self, data):
        url = 'http://127.0.0.1:12345/api/client-profile-view'
        x = requests.post(url, data=data)
        return Response(x.text)

    def client_profile_update(self, data):
        url = 'http://127.0.0.1:12345/api/client-profile-update'
        x = requests.post(url, data=data)
        return Response(x.text)

    def admin_register(self, data):
        url = 'http://127.0.0.1:12345/api/admin-register'
        x = requests.post(url, data=data)
        return Response(x.text)

    def admin_login(self, data):
        url = 'http://127.0.0.1:12345/api/admin-login'
        x = requests.post(url, data=data)
        return Response(x.text)

    def admin_profile_view(self, data):
        url = 'http://127.0.0.1:12345/api/admin-profile-view'
        x = requests.post(url, data=data)
        return Response(x.text)

    def admin_profile_update(self, data):
        url = 'http://127.0.0.1:12345/api/admin-profile-update'
        x = requests.post(url, data=data)
        return Response(x.text)
