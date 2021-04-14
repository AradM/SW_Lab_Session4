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
        # if request_type == 'client-login':
        return Response("")

    def client_register(self, data):
        url = 'http://127.0.0.1:8000/api/client-register'
        x = requests.post(url, data=data)
        return Response(x.text)


class ClientRegister(viewsets.ViewSet):
    """
    Sample input:

    """

    def list(self, request):
        data = request.data
        client = Client()
        client.username = data['username']  # todo are these fields available?
        client.password = str(hash(data['password']))
        client.email = data['email']
        client.mobile = data['mobile']
        client.save()
        return Response("Client registered successfully!")
