import redis
from django.shortcuts import render
from django.http import HttpRequest
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from django.contrib.auth.decorators import login_required
from rest_framework.decorators import api_view, permission_classes

def get_number():
    r = redis.from_url('redis://localhost', decode_responses=True)
    return r.get('number')

@login_required
def index(request: HttpRequest):
    return render(
        request,
        'api/index.html',
        context={
            'number': get_number(),
        }
    )

@api_view(['GET'])
@permission_classes([IsAuthenticated])
def get(request):
    return Response({'number': get_number()})