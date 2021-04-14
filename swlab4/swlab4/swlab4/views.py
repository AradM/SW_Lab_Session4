import datetime
import string
import random

from django.shortcuts import render
import requests
from rest_framework import viewsets
from rest_framework.response import Response

from swlab4.swlab4.models import Client


class GatewayAPI(viewsets.ViewSet):
    """
    Sample input:

    """

    def list(self, request):
        request_type = request.data["type"]
        if request_type == 'client-register':
            return self.client_register(request.data)
        if request_type == 'client-login':
            return self.client_login(request.data)
        return Response("")

    def client_register(self, data):
        url = 'http://127.0.0.1:8000/api/client-register'
        x = requests.post(url, data=data)
        return Response(x.text)

    def client_login(self, data):
        url = 'http://127.0.0.1:8000/api/client-login'
        x = requests.post(url, data=data)
        return Response(x.text)


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
        client = Client.objects.get(username=username)
        if client.password == password:
            token = ''.join(random.choice(string.ascii_uppercase + string.digits) for _ in range(100))
            client.token = token
            client.token_generation_time = datetime.datetime.now()
            return Response(client.token)
        else:
            return Response("Username or password are wrong!")
