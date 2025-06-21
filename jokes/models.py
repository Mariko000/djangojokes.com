# jokes/models.py

from django.db import models
from django.urls import reverse # reverse関数をインポート
from common.utils.text import unique_slug

class Joke(models.Model):
    question = models.TextField(max_length=200)
    answer = models.TextField(max_length=100, blank=True)
    slug = models.SlugField(max_length=50, unique=True, null=True, editable=False)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.question
    
    def save(self, *args, **kwargs):
        if not self.slug:
            # unique_slugの第一引数に質問テキスト、第二引数にモデルクラスを渡す
            self.slug = unique_slug(self.question, type(self))
        super().save(*args, **kwargs)

    def get_absolute_url(self):
        # 'jokes' はapp_name、'detail' はjokes/urls.pyで定義したname
        # kwargs={'slug': self.slug} でスラッグ値をURLに渡す
        return reverse('jokes:detail', kwargs={'slug': self.slug})