from rest_framework import serializers
from .models import Client, Account, Transfer

class ClientSerializer(serializers.ModelSerializer):
    class Meta:
        model = Client
        fields = '__all__'
    
    def validate_email(self, value):
        if not value:
            raise serializers.ValidationError("The email is a required field.")
        
        if Client.objects.filter(client_mail=value).exists():
            raise serializers.ValidationError("The email is already in use.")
        
        return value

    def validate_name(self, value):
        if not value.strip():
            raise serializers.ValidationError("The name can't be empty.")
        
        return value

class AccountSerializer(serializers.ModelSerializer):
    class Meta:
        model = Account
        fields = '__all__'
    
    def validate_account_number(self, value):
        
        if not value.isdigit():
            raise serializers.ValidationError("The account number must ONLY be numeric.")
        # if not value:
        #     raise serializers.ValidationError("The account is a required field.")
        
        return value
    
    def validate_balance(self, value):
        if value < 0:
            raise serializers.ValidationError("The balance can't be negative.")
        
        return value

class TransferSerializer(serializers.ModelSerializer):
    class Meta:
        model = Transfer
        fields = '__all__'
    
    def validate(self, data):
        account_origin = data['account_origin']
        account_destination = data['account_destination']
        amount = data['amount']

        if account_origin == account_destination:
            raise serializers.ValidationError("The origin account and destination cannot be the same.")
        
        # if not amount:
        #     raise serializers.ValidationError("Please, enter a valid amount.")

        if amount <= 0:
            raise serializers.ValidationError("The amount must be greater than cero.")
        
        if account_origin.balance < amount:
            raise serializers.ValidationError("The balance from origin account is insifficent.")
        
        return data
    
    def create(self, validated_data):
        account_origin = validated_data['account_origin']
        account_destination = validated_data['account_destination']
        amount = validated_data['amount']

        # Update balance
        account_origin.balance -= amount
        account_origin.save()

        account_destination.balance += amount
        account_destination.save()

        return super().create(validated_data)




