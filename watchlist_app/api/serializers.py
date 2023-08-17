from rest_framework import serializers
from watchlist_app.models import Movie, Watchlist, StreamPlatform, Review


""" 
# validation (for serializers)
def name_length(value):
    if len(value) < 3:
        raise serializers.ValidationError("Name is too short")


class MovieSerializers(serializers.Serializer):

    # For get
    id = serializers.IntegerField(read_only=True)
    name = serializers.CharField(validators = [name_length])
    description = serializers.CharField()
    active = serializers.BooleanField()

    # For post
    def create(self, validated_data):
        return Movie.objects.create(**validated_data)
    
    # For put
    def update(self, instance, validated_data):
        instance.name = validated_data.get('name', instance.name)
        instance.description = validated_data.get('description', instance.description)
        instance.active = validated_data.get('active', instance.active)
        instance.save()
        return instance

    '''
    # Field level validation for name
    def validate_name(self, value):

        if len(value) < 3:
            raise serializers.ValidationError("Name is too short")
        else:
            return value
    
    # Field level validation for description
    def validate_description(self, value):

        if len(value) < 3:
            raise serializers.ValidationError("Description is too short")
        else:
            return value

    '''
    # Object level validation    
    def validate(self, data):
        if data['name'] == data['description']:
            raise serializers.ValidationError("Description and Name Should not be same")
        else:
            return data
"""   

class MovieSerializers(serializers.ModelSerializer):

    len_name = serializers.SerializerMethodField()

    class Meta:
        model = Movie
        fields = "__all__"
        # fields = ['id', 'name', 'description']
        # exclude = ['active']
        # exclude = ['description']

    def get_len_name(self, object):
        length = len(object.name)
        return length

    # Field level validation for name
    def validate_name(self, value):

        if len(value) < 3:
            raise serializers.ValidationError("Name is too short")
        else:
            return value
    
    # Field level validation for description
    def validate_description(self, value):

        if len(value) < 3:
            raise serializers.ValidationError("Description is too short")
        else:
            return value
        
    # Object level validation    
    def validate(self, data):
        if data['name'] == data['description']:
            raise serializers.ValidationError("Description and Name Should not be same")
        else:
            return data

#-------------------------------------------------------------------------------------------------

# Serializers with Updated models

class ReviewSerializers(serializers.ModelSerializer):

    review_user = serializers.StringRelatedField(read_only=True)

    class Meta:
        model = Review
        #fields = "__all__"
        exclude = ['watchlist']


class WatchlistSerializers(serializers.ModelSerializer):

    reviews = ReviewSerializers(many = True, read_only=True)

    class Meta:
        model = Watchlist
        fields = "__all__"


class StreamPlatformSerializers(serializers.ModelSerializer):

    watchlist = WatchlistSerializers(many=True, read_only=True)

    # watchlist = serializers.StringRelatedField(many=True)

    # watchlist = serializers.PrimaryKeyRelatedField(many=True, read_only=True)

    '''
    watchlist = serializers.HyperlinkedRelatedField(
        many=True,
        read_only=True,
        view_name='watch_detail'
    )

    # context={'request': request} should be passed in get views
    '''
    class Meta:
        model = StreamPlatform
        fields = "__all__"