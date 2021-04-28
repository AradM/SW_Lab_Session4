import datetime
import string
import random

from django.shortcuts import render
import requests
from rest_framework import viewsets
from rest_framework.response import Response

from swlab4.swlab4.client_views import time_to_int
from swlab4.swlab4.models import Client
from swlab4.swlab4.models import Admin


class AdminRegister(viewsets.ViewSet):
    """
    Sample input:

        {
        "type": "admin-register",
        "username": "Arad",
        "password": "1234",
        "email": "arad.mohammadi99@gmail.com",
        "mobile": "09123385973"
        }
    """

    def list(self, request):
        data = request.data
        admin = Admin()
        admin.username = data['username']  # todo are these fields available?
        admin.password = data['password']
        admin.email = data['email']
        admin.mobile = data['mobile']
        admin.save()
        return Response("Admin registered successfully!")


class AdminLogin(viewsets.ViewSet):
    """
    Sample input:

        {
        "type": "admin-login",
        "username": "Arad",
        "password": "1234"
        }
    """

    def list(self, request):
        data = request.data
        username = data['username']  # todo are these fields available?
        password = data['password']
        admin = Admin.objects.get(username=username)

        if admin.password == password:
            token = ''.join(random.choice(string.ascii_uppercase + string.digits) for _ in range(100))
            admin.token = token
            admin.token_generation_time = datetime.datetime.now()
            admin.save()
            return Response(admin.token)
        else:
            return Response("Username or password are wrong!")


class AdminProfileView(viewsets.ViewSet):
    """
    Sample input:

        {
        "type": "admin-profile-view",
        "token": "random string for token"
        }
    """

    def list(self, request):
        data = request.data
        token = data['token']
        admin = Admin.objects.get(token=token)
        if not admin:
            return Response("Token is wrong!")
        if time_to_int(admin.token_generation_time + datetime.timedelta(hours=5, minutes=30)) \
                > time_to_int(datetime.datetime.now()):
            admin.token_generation_time = datetime.datetime.now()
            return Response({"username": admin.username,
                             "email": admin.email,
                             "mobile": admin.mobile
                             })
        else:
            return Response("Token has expired!")


class AdminProfileUpdate(viewsets.ViewSet):
    """
    Sample input:
    {
        "type": "admin-profile-view",
        "token": "random string for token"
        "username": AradArad
    }

    """

    def list(self, request):
        data = request.data
        token = data['token']
        admin = Admin.objects.get(token=token)
        if not admin:
            return Response("Token is wrong!")
        if time_to_int(admin.token_generation_time + datetime.timedelta(hours=5, minutes=30)) > time_to_int(
                datetime.datetime.now()):
            admin.token_generation_time = datetime.datetime.now()
            if 'username' in data:
                admin.username = data['username']
            if 'mobile' in data:
                admin.mobile = data['mobile']
            if 'password' in data:
                admin.password = data['password']
            if 'email' in data:
                admin.email = data['email']
            admin.save()
            return Response("Successfully updated")
        else:
            return Response("Token has expired!")


class AdminSeeClients(viewsets.ViewSet):
    """
    Sample input:

        {
        "token": "random string for token"
        }
    """

    def list(self, request):
        data = request.data
        token = data['token']
        admin = Admin.objects.get(token=token)
        if not admin:
            return Response("Token is wrong!")
        if time_to_int(admin.token_generation_time + datetime.timedelta(hours=5, minutes=30)) \
                > time_to_int(datetime.datetime.now()):
            admin.token_generation_time = datetime.datetime.now()
            clients = Client.objects.filter()
            ans = []
            for client in clients:
                ans.append({
                    "username": client.username,
                    "mobile": client.mobile,
                    "email": client.email,
                })
            return Response(ans)
        else:
            return Response("Token has expired!")


class IsAdminTokenAvailable(viewsets.ViewSet):
    """
    Sample input:

        {
        "token": "random string for token"
        }
    """

    def list(self, request):
        data = request.data
        token = data['token']
        admin = Admin.objects.get(token=token)
        if not admin:
            return Response("No")
        if time_to_int(admin.token_generation_time + datetime.timedelta(hours=5, minutes=30)) \
                > time_to_int(datetime.datetime.now()):
            return Response("Yes")
        else:
            return Response("No")
