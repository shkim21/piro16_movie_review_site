from django.shortcuts import render, redirect, get_object_or_404
from .models import Review, Director, Actor
from .form import ReviewForm
# Create your views here.
from django.db.models import Q
from django.http import HttpResponse



def review_list(request):
    reviews = Review.objects.all()
    # print("reviews:", type(reviews))


    # print("reviews.title:",reviews.title)

    # for r in Review.objects.all():
    #     print("r type:", type(r))
    #     s = str(r.id) + ' : ' + r.title + '\n'
    #     print(s)

    # row = Review.objects.get(title="스파이더맨: 노 웨이 홈") # pk는 모델에서 변수로 추가 안해도 생성되는 거 다들 아시죠?
    # print(row.title)
    # print(type(row))#찍히는 객체의 타입도 확인을 해보자.

    reviews = Review.objects.all()
    print("reviews:", reviews)
    # rows = Review.objects.filter(Q(title='스파이더맨') | Q(release_date="2016"))

    # rows = Review.objects.exclude(title='스파이더맨')
    # print("rows:", rows)
    # c = Review.objects.exclude(title='스파이더맨').count()
    # print("c:", c)
    rows = Review.objects.order_by('?').first()
    print("rows type:", type(rows))
    # for r in rows:
    #     print("r id:", r.id, ", r title: ", r.title)


    ctx = {'reviews': reviews}

    return render(request, template_name='movie_list.html', context=ctx)

def ex(request):
    print("ex enter")
    response = HttpResponse("<div>Hello World!</div>")
    return response


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

    print("director:", review.director)

    dir = Director.objects.get(name="존 왓츠")
    print("dir:", dir)
    print("director2.review_set.all():", dir.review_set.all())


    actor = Actor.objects.get(pk=1)
    print("actors:", actor)
    print("actors set all:", actor.review_set.all())

    print("review.all", review.actor.all())
    actors = review.actor.all()

    ctx = {'review': review, 'hour': hour, 'minute': minute, "actors":actors}

    return render(request, template_name='movie_detail.html', context=ctx)


def create(request):
    if request.method == 'POST':
        form = ReviewForm(request.POST)
        if form.is_valid():
            review = form.save()
            return redirect("review:list")
    else:
        print("here!")
        print(request.method)
        print("request.GET:", request.GET)
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
        print("request.POST:", request.POST) #request.POST로 들어오는 것 전부 출력!
        print("request.FILES:", request.FILES)
        review.title = request.POST.get("title")
        review.release_date = request.POST.get("release_date")
        review.genre = request.POST.get("genre")
        review.rating = request.POST.get("rating")
        review.running_time = request.POST.get("running_time")
        review.content = request.POST.get("content")

        get_dir_name = request.POST.get("director")
        direc = Director.objects.get(name=get_dir_name)
        review.director = direc

        get_act_name = request.POST.get("actor")
        act = Actor.objects.get(name=get_act_name)
        review.actor.add(act)#manyto many field save

        poster = request.FILES.get('poster')
        review.image = poster
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
    # return render(request, template_name='movie_list.html', context=ctx)
