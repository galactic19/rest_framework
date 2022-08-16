from django.forms import ModelForm

from instagram.models import Post


class PostForm(ModelForm):
    class Meta:
        model = Post
        fields = ['content', 'is_public']


