from django.http import Http404, HttpResponse
from django.http import HttpResponseRedirect
from django.shortcuts import render
from .models import Movie
 
# data = {
#     "movies": [
#         {"id": 1, "title": "The Shawshank Redemption", "year": 1994, "description": "Two imprisoned men bond over a number of years, finding solace and eventual redemption through acts of common decency."},
#         {"id": 2, "title": "The Godfather", "year": 1972, "description": "The aging patriarch of an organized crime dynasty transfers control of his clandestine empire to his reluctant son."},
#         {"id": 3, "title": "The Godfather: Part II", "year": 1974, "description": "The early life and career of Vito Corleone in 1920s New York City is portrayed, while his son, Michael, expands and tightens his grip on the family crime syndicate."},
#         {"id": 4, "title": "The Dark Knight", "year": 2008, "description": "When the menace known as the Joker wreaks havoc and chaos on the people of Gotham, the caped crusader must come to terms with one of the greatest psychological tests of his ability to fight injustice."},
#         {"id": 5, "title": "12 Angry Men", "year": 1957, "description": "A dissenting juror in a murder trial slowly manages to convince the others that the case is not as obviously clear as it seemed in court."}
#     ]
# }

def movies(request):
    movies = Movie.objects.all()
    data = {'movies': movies}
    return render(request, 'movies/movies.html', data)

def details(request, id):
    try:
        movie = Movie.objects.get(pk=id)    
    except Movie.DoesNotExist:
        raise Http404('Given Id for the movie doesn\'t exist')

    data = {'movie': movie}
    return render(request, 'movies/details.html', data)  

def add(request):
    title =  request.POST.get('title')
    year =  request.POST.get('year')
    description = request.POST.get('description')

    if title and year and description:
        movie = Movie(title=title, year=year, description=description)
        movie.save()
        return HttpResponseRedirect('/movies')

    return render(request, 'movies/add.html')

def delete(request, id):
    try:
        movie = Movie.objects.get(pk=id)    
    except Movie.DoesNotExist:
        raise Http404('Given Id for the movie doesn\'t exist')
    movie.delete()
    return HttpResponseRedirect('/movies')
