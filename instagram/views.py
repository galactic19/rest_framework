from rest_framework.decorators import action
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet

from .models import Post
from .permissions import IsAuthorOrReadonly
from .serializers import PostSerializer


class PostViewSet(ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    # authentication_classes = [IsAuthenticated]
    permission_classes = [IsAuthenticated, IsAuthorOrReadonly]  # 인증 설정

    def perform_create(self, serializer):
        author = self.request.user
        ip = self.request.META['REMOTE_ADDR']
        serializer.save(author=author, ip=ip)

    @action(detail=False, methods=['GET'])
    def public(self, request):
        qs = self.get_queryset().filter(is_public=True)
        serializer = self.get_serializer(qs, many=True)
        # serializer = PostSerializer(qs, many=True)
        return Response(serializer.data)

    @action(detail=True, methods=['PATCH'])
    def set_public(self, request, pk):
        instance = self.get_object()
        instance.is_public = True
        instance.save(update_fields=['is_public'])
        serializer = self.get_serializer(instance)
        return Response(serializer.data)


# class PostListAPIView(APIView):
#     '''
#         APIView 를 사용하여 list api 만들어 보기.
#     '''
#     def get(self, request, *args, **kwargs):
#         qs = Post.objects.filter(is_public=True)
#         serializer = PostSerializer(qs, many=True)
#         return Response(serializer.data)
#
#
# public_post_list = PostListAPIView.as_view()


# @api_view(['GET'])
# def public_post_list(request, *args, **kwargs):
#     qs = Post.objects.filter(is_public=True)
#     serializer = PostSerializer(qs, many=True)
#     return Response(serializer.data)



# class PostListView(APIView):
#     @staticmethod
#     def get(self, request, *args, **kwargs):
#         qs = Post.objects.all()
#         serializer = PostSerializer(qs, many=True)
#         return Response(serializer.data)

# post_list = PostListView.as_view()


# class PostDetailAPIView(APIView):
#
#     @staticmethod
#     def get_object(self, pk):
#         return get_object_or_404(Post, pk=pk)
#
#     def get(self, request, pk):
#         post = self.get_object(pk)
#         serializer = PostSerializer(post)
#         return Response(serializer.data)


# post_detail = PostDetailAPIView.as_view()


# class PostDetailAPIView(RetrieveAPIView):
#     queryset = Post.objects.all()
#
#     def get(self, request, *args, **kwargs):
#         post = self.get_object()
#         return Response({
#             'post': PostSerializer(post).data,
#         })
#
#
# post_detail = PostDetailAPIView.as_view()


# class PostMixinApiView(mixins.ListModelMixin, generics.GenericAPIView):
#     '''
#         mixins 을 사용하여 api 구현해보기
#     '''
#     queryset = Post.objects.all()
#     serializer_class = PostSerializer
#
#     def get(self, request, *args, **kwargs):
#         return self.list(request, *args, **kwargs)


# post_list = PostMixinApiView()


# class PostListGenericView(generics.ListAPIView):
#     '''
#         generics.ListAPIView 를사용하여 API 구현
#     '''
#     queryset = Post.objects.all()
#     serializer_class = PostSerializer
#
#
# post_list = PostListGenericView.as_view()