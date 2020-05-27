from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view
from account.models import account
from blog.models import Post
from blog.api.serializers import PostSerializer 
