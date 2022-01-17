from django.shortcuts import render, redirect, get_object_or_404
from .models import Review, Director
from .form import ReviewForm
# Create your views here.


def review_list(request):
    reviews = Review.objects.all()
    ctx = {'reviews': reviews}

    return render(request, template_name='movie_list.html', context=ctx)


def detail(request, pk):
    review = Review.objects.get(id=pk)
    hour = 0
    minute = 0
    if int(review.running_time) > 60:
        hour = int(review.running_time) // 60
        minute = int(review.running_time) % 60
    print("hour:", hour)
    print("minute:", minute)
    print("review.running_time:", review.running_time)
    print("review:", review)
    print("review:", type(review))

    print("review.director2:", review.director2)

    director2= Director.objects.get(id=1)
    print("director2:", director2)
    print("director2.review_set.all():", director2.review_set.all().first())


    ctx = {'review': review, 'hour': hour, 'minute': minute}

    return render(request, template_name='movie_detail.html', context=ctx)


def create(request):
    if request.method == 'POST':
        form = ReviewForm(request.POST)
        if form.is_valid():
            review = form.save()
            return redirect("review:list")
    else:
        form = ReviewForm()
        print()
        ctx = {'form': form}

        return render(request, template_name='movie_form.html', context=ctx)


def review_update(request, pk):
    review = get_object_or_404(Review, id=pk)

    if request.method == 'POST':
        print("request method:", request.method)
        form = ReviewForm(request.POST, instance=review)
        # print("form:", form)
        print("request:", request)
        print("request.POST:", request.POST)
        print("request.FILES:", request.FILES)
        review.title = request.POST.get("title")
        review.release_date = request.POST.get("release_date")
        review.genre = request.POST.get("genre")
        review.rating = request.POST.get("rating")
        review.running_time = request.POST.get("running_time")
        review.content = request.POST.get("content")
        review.director = request.POST.get("director")
        review.actor = request.POST.get("actor")
        review.image = request.FILES.get('poster')
        print("review.image :", review.image)
        review.save()
        return redirect('review:detail', pk)

        # if form.is_valid():
        #     print("form valid")
        #     review = form.save()
        #     return redirect('review:detail', pk)
        # else:
        #     print("no valid")

    else:
        form = ReviewForm(instance=review)
        ctx = {'form': form, 'review': review}

        return render(request, template_name='movie_form.html', context=ctx)


def review_delete(request, pk):
    review = Review.objects.get(id=pk)
    review.delete()
    return redirect('review:list')
