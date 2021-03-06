from rest_framework import serializers

#imported for UserProfileSerializer
from profiles_api import models

class HelloSerializer(serializers.Serializer):
    '''
    Serializes the name field for testing APIView.
    '''

    name = serializers.CharField(max_length = 10)


#UserProfile Class

class UserProfileSerializer(serializers.ModelSerializer):
    '''
    serializes a user profile object
    '''

    class Meta:
        model = models.UserProfile
        fields = ('id', 'email', 'name', 'password')

        #Exceptions for password field
        extra_kwargs = {
            'password':{
                'write_only':True,
                'style':{
                    'input_type':'password'
                }
            }
        }

        #Over-writing create method
        def create(self, validated_data):
            '''
            create and return a new user
            '''

            user = models.UserProfile.objects.create_user(
                email = validated_data['email'],
                name = validated_data['name'],
                password = validated_data['password']
            )

            return user

# Profile Feed Item Serializer

class ProfileFeedItemSerializer(serializers.ModelSerializer):
    '''
    serializes profile feed items
    '''
    class Meta:
        model = models.ProfileFeedItem
        fields = ('id','user_profile', 'status_text','created_on')
        extra_kwargs = {
            'user_profile': {
                'read_only': True
            }
        }