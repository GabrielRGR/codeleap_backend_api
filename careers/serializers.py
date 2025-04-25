from rest_framework.serializers import ModelSerializer
from .models import PostModel, LikesModel

class PostSerializer(ModelSerializer):
    class Meta:
        model = PostModel
        fields = '__all__'
        read_only_fields =['id', 'username', 'created_datetime']

    def update(self, instance, validated_data):
        
        instance.title = validated_data.get('title', instance.title)
        instance.content = validated_data.get('content', instance.content)
        #instance.likes = validated_data.get('likes', instance.content)
        instance.save()

        return instance
    
class LikesSerializer(ModelSerializer):
    class Meta:
        model = LikesModel
        fields = '__all__'
        read_only_fields = ['id', 'username']