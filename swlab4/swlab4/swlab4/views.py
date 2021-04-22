import datetime
import string
import random

from django.shortcuts import render
import requests
from rest_framework import viewsets
from rest_framework.response import Response

from swlab4.swlab4.models import Client
from swlab4.swlab4.models import Admin
from swlab4.swlab4.models import Book

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
        url = 'http://127.0.0.1:8000/api/client-register'
        x = requests.post(url, data=data)
        return Response(x.text)

    def client_login(self, data):
        url = 'http://127.0.0.1:8000/api/client-login'
        x = requests.post(url, data=data)
        return Response(x.text)

    def client_profile_view(self, data):
        url = 'http://127.0.0.1:8000/api/client-profile-view'
        x = requests.post(url, data=data)
        return Response(x.text)

    def client_profile_update(self, data):
        url = 'http://127.0.0.1:8000/api/client-profile-update'
        x = requests.post(url, data=data)
        return Response(x.text)

    def admin_register(self, data):
        url = 'http://127.0.0.1:8000/api/admin-register'
        x = requests.post(url, data=data)
        return Response(x.text)

    def admin_login(self, data):
        url = 'http://127.0.0.1:8000/api/admin-login'
        x = requests.post(url, data=data)
        return Response(x.text)

    def admin_profile_view(self, data):
        url = 'http://127.0.0.1:8000/api/admin-profile-view'
        x = requests.post(url, data=data)
        return Response(x.text)

    def admin_profile_update(self, data):
        url = 'http://127.0.0.1:8000/api/admin-profile-update'
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


class CURDGateway(viewsets.ViewSet):
    """
    Sample input:

    """

    def list(self, request):
        request_type = request.data["type"]

        if request_type == 'create-book':
            return self.create_book(request.data)
        if request_type == 'update-book':
            return self.update_book(request.data)
        if request_type == 'read-book':
            return self.read_book(request.data)
        if request_type == 'delete-book':
            return self.delete_book(request.data)

        return Response("")

    def create_book(self, data):
        url = 'http://127.0.0.1:8000/api/create-book'
        x = requests.post(url, data=data)
        return Response(x.text)

    def update_book(self, data):
        url = 'http://127.0.0.1:8000/api/update-book'
        x = requests.post(url, data=data)
        return Response(x.text)

    def read_book(self, data):
        url = 'http://127.0.0.1:8000/api/read-book'
        x = requests.post(url, data=data)
        return Response(x.text)

    def delete_book(self, data):
        url = 'http://127.0.0.1:8000/api/delete-book'
        x = requests.post(url, data=data)
        return Response(x.text)


class CreateBook(viewsets.ViewSet):
    """
    Sample input:

        {
        "type": "create-book",
        "title": "Pastoral",
        "author": "James Smith",
        "publisher": "Flower",
        "category": "Romantic"
        }
    """

    def list(self, request):
        data = request.data
        book = Book()
        book.title = data['title']
        book.author = data['author']
        book.publisher = data['publisher']
        book.category = data['category']
        book.save()
        return Response("Book Created Successfully!")


class UpdateBook(viewsets.ViewSet):
    """
    Sample input:

        {
        "type": "update-book",
        "id" : "a book id"
        "title": "Pastoral",
        "author": "James Smith",
        "publisher": "Flower",
        "category": "Romantic"
        }
    """

    def list(self, request):
        data = request.data
        book_id = data['id']
        book = Book.objects.get(book_id=book_id)
        if not book:
            return Response("Book id is Wrong!")
        else:
            if 'title' in data:
                book.username = data['title']
            if 'author' in data:
                book.mobile = data['author']
            if 'category' in data:
                book.password = data['category']
            if 'publisher' in data:
                book.email = data['publisher']
            book.save()
            return Response("Successfully updated")


class ReadBook(viewsets.ViewSet):
    """
    Sample input:

        {
        "type": "read-book",
        "id" : "a book id"
        }
    """

    def list(self, request):
        data = request.data
        book_id = data['id']
        book = Book.objects.get(book_id=book_id)
        if not book:
            return Response("Book id is Wrong!")
        else:
            return Response("title : " + book.title + "\nauthor : " + book.author + "\npublisher : " + book.publisher +
                            "\ncategory : " + book.category)


class DeleteBook(viewsets.ViewSet):
    """
    Sample input:

        {
        "type": "delete-book",
        "id" : "a book id"
        }
    """

    def list(self, request):
        data = request.data
        book_id = data['id']
        book = Book.objects.get(book_id=book_id)
        if not book:
            return Response("Book id is Wrong!")
        else:
            book.delete()
            return Response("Book deleted successfully")
