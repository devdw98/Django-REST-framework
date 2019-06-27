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

    """
    *기본 serializer
    id = serializers.IntegerField(read_only=True)
    title = serializers.CharField(required=False, allow_blank=True, max_length=100)
    code = serializers.CharField(style={'base_template': 'textarea.html'})
    linenos = serializers.BooleanField(required=False)
    language = serializers.ChoiceField(choices=LANGUAGE_CHOICES, default='python')
    style = serializers.ChoiceField(choices=STYLE_CHOICES, default='friendly')

    def create(self, validated_data):
       
    #    Create and return a new `Snippet` instance, given the validated data.
    
        return Snippet.objects.create(**validated_data)

    def update(self, instance, validated_data):

    #    Update and return an existing `Snippet` instance, given the validated data.

        instance.title = validated_data.get('title', instance.title)
        instance.code = validated_data.get('code', instance.code)
        instance.linenos = validated_data.get('linenos', instance.linenos)
        instance.language = validated_data.get('language', instance.language)
        instance.style = validated_data.get('style', instance.style)
        instance.save()
        return instance
    """