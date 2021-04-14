from django.shortcuts import render
from rest_framework import viewsets
from rest_framework.response import Response


class GatewayAPI(viewsets.ViewSet):
    """
    Sample input:

    """

    def list(self, request):
        request_type = request.data["type"]
        return Response("")
