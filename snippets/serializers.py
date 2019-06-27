#Serializer : Django에서 사용하는 객체들을 REST API에서 사용할 형태로 변환해주는 어뎁터

from rest_framework import serializers
from .models import Snippet, LANGUAGE_CHOICES, STYLE_CHOICES

class SnippetSerializer(serializers.ModelSerializer):
    """
    ModelSerializer : 하나의 모델에 대해서 Serializer 클래스를 자동으로 만들어주는 클래스
    class Meta에 어떤 모델에 대해서 serializer를 만드는 것인지 알리고, 필드 정보를 준다.
    >> create(), update() 도 기본 구현이 되어 생략가능하다.
    """
    class Meta:
       model = Snippet
       fields = ('id', 'title', 'code', 'linenos', 'language','style')