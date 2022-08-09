from rest_framework import mixins, generics
from rest_framework.generics import get_object_or_404
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.viewsets import ModelViewSet

from .models import Post
from .serializers import PostSerializer


class PostViewSet(ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = PostSerializer


class PostListView(APIView):

    def get(self, request):
        qs = Post.objects.all()
        serializer = PostSerializer(qs, many=True)
        return Response(serializer.data)

# post_list = PostListView.as_view()


class PostDetailAPIView(APIView):

    def get_object(self, pk):
        return get_object_or_404(Post, pk=pk)

    def get(self, request, pk, format=None):
        post = self.get_object(pk)
        serializer = PostSerializer(post)
        return Response(serializer.data)

post_detail = PostDetailAPIView.as_view()


class PostMixinApiView(mixins.ListModelMixin, generics.GenericAPIView):
    '''
        mixins 을 사용하여 api 구현해보기
    '''
    queryset = Post.objects.all()
    serializer_class = PostSerializer

    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)


# post_list = PostMixinApiView()


class PostListGenericView(generics.ListAPIView):
    '''
        generics.ListAPIView 를사용하여 API 구현
    '''
    queryset = Post.objects.all()
    serializer_class = PostSerializer


post_list = PostListGenericView.as_view()