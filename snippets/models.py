from django.db import models
from pygments.lexers import get_all_lexers
from pygments.styles import get_all_styles

# Create your models here.

LEXERS = [item for item in get_all_lexers() if item[1]]
LANGUAGE_CHOICES = sorted([(item[1][0], item[0]) for item in LEXERS])
STYLE_CHOICES = sorted((item, item) for item in get_all_styles())

class Snippet(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    title = models.CharField(max_length = 100, blank = True, default = '')
    code = models.TextField()
    linenos = models.BooleanField(default = False) #줄 번호 표시 여부
    language = models.CharField(choices = LANGUAGE_CHOICES, default = 'python', max_length = 100) #소스코드 언어
    style = models.CharField(choices = STYLE_CHOICES, default = 'friendly',max_length = 100) #코드 렌더링 시 채택할 스타일

    class Meta:
        ordering = ('created',) #created field로 순서나타냄