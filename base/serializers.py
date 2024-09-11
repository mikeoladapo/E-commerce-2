from rest_framework import serializers
from .models import Profile,Category,Product

class ProfileSerializer(serializers.Serializer):
    user = serializers.SlugRelatedField(queryset=Profile.objects.all(),slug_field='username')
    #user = serializers.PrimaryKeyRelatedField(queryset=Profile.objects.all())
    date_of_birth = serializers.DateField()
    phonenumber = serializers.CharField(max_length=12)
    picture = serializers.ImageField(allow_null=True,required=False)

    def create(self,validated_data):
        return Profile.objects.create(**validated_data)
    
    def update(self,instance,validated_data):
        instance.user = validated_data.get('user',instance.user)
        instance.date_of_birth = validated_data.get('date_of_birth',instance.date_of_birth)
        instance.phonenumber = validated_data.get('phonenumber',instance.phonenumber)
        instance.picture = validated_data.get('picture',instance.picture)
        instance.save()
        return instance
    
class CategorySerializer(serializers.Serializer):
    name = serializers.CharField(max_length = 20)
    def create(self, validated_data):
        return Category.objects.create(**validated_data)
    def update(self,instance,validated_data):
        instance.name = validated_data.get('name',instance.name)
        instance.save()
        return instance

class ProductSerializer(serializers.Serializer):
    name = serializers.CharField(max_length = 20)
    price = serializers.DecimalField(max_digits=10,decimal_places=2)
    about = serializers.CharField(max_length = 50)
    #category = serializers.PrimaryKeyRelatedField(queryset=Category.objects.all())
    category = serializers.SlugRelatedField(queryset=Category.objects.all(),slug_field="name")
    picture = serializers.ImageField(allow_null=True,required=False)

    def create(self, validated_data):
        return Product.objects.create(**validated_data)
    def update(self, instance, validated_data):
        instance.name = validated_data.get('name',instance.name)
        instance.price = validated_data.get('price',instance.price)
        instance.about = validated_data.get('about',instance.about)
        instance.category = validated_data.get('category',instance.category)
        instance.picture = validated_data.get('picture',instance.picture)
        instance.save()
        return instance