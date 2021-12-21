from django.shortcuts import render, redirect, get_object_or_404
from .models import Review
from .form import ReviewForm
# Create your views here.

def review_list(request):
    reviews = Review.objects.all()
    ctx = {'reviews': reviews}

    return render(request, template_name='movie_list.html', context=ctx)

def detail(request, pk):
    review = Review.objects.get(id=pk)
    ctx = {'review': review}

    return render(request, template_name='movie_detail.html', context=ctx)

def create(request):
    if request.method == 'POST':
        form = ReviewForm(request.POST)
        if form.is_valid():
            review = form.save()
            return redirect("review:list")
    else:
        form = ReviewForm()
        ctx = {'form': form}

        return render(request, template_name='movie_form.html', context=ctx)


def review_update(request, pk):
    review = get_object_or_404(Review, id=pk)

    if request.method == 'POST':
        form = ReviewForm(request.POST, instance=review)
        if form.is_valid():
            review = form.save()
            return redirect('review:detail', pk)

    else:
        form = ReviewForm(instance=review)
        ctx={'form': form}

        return render(request, template_name='movie_form.html', context=ctx)

def review_delete(request, pk):
    review = Review.objects.get(id=pk)
    review.delete()
    return redirect('review:list')