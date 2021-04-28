import datetime
import string
import random

from django.shortcuts import render
import requests
from rest_framework import viewsets
from rest_framework.response import Response

from swlab4.swlab4.models import Book


class ClientSeeBooks(viewsets.ViewSet):
    """
    Sample input:

        {
        "token": "dasgjhfjdahfjdhuisydfauyifusdycadfsycoyufsdc",
        "category": "Horror", # optional
        "title": "A Book!"    # optional
        }
    """

    def find_book(self, category, title):
        if not category and not title:
            books = Book.objects.filter()
        elif category and title:
            books = Book.objects.filter(category__icontains=category, title__icontains=title)
        elif category:
            books = Book.objects.filter(category__icontains=category)
        elif title:
            books = Book.objects.filter(title__icontains=title)
        ans = []
        for book in books:
            ans.append({
                "title": book.title,
                "author": book.author,
                "publisher": book.publisher,
                "category": book.category
            })
        return ans

    def list(self, request):
        data = request.data
        token = data['token']

        url = 'http://127.0.0.1:12345/api/is-client-token-available'
        x = requests.post(url, data={"token": token})
        response = Response(x.text)

        if response.data == '"Yes"':
            category, title = None, None
            if "category" in data:
                category = data['category']
            if "title" in data:
                title = data['title']
            return Response(self.find_book(category, title))
        else:
            return Response("Token is wrong!")


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
        "token" : "aasdhaksjdhask1j23hn1k23jh1n23"
        "title": "Pastoral",
        "author": "James Smith",
        "publisher": "Flower",
        "category": "Romantic"
        }
    """

    def list(self, request):
        data = request.data
        token = data['token']

        url = 'http://127.0.0.1:12345/api/is-admin-token-available'
        x = requests.post(url, data={"token": token})
        response = Response(x.text)

        if response.data == '"Yes"':
            book = Book()
            book.title = data['title']
            book.author = data['author']
            book.publisher = data['publisher']
            book.category = data['category']
            book.save()
            return Response("Book Created Successfully!")
        else:
            return Response("Token has expired!")


class UpdateBook(viewsets.ViewSet):
    """
    Sample input:

        {
        "type": "update-book",
        "token" : "aasdhaksjdhask1j23hn1k23jh1n23"
        "id" : "a book id"
        "title": "Pastoral",
        "author": "James Smith",
        "publisher": "Flower",
        "category": "Romantic"
        }
    """

    def list(self, request):
        data = request.data
        token = data['token']

        url = 'http://127.0.0.1:12345/api/is-admin-token-available'
        x = requests.post(url, data={"token": token})
        response = Response(x.text)

        if response.data == '"Yes"':
            book_id = data['id']
            book = Book.objects.get(book_id=book_id)
            if not book:
                return Response("Book id is Wrong!")
            else:
                if 'title' in data:
                    book.title = data['title']
                if 'author' in data:
                    book.author = data['author']
                if 'category' in data:
                    book.category = data['category']
                if 'publisher' in data:
                    book.publisher = data['publisher']
                book.save()
                return Response("Successfully updated")
        else:
            return Response("Token has expired")


class ReadBook(viewsets.ViewSet):
    """
    Sample input:

        {
        "type": "read-book",
        "token" : "aasdhaksjdhask1j23hn1k23jh1n23"
        "id" : "a book id"
        }
    """

    def list(self, request):
        data = request.data
        token = data['token']

        url = 'http://127.0.0.1:12345/api/is-admin-token-available'
        x = requests.post(url, data={"token": token})
        response = Response(x.text)

        if response.data == '"Yes"':
            book_id = data['id']
            book = Book.objects.get(book_id=book_id)
            if not book:
                return Response("Book id is Wrong!")
            else:
                return Response(
                    "title : " + book.title + "\nauthor : " + book.author + "\npublisher : " + book.publisher +
                    "\ncategory : " + book.category)
        else:
            return Response("Token has expired")


class DeleteBook(viewsets.ViewSet):
    """
    Sample input:

        {
        "type": "delete-book",
        "token" : "aasdhaksjdhask1j23hn1k23jh1n23"
        "id" : "a book id"
        }
    """

    def list(self, request):
        data = request.data
        token = data['token']

        url = 'http://127.0.0.1:12345/api/is-admin-token-available'
        x = requests.post(url, data={"token": token})
        response = Response(x.text)

        if response.data == '"Yes"':
            book_id = data['id']
            book = Book.objects.get(book_id=book_id)
            if not book:
                return Response("Book id is Wrong!")
            else:
                book.delete()
                return Response("Book deleted successfully")
        else:
            return Response("Token has expired")
