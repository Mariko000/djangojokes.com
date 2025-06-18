# jokes/models.py

from django.db import models

class Joke(models.Model):
    text = models.TextField() # ここに 'text' フィールドがあるはず
    created_at = models.DateTimeField(auto_now_add=True) # 作成日時を自動で記録

    def __str__(self):
        return self.text[:50] + "..." if len(self.text) > 50 else self.text