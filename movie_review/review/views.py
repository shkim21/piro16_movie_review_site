from django.shortcuts import render, redirect, get_object_or_404
from .models import Review, Director
from .form import ReviewForm
# Create your views here.


def review_list(request):
    reviews = Review.objects.all()

    for r in Review.objects.all():
        s = str(r.id) + ' : ' + r.title + '\n'
        print(s)


    row = Review.objects.get(id=1) # pk는 모델에서 변수로 추가 안해도 생성되는 거 다들 아시죠?
    print(row.title)
    print(type(row))#찍히는 객체의 타입도 확인을 해보자.

    rows = Review.objects.filter(title='스파이더맨')
    print("rows:", rows)
    print(type(rows))

    rows2 = Review.objects.filter(title='스파이더맨', release_date="2000")
    print("rows2:", rows2)
    print("rows2 type:", type(rows2))

    c = Review.objects.count()
    print("c:", c)

    rows = Review.objects.order_by('-id')
    for r in rows:
        print("r id:", r.id, ", r title: ", r.title)
    
    dir = Director.objects.get(pk=1)
    # new_review = Review.objects.create(title="kingsman", director2=dir)
    # new_review.save()#저장을 해야 db에 반영이 된다!

    lt = Review.objects.filter(release_date__lt = 2020)
    print("lt:", lt)
    start = Review.objects.filter(title__startswith="스")
    print("start:", start)

    all = Review.objects.all()
    print(all.query)
    queryset = Review.objects.filter(title__startswith='스') | Review.objects.filter(director__startswith='크')
    print("queryset:", queryset)


    rev1 = Review.objects.all().values('title', 'content')
    rev2 = Review.objects.all().values_list('title', 'content')
    rev3 = Review.objects.all().only('title', 'content')
    print("rev1:", rev1)
    print("rev2:", rev2)
    print("rev3:", rev3)
    print("rev3 type:", type(rev3.first()))

    ctx = {'reviews': reviews}

    return render(request, template_name='movie_list.html', context=ctx)


def detail(request, pk):
    review = Review.objects.get(id=pk)
    # review2 = get_object_or_404(Review, pk=10)
    # print("review2:" ,review2)
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
        print("request.GET:", request.GET)
        form = ReviewForm(instance=review)
        ctx = {'form': form, 'review': review}

        return render(request, template_name='movie_form.html', context=ctx)


def review_delete(request, pk):
    review = Review.objects.get(id=pk)
    review.delete()
    return redirect('review:list')
