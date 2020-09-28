from rest_framework import serializers
from .models import Register
 

class RegisterSerializer(serializers.ModelSerializer):
    password2 = serializers.CharField(style = {'input_type' : 'password'}, write_only= True)
    
    class Meta:
        model = Register
        fields = ['EmailId', 'Password', 'password2']
        # extra_kwargs = {
        #     'Password' : {'write_only' : True, 'read_only' : True}
        # }

    def save(self):

        email = self.validated_data['EmailId']
        if Register.objects.filter(EmailId = email).exists():
            raise serializers.ValidationError({'email' : 'Email already exist'})

        password = self.validated_data['Password']
        password2 = self.validated_data['password2']

        if password != password2:
            raise serializers.ValidationError({'password' : 'Password must match.'})
        

        register = Register(
            EmailId = self.validated_data['EmailId'],
            Password = self.validated_data['Password']
        )    
        register.save()
        return register

