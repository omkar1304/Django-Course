from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.decorators import api_view, authentication_classes, permission_classes
from .serializers import ProductSerializer, SingerSerializer, SongSerializer, PersonSerializer, CodeSerializer, AnimeSerializer
from .models import Product, Singer, Song, Person, Code, Anime
from rest_framework import permissions, authentication
from .permissions import CustomDjangoModelPermissions, CustomPermissions
from rest_framework.mixins import ListModelMixin, RetrieveModelMixin, CreateModelMixin, UpdateModelMixin, DestroyModelMixin
from rest_framework.generics import ListAPIView, ListCreateAPIView, RetrieveAPIView, CreateAPIView, UpdateAPIView, DestroyAPIView, GenericAPIView
from rest_framework import viewsets
from rest_framework_simplejwt.authentication import JWTAuthentication
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import SearchFilter, OrderingFilter


# All methods using function based view ->
# To add Authentication and Permission classes in function based view
@api_view(['GET', 'POST','PUT', 'DELETE'])
@permission_classes([permissions.IsAuthenticated])
@authentication_classes([authentication.BasicAuthentication])
def personAPIView(request, pk=None):
    # List and Detail view ->
    if request.method == "GET":
        if pk is not None:
            queryset = Person.objects.get(id=pk)
            serializer = PersonSerializer(instance=queryset)
            return Response(serializer.data)
        queryset = Person.objects.all()
        serializer = PersonSerializer(instance=queryset, many=True)
        return Response(serializer.data)

    # Create view ->
    if request.method == "POST":
        data = request.data
        serializer = PersonSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response({'msg':'Data created successfully'})
        return Response(serializer.errors)
    
    # Update view ->
    if request.method == "PUT":
        data = request.data
        queryset = Person.objects.get(id=pk)
        serializer = PersonSerializer(instance=queryset, data=data)
        if serializer.is_valid():
            serializer.save()
            return Response({'msg':'Data updated successfully'})
        return Response(serializer.errors)

    # Delete view ->
    if request.method == "DELETE":
        queryset = Person.objects.get(id=pk)
        queryset.delete()
        return Response({"msg": "Data deleted successfully"})

    return Response({'msg' : 'Normal response'})


'''LIST API VIEW  -> '''

# To display list of products using function (GET)
@api_view(['GET'])
def productListAPIView(request, *args, **kwargs):
    queryset = Product.objects.all()
    serializer = ProductSerializer(instance=queryset, many=True).data
    return Response(serializer)

# To display list of products using class (GET)
class ProductListAPIView(ListAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

# To display list of products and also product create form using class (GET)
class ProductListCreateAPIView(ListCreateAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    permission_classes = [CustomDjangoModelPermissions]



'''DETAIL API VIEW  -> '''
# To get particulatr product data using class (GET)
class ProductDetailAPIView(RetrieveAPIView): 
    queryset = Product.objects.all()
    serializer_class = ProductSerializer



'''CREATE API VIEW  -> '''

# To create product data using class (POST)
class ProductCreateAPIView(CreateAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

    # ro add what type of authentication ->
    # authentication_classes = [authentication.SessionAuthentication]

    # to add permissions on view ->  
    # 1. AllowAny -> Any user can access and perform any type of action
    # 2. IsAuthenticated -> Only registered user can access and perform any type of action
    # 3. IsAuthenticatedOrReadOnly -> if authenticated then can pefrom any type of action else only get type of action
    # 4. IsAdminUser -> Only admin can access and perfrom any type of action
    permission_classes = [permissions.IsAuthenticated] 
    

    # to add or override data in serializer we can use below method
    '''def perform_create(self, serializer):
        serializer.save(user=self.request.user)'''



'''UPDATE API VIEW  -> '''

# To update product data using class (PUT)
class ProductUpdateAPIView(UpdateAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

    '''def perform_update(self, serializer):
        return super().perform_update(serializer)'''



'''DELETE API VIEW  -> '''

# To delete product data using class (DELETE)
class ProductDestoryAPIView(DestroyAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

    '''def perform_destroy(self, instance):
        return super().perform_destroy(instance)'''

class ProductGenericAPIView(ListModelMixin,
                            RetrieveModelMixin,
                            CreateModelMixin,
                            UpdateModelMixin,
                            DestroyModelMixin,
                            GenericAPIView):
    # generic api view allow us to create functions for different types of methods -> get, post, put, delete
    # just like base view in django

    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    lookup_field = 'pk'
    
    # ro add what type of authentication ->
    authentication_classes = [authentication.SessionAuthentication, authentication.TokenAuthentication]

    # to add permissions on view ->  
    # 1. AllowAny -> Any user can access and perform any type of action
    # 2. IsAuthenticated -> Only registered user can access and perform any type of action
    # 3. IsAuthenticatedOrReadOnly -> if authenticated then can pefrom any type of action else only get type of action
    # 4. IsAdminUser -> Only admin can access and perfrom any type of action
    # 5. DjangoModelPermissions -> using django admin panel we can assign permission(view, update, create, delete) to specofic person
    # 6. CustomPermission -> we can user our own custom permission by inheriating any built in permission as below 
    permission_classes = [CustomPermissions]


    '''
    ListModelMixin gives -> self.list 
    RetrieveModelMixin gives -> self.retrieve
    CreateModelMixin gives -> self.create
    UpdateModelMixin gives -> self.update
    DestroyModelMixin gives -> self.destroy
    '''

    # to handle list and detail view
    def get(self, request, *args, **kwargs):
        # if pk is there then it will act as detail view
        pk = kwargs.get('pk')
        if pk is not None:
            return self.retrieve(request, *args, **kwargs)
        # if not then it will act as list view
        return self.list(request, *args, **kwargs) 

    # to handle create view
    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)

    # to handle update view
    def put(self, request, *args, **kwargs):
        return self.update(request, *args, kwargs)

    # to handle delete view
    def delete(self, request, *args, **kwargs):
        return self.destroy(request, *args, **kwargs)



'''ViewSet to handle all urls internally -> '''
class ProductViewSet(viewsets.ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    lookup_field = 'pk'
    authentication_classes = [authentication.SessionAuthentication]
    permission_classes = [permissions.IsAuthenticated]

class SingerViewSet(viewsets.ModelViewSet):
    queryset = Singer.objects.all()
    serializer_class = SingerSerializer
    lookup_field = 'pk'

class SongViewSet(viewsets.ModelViewSet):
    queryset = Song.objects.all()
    serializer_class = SongSerializer
    lookup_field = 'pk'

class CodeViewSet(viewsets.ModelViewSet):
    queryset = Code.objects.all()
    serializer_class = CodeSerializer
    lookup_field = 'pk'
    authentication_classes = [JWTAuthentication]
    permission_classes = [permissions.IsAuthenticated]

class AnimeViewSet(viewsets.ModelViewSet):
    queryset = Anime.objects.all()
    serializer_class = AnimeSerializer
    lookup_field = 'pk'
    
    # for Filter ->
    '''
    filter_backends = [DjangoFilterBackend]
    # filterset_fields = '__all__'
    filterset_fields = ['name', 'ratings']
    '''

    # for search ->
    '''
    filter_backends = [SearchFilter]
    # search_fields = ['name', 'ratings']
    # search_fields = ['^name'] # it will filter based on starts with in name field
    search_fields = ['=name'] # it will filter based on exact match in name field
    '''

    # for ordering ->
    filter_backends = [OrderingFilter]
    # ordering_fields = '__all__'
    # ordering_fields = ['name']
    ordering_fields = ['name', 'ratings']




    
   
