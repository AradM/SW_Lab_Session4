import datetime
import string
import random

from django.shortcuts import render
import requests
from rest_framework import viewsets
from rest_framework.response import Response

from swlab4.swlab4.models import Client
from swlab4.swlab4.models import Admin


class ClientRegister(viewsets.ViewSet):
    """
    Sample input:

        {
        "type": "client-register",
        "username": "Ashkan",
        "password": "1234",
        "email": "ashkan.m10@gmail.com",
        "mobile": "09205817215"
        }
    """

    def list(self, request):
        data = request.data
        client = Client()
        client.username = data['username']  # todo are these fields available?
        client.password = data['password']
        client.email = data['email']
        client.mobile = data['mobile']
        client.save()
        return Response("Client registered successfully!")


class ClientLogin(viewsets.ViewSet):
    """
    Sample input:

        {
        "type": "client-login",
        "username": "Ashkan",
        "password": "1234"
        }
    """

    def list(self, request):
        data = request.data
        username = data['username']  # todo are these fields available?
        password = data['password']
        print(username, password)
        client = Client.objects.get(username=username)
        print("++++++++++++++++++++++++++", client.email)
        if client.password == password:
            token = ''.join(random.choice(string.ascii_uppercase + string.digits) for _ in range(100))
            client.token = token
            client.token_generation_time = datetime.datetime.now()
            client.save()
            return Response(client.token)
        else:
            return Response("Username or password are wrong!")


def time_to_int(dt):
    return int(dt.strftime("%Y%m%d%H%M%S"))


class ClientProfileView(viewsets.ViewSet):
    """
    Sample input:

        {
        "type": "client-profile-view",
        "token": "dasgjhfjdahfjdhuisydfauyifusdycadfsycoyufsdc"
        }
    """

    def list(self, request):
        data = request.data
        token = data['token']
        client = Client.objects.get(token=token)
        if not client:
            return Response("Token is wrong!")
        if time_to_int(client.token_generation_time + datetime.timedelta(hours=5, minutes=30)) > time_to_int(
                datetime.datetime.now()):
            client.token_generation_time = datetime.datetime.now()
            return Response({"username": client.username,
                             "email": client.email,
                             "mobile": client.mobile
                             })
        else:
            return Response("Token has expired!")


class ClientProfileUpdate(viewsets.ViewSet):
    """
    Sample input:

    """

    def list(self, request):
        data = request.data
        token = data['token']
        client = Client.objects.get(token=token)
        if not client:
            return Response("Token is wrong!")
        if time_to_int(client.token_generation_time + datetime.timedelta(hours=5, minutes=30)) \
                > time_to_int(datetime.datetime.now()):
            client.token_generation_time = datetime.datetime.now()
            if 'username' in data:
                client.username = data['username']
            if 'mobile' in data:
                client.mobile = data['mobile']
            if 'password' in data:
                client.password = data['password']
            if 'email' in data:
                client.email = data['email']
            client.save()
            return Response("Successfully updated")
        else:
            return Response("Token has expired!")


class IsClientTokenAvailable(viewsets.ViewSet):
    """
    Sample input:

        {
        "token": "random string for token"
        }
    """

    def list(self, request):
        data = request.data
        token = data['token']
        client = Client.objects.get(token=token)
        if not client:
            return Response("No")
        if time_to_int(client.token_generation_time + datetime.timedelta(hours=5, minutes=30)) \
                > time_to_int(datetime.datetime.now()):
            return Response("Yes")
        else:
            return Response("No")
