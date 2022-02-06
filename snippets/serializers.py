from rest_framework import serializers
from django.contrib.auth.models import User
from .models import Snippet


class SnippetSerializer(serializers.ModelSerializer):
    """
    1. User 인스턴스의 정보를 참조할 수 있도록 owner 필드 추가.
    2. 필드에 명시되는 source 인자는 해당 필드의 값을 채우기 위해 사용할 속성을 명시하며,
       serialize 되는 DB 인스턴스의 그 어떤 속성이든 가리킬 수 있음.
    3. serialize의 owner 필드는 ReadOnlyField 클래스로 정의.
       ReadOnlyField로 정의되는 필드들은 읽기 전용 특성을 가지고, 오로지 serialize를 통해
       DB 인스턴스의 정보를 표현할 때만 사용된다. 즉, deserialize를 통해 DB 인스턴스를 생성 및 수정할 때는 사용되지 않음.
    """
    owner = serializers.ReadOnlyField(source='owner.username')
    class Meta:
        model = Snippet
        fields = ['id', 'title', 'code', 'linenos', 'language', 'style', 'owner']


# User 모델에 대응하는 시리얼라이저.
class UserSerializer(serializers.ModelSerializer):
    # User 모델에는 역관계에 대한 명시적인 필드가 없어 snippets 필드를 명시적으로 정의.
    snippets = serializers.PrimaryKeyRelatedField(many=True, queryset=Snippet.objects.all())

    class Meta:
        model = User
        fields = ['id', 'username', 'snippets']