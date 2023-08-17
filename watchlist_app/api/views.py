from watchlist_app.models import Movie, Watchlist, StreamPlatform, Review
from watchlist_app.api.serializers import MovieSerializers, WatchlistSerializers, StreamPlatformSerializers, ReviewSerializers
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status
from rest_framework.views import APIView
from rest_framework import generics
from rest_framework import mixins
from rest_framework import viewsets
from django.shortcuts import get_object_or_404
from rest_framework.exceptions import ValidationError
from rest_framework.permissions import IsAuthenticated, IsAuthenticatedOrReadOnly
from watchlist_app.api.permissions import AdminOrReadonly, ReviewUserOrReadonly

@api_view(['GET', 'POST'])
def movie_list(request):

    if request.method == 'GET':

        movies = Movie.objects.all()
        serializer = MovieSerializers(movies, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
    
    if request.method == 'POST':

        serializer = MovieSerializers(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET', 'PUT', 'DELETE'])
def movie_details(request, pk):

    if request.method == 'GET':
        try:
            movie = Movie.objects.get(pk=pk)
        except Movie.DoesNotExist:
            return Response({'Error': 'Movie Not Found'}, status=status.HTTP_404_NOT_FOUND)
        
        serializer = MovieSerializers(movie)
        return Response(serializer.data, status=status.HTTP_200_OK)
    
    if request.method == 'PUT':

        movie = Movie.objects.get(pk=pk)
        serializer = MovieSerializers(movie, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    if request.method == 'DELETE':
        movie = Movie.objects.get(pk=pk)
        movie.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    
class MovieListAV(APIView):

    def get(self, request):
        movies = Movie.objects.all()
        serializer = MovieSerializers(movies, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
    
    def post(self, request):
        serializer = MovieSerializers(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        
        

class MovieDetailAV(APIView):

    def get(self, request, pass_pk):

        try:
            movie = Movie.objects.get(pk=pass_pk)
        except Movie.DoesNotExist:
            return Response({'Error': 'Movie Not Found'}, status=status.HTTP_404_NOT_FOUND)
        
        serializer = MovieSerializers(movie)
        return Response(serializer.data, status=status.HTTP_200_OK)


    def put(self, request, pass_pk):

        movie = Movie.objects.get(pk=pass_pk)
        serializer = MovieSerializers(movie, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
            
    
        
    def delete(self, request, pass_pk):
        movie = Movie.objects.get(pk=pass_pk)
        movie.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

 #-------------------------------------------------------------------------------------------------   

class WatchListAV(APIView):

    def get(self, request):
        movies = Watchlist.objects.all()
        serializer = WatchlistSerializers(movies, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
    
    def post(self, request):
        serializer = WatchlistSerializers(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        

class WatchDetailAV(APIView):

    def get(self, request, pk):

        try:
            movie = Watchlist.objects.get(pk=pk)
        except Watchlist.DoesNotExist:
            return Response({'Error': 'Movie Not Found'}, status=status.HTTP_404_NOT_FOUND)
        
        serializer = WatchlistSerializers(movie)
        return Response(serializer.data, status=status.HTTP_200_OK)
    
    def put(self, request, pk):

        movie = Watchlist.objects.get(pk=pk)
        serializer = WatchlistSerializers(movie, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        
    def delete(self, request, pk):
        movie = Watchlist.objects.get(pk=pk)
        movie.delete()
        return Response({'Deleted': 'Watchlist with passed pk is deleted'},status=status.HTTP_204_NO_CONTENT)
    

class StreamPlatformAV(APIView):

    def get(self, request):
        platform = StreamPlatform.objects.all()
        serializer = StreamPlatformSerializers(platform, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
    
    def post(self, request):
        serializer = StreamPlatformSerializers(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        
class StreamPlatformDetailAV(APIView):

    def get(self, request, pk):

        try:
            platform = StreamPlatform.objects.get(pk=pk)
        except StreamPlatform.DoesNotExist:
            return Response({'Error': 'StreamPlatform does Not Found'}, status=status.HTTP_404_NOT_FOUND)
        
        serializer = StreamPlatformSerializers(platform)
        return Response(serializer.data, status=status.HTTP_200_OK)
    
    
    def put(self, request, pk):

        platform = StreamPlatform.objects.get(pk=pk)
        serializer = StreamPlatformSerializers(platform, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        
    def delete(self, request, pk):
        platform = StreamPlatform.objects.get(pk=pk)
        platform.delete()
        return Response({'Deleted': 'StreamPlatform is deleted'}, status=status.HTTP_204_NO_CONTENT)
    
# Generic API Views and Mixins

class ReviewList(mixins.ListModelMixin, mixins.CreateModelMixin, generics.GenericAPIView):

    # Reviews of all the moviess
    queryset = Review.objects.all()
    serializer_class = ReviewSerializers

    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)
    
class ReviewDetail(mixins.RetrieveModelMixin, mixins.UpdateModelMixin, mixins.DestroyModelMixin, generics.GenericAPIView):
    queryset = Review.objects.all()
    serializer_class = ReviewSerializers

    def get(self, request, *args, **kwargs):
        return self.retrieve(request, *args, **kwargs)
    
    def put(self, request, *args, **kwargs):
        return self.update(request, *args, **kwargs)

    def delete(self, request, *args, **kwargs):
        return self.destroy(request, *args, **kwargs)


# Concrete view classes for Review model

class ConcreteReviewList(generics.ListCreateAPIView):
    queryset = Review.objects.all()
    serializer_class = ReviewSerializers

class ConcreteReviewDetail(generics.RetrieveUpdateDestroyAPIView):

    #permission_classes = [IsAuthenticatedOrReadOnly]
    permission_classes = [AdminOrReadonly]
    #permission_classes = [ReviewUserOrReadonly]
    
    
    queryset = Review.objects.all()
    serializer_class = ReviewSerializers

# Concrete view classes for model StreamPlatform and Watchlist (For practice)

class ConcreteWatchList(generics.ListCreateAPIView):
    queryset = Watchlist.objects.all()
    serializer_class = WatchlistSerializers

class ConcreteWatchListDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Watchlist.objects.all()
    serializer_class = WatchlistSerializers

class ConcreteStreamPlatform(generics.ListCreateAPIView):
    queryset = StreamPlatform.objects.all()
    serializer_class = StreamPlatformSerializers

class ConcreteStreamPlatformDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = StreamPlatform.objects.all()
    serializer_class = StreamPlatformSerializers


# Concrete view classes to get reviews of particular movie
class ConcreteWatchReviewList(generics.ListAPIView):

    # queryset = Review.objects.all()
    # overriding the above line by function
    serializer_class = ReviewSerializers
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        # pk = self.kwargs['passkey']
        # or you can use above line
        pk = self.kwargs.get('passkey')
        movie_review = Review.objects.filter(watchlist=pk)
        #print(movie_review)
        return movie_review

# Concrete view classes to get Create a review for particular movie
class ConcreteWatchReviewCreate(generics.CreateAPIView):
    serializer_class = ReviewSerializers

    def get_queryset(self):
        return Review.objects.all()

    def perform_create(self, serializer):
        
        # pk = self.kwargs.get('trykey')
        # or you can use above line
        pk = self.kwargs['trykey']
        get_movie = Watchlist.objects.get(pk=pk)
        #print(movie)

        get_review_user = self.request.user
        review_queryset = Review.objects.filter(watchlist = get_movie, review_user = get_review_user)
        if review_queryset.exists():
            raise ValidationError("You have already reviewed this movie")
        
        if get_movie.number_rating == 0:
            get_movie.avg_rating = serializer.validated_data['rating']
            print(serializer.validated_data['rating'])
        else:
            get_movie.avg_rating = (get_movie.avg_rating + serializer.validated_data['rating']) / 2

        get_movie.number_rating = get_movie.number_rating + 1
        get_movie.save()


        serializer.save(watchlist = get_movie, review_user = get_review_user)
    
class ConcreteWatchReviewDetail(generics.RetrieveUpdateDestroyAPIView):
    
    queryset = Review.objects.all()
    serializer_class = ReviewSerializers
    permission_classes = [ReviewUserOrReadonly]

# Using Viewset and Routers

class StreamPlatformViewset(viewsets.ViewSet):

    def list(self, request):
        queryset = StreamPlatform.objects.all()
        serializer = StreamPlatformSerializers(queryset, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def retrieve(self, request, pk=None):
        queryset = StreamPlatform.objects.all()
        watchlist = get_object_or_404(queryset, pk=pk)
        serializer = StreamPlatformSerializers(watchlist)
        return Response(serializer.data, status=status.HTTP_200_OK)
    
    def create(self, request):
        serializer = StreamPlatformSerializers(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def update(self, request, pk=None):
        platform = StreamPlatform.objects.get(pk=pk)
        serializer = StreamPlatformSerializers(platform, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def partial_update(self, request, pk=None):
        platform = StreamPlatform.objects.get(pk=pk)
        serializer = StreamPlatformSerializers(platform, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def destroy(self, request, pk=None):
        platform = StreamPlatform.objects.get(pk=pk)
        platform.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


# model viewset

class StreamPlatformMV(viewsets.ModelViewSet):
    queryset = StreamPlatform.objects.all()
    serializer_class = StreamPlatformSerializers

class ReviewMV(viewsets.ModelViewSet):
    queryset = Review.objects.all()
    serializer_class = ReviewSerializers

# readonly model viewset

class ReviewROMV(viewsets.ReadOnlyModelViewSet):
    queryset = Review.objects.all()
    serializer_class = ReviewSerializers