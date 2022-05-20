from django.forms import ModelForm
from .models import Post


# Создаём модельную форму
class PostForm(ModelForm):

    class Meta:
        model = Post
        fields = ['author', 'categories', 'title_post', 'post_text'] #'post_types' ar - статья, ne - новость
