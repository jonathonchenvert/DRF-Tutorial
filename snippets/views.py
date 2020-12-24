# from django.shortcuts import render
# from django.http import HttpResponse, JsonResponse
from django.http import Http404
# from django.views.decorators.csrf import csrf_exempt

# from rest_framework.parsers import JSONParser
# from rest_framework import status
# from rest_framework.decorators import api_view
# from rest_framework.views import APIView
# from rest_framework.response import Response
from rest_framework import generics#, mixins

from snippets.models import Snippet
from snippets.serializers import SnippetSerializer

# Create your views here.

# View to display all snippets with mixed-in generic class-based views


class SnippetList(generics.ListCreateAPIView):
    queryset = Snippet.objects.all()
    serializer_class = SnippetSerializer


# View to display all snippets with mixins class

# class SnippetList(mixins.ListModelMixin, mixins.CreateModelMixin, generics.GenericAPIView):
#     queryset = Snippet.objects.all()
#     serializer_class = SnippetSerializer
#
#     def get(self, request, *args, **kwargs):
#         return self.list(request, *args, **kwargs)
#
#     def post(self, request, *args, **kwargs):
#         return self.create(request, *args, **kwargs)

# View to display all snippets with class-based views

# class SnippetList(APIView):
#     # List all snippets, or create a new snippet
#     def get(self, request, format=None):
#         snippets = Snippet.objects.all()
#         serializer = SnippetSerializer(snippets, many=True)
#         return Response(serializer.data)
#
#     def post(self, request, format=None):
#         serializer = SnippetSerializer(data=request.data)
#
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data, status=status.HTTP_201_CREATED)
#
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


# View to display all snippets with wrapping API views

# @api_view(['GET', 'POST'])
# def snippet_list(request, format=None):
#     # List all code snippets, or create a new snippet
#     if request.method == 'GET':
#         snippets = Snippet.objects.all()
#         serializer = SnippetSerializer(snippets, many=True)
#         return Response(serializer.data)
#
#     elif request.method == 'POST':
#         serializer = SnippetSerializer(data=request.data)
#
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data, status=status.HTTP_201_CREATED)
#
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


# View to display all snippets with regular Django views; used only for example purposes

# @csrf_exempt
# def snippet_list(request):
#     # List all code snippets, or create a new snippet
#
#     if request.method == 'GET':
#         snippets = Snippet.objects.all()
#         serializer = SnippetSerializer(snippets, many=True)
#         return JsonResponse(serializer.data, safe=False)
#
#     elif request.method == 'POST':
#         data = JSONParser().parse(request)
#         serializer = SnippetSerializer(data=data)
#
#         if serializer.is_valid():
#             serializer.save()
#             return JsonResponse(serializer.data, status=201)
#         return JsonResponse(serializer.errors, status=400)


# View to request a single snippet, update it, or delete it with class-based views

# class SnippetDetail(APIView):
#     # Retrieve, Update, or Delete a snippet instance
#     def get_object(self, pk):
#         try:
#             return Snippet.objects.get(pk=pk)
#         except Snippet.DoesNotExist:
#             raise Http404
#
#     def get(self, request, pk, format=None):
#         snippet = self.get_object(pk)
#         serializer = SnippetSerializer(snippet)
#         return Response(serializer.data)
#
#     def put(self, request, pk, format=None):
#         snippet = self.get_object(pk)
#         serializer = SnippetSerializer(snippet, data=request.data)
#
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data)
#
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
#
#     def delete(self, request, pk, format=None):
#         snippet = self.get_object(pk)
#         snippet.delete()
#
#         return Response(status=status.HTTP_204_NO_CONTENT)


# View to request a single snippet, update it, or delete it with mixed-in generic class-based views


class SnippetDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Snippet.objects.all()
    serializer_class = SnippetSerializer

# View to request a single snippet, update it, or delete it with mixins class

# class SnippetDetail(mixins.RetrieveModelMixin, mixins.UpdateModelMixin,
#                     mixins.DestroyModelMixin, generics.GenericAPIView):
#
#     queryset = Snippet.objects.all()
#     serializer_class = SnippetSerializer
#
#     def get(self, request, *args, **kwargs):
#         return self.retrieve(request, *args, **kwargs)
#
#     def put(self, request, *args, **kwargs):
#         return self.update(request, *args, **kwargs)
#
#     def delete(self, request, *args, **kwargs):
#         return self.destroy(request, *args, **kwargs)

# View to request a single snippet, update it, or delete it with wrapping API views

# @api_view(['GET', 'PUT', 'DELETE'])
# def snippet_detail(request, pk, format=None):
#     # Retrieve, Update, or Delete a code snippet
#
#     # First check to see that the snippet exists
#     try:
#         snippet = Snippet.objects.get(pk=pk)
#     except Snippet.DoesNotExist:
#         return Response(status=status.HTTP_404_NOT_FOUND)
#
#     # Retrieve
#     if request.method == 'GET':
#         serializer = SnippetSerializer(snippet)
#         return Response(serializer.data)
#
#     # Update
#     elif request.method == 'PUT':
#         serializer = SnippetSerializer(snippet, data=request.data)
#
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data)
#
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
#
#     elif request.method == 'DELETE':
#         snippet.delete()
#         return Response(status=status.HTTP_204_NO_CONTENT)


# View to request a single snippet, update it, or delete it with regular Django views; used only for example purposes

# @csrf_exempt
# def snippet_detail(request, pk):
#     # Retrieve, Update, or Delete a code snippet
#
#     # First check to see that the snippet exists
#     try:
#         snippet = Snippet.objects.get(pk=pk)
#     except Snippet.DoesNotExist:
#         return HttpResponse(status=404)
#
#     # Retrieve
#     if request.method == 'GET':
#         serializer = SnippetSerializer(snippet)
#         return JsonResponse(serializer.data)
#
#     # Update
#     elif request.method == 'PUT':
#         data = JSONParser().parse(request)
#         serializer = SnippetSerializer(snippet, data=data)
#
#         if serializer.is_valid():
#             serializer.save()
#             return JsonResponse(serializer.data)
#
#         return JsonResponse(serializer.errors, status=400)
#
#     # Delete
#     elif request.method == 'DELETE':
#         snippet.delete()
#         return HttpResponse(status=204)
