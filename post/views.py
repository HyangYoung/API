from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet
from .serializers import PostSerializer
from .models import Post


class PostViewSet(ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = PostSerializer

    # def dispatch(self, request, *args, **kwargs):
    #     print("request.body", request.body) # logger recommend
    #     print("request.POST", request.POST) # logger recommend
    #     return super().dispatch(request, *args, **kwargs)


# def post_list(request):
#     pass
#
# def post_detail(request, pk):
#     pass