from .models import Product, Singer, Song, Person, Code, Anime
from rest_framework import serializers




class ProductSerializer(serializers.ModelSerializer):
    # to change model field-> here we are changing name field to product name field without changing in model
    # decalre custom field name with serizalise method and method name would be get_customFieldName(self, obj)
    product_name = serializers.SerializerMethodField(read_only=True) # get_product_name see below

    # to generate individual url for product detail view in list view itself
    # just need to pass name of url and its lookup field mentioned in url
    url = serializers.HyperlinkedIdentityField(view_name='productdetailapi', lookup_field='pk')

    # if you want email id who created this data but dont want to save in database as its doesnt have field in DB
    # so while calling create method we can pop out email and save it
    # email = serializers.EmailField(write_only=True)

    class Meta:
        model = Product
        fields = ['url', 'id', 'product_name', 'name', 'description', 'price']

    # this function will help to modify model field
    def get_product_name(self, obj):
        return obj.name # passing name so it can change from name to product_name and add same in field list

    '''Model Serializer create and update methods'''
    # overriding create method and poping out email id
    # def create(self, validated_data):
    #     email = validated_data.pop('email')
    #     print(email)
    #     return super().create(validated_data)

    # # same way we can update data using this
    # def update(self, instance, validated_data):
    #     return super().update(instance, validated_data)


    '''Custom validation with Model Serializer'''

    # field level validation -> 
    # we can validate individual fields in serializer using format -> def validate_fieldName
    # def validate_name(self, value):
    #     qs = Product.objects.filter(name__exact=value)
    #     if qs.exists():
    #         raise serializers.ValidationError(f"{value} already exist")
    #     return value

    # object level validation ->
    # this is how we can get values of all data and perfrom validation
    # def validate(self, data):
    #     name = data.get('name')
    #     price = data.get('price')
    #     if len(name) >= 100:
    #         raise serializers.ValidationError(f"{name} is too long")
    #     if price < 0:
    #         raise serializers.ValidationError(f"{price} not acceptable")
    #     return super().validate(data)

class PersonSerializer(serializers.ModelSerializer):
    class Meta:
        model = Person
        fields = '__all__'



class SongSerializer(serializers.ModelSerializer):
    class Meta:
        model = Song
        fields = ['song_name', 'singer', 'durantion']


class SingerSerializer(serializers.ModelSerializer):
    # here we are creating nested serializer 
    # we already have forigenkey relationship between song -> singer and we defined related_name='extra
    # so using that name we can songs which are related to singer and add in  fields
    extra = SongSerializer(many=True, read_only=True)
    class Meta:
        model = Singer
        fields = ['singer_name', 'gender', 'extra']


class CodeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Code
        fields = ['name', 'desc']


class AnimeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Anime
        fields = '__all__'