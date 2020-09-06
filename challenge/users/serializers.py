from rest_framework import serializers
from django.contrib.auth.models import User
from users import models


class UserSerializer(serializers.ModelSerializer):
    """ Serializes a user object """

    class Meta:
        model = User
        fields = ['id', 'username', 'password']
        extra_kwargs = {
            'password':  {
                'write_only': True,
                'style': {
                    'input_type': 'password'
                }
            }
        }