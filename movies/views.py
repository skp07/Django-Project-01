from django.shortcuts import render, redirect, get_object_or_404
from .models import MovieInfo, Comment
from movies.forms import CommentForm
from django.contrib.auth import authenticate, login
from django.contrib.auth.forms import UserCreationForm
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.db.models import Q



def home(request):
    template_name = 'movies/homepage.html'
    return render(request, template_name)


def details(request, movie_id):
    movie = get_object_or_404(MovieInfo, pk=movie_id)
    context = {'movie': movie}
    template_name = 'movies/details.html'
    return render(request, template_name, context)


def add_comment(request, pk):
    post = get_object_or_404(MovieInfo, pk=pk)
    if request.method == 'POST':
        form = CommentForm(request.POST)

        if form.is_valid():
            comment = form.save(commit=False)
            comment.post = post
            comment.save()
            return redirect('/movies/' + str(post.pk) + "/", pk=post.pk)
    else:
        form = CommentForm()
    return render(request, 'movies/add_comments.html', {'form': form})


def delete_comment(request, pk):
    if not request.user.is_authenticated():
        return render(request, 'movies/login.html')
    else:
        comment = get_object_or_404(Comment, pk=pk)
        comment.delete()
        return redirect('/movies/' + str(comment.post.pk) + "/", pk=comment.post.pk)


def signup(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)

        if form.is_valid():
            form.save()

            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=raw_password)

            try:
                login(request, user)
            except AttributeError:
                return redirect('/movies/login/')

    else:
        form = UserCreationForm()
    return render(request, 'movies/signup.html', {'form': form})


def index(request):
    movie_list = MovieInfo.objects.all()
    page = request.GET.get('page', 1)

    # search engine
    query = request.GET.get('q')
    if query:
        movie_list = movie_list.filter(
            Q(movie_title__icontains=query)|
            Q(director__icontains=query)|
            Q(genre__icontains=query)|
            Q(starring__icontains=query)|
            Q(year__icontains=query)
        ).distinct()
    # ---------
    paginator = Paginator(movie_list, 4)
    try:
        movies = paginator.page(page)
    except PageNotAnInteger:
        movies = paginator.page(1)
    except EmptyPage:
        movies = paginator.page(paginator.num_pages)

    return render(request, 'movies/index.html', {'movies': movies})



