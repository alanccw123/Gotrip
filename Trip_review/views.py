import json

from django.forms import forms
from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.views.decorators.csrf import csrf_exempt
from Trip_review import models


# Create your views here.
def review(request):
    # get all the reviews in database
    user_review = models.Review.objects.all().order_by('-Review_id')
    return render(request, 'review.html', {'review': user_review})


def review_delete(request):
    review_id = request.GET.get('review_id')
    # change status to 2
    models.Review.objects.filter(id=review_id).update(delete_status=1)

    # go back to trip detail page after deleting
    return redirect(request, '/review/')


@csrf_exempt
def review_add(request):
    if request.method == 'POST':
        # data = request.POST
        # date = data.get('time')
        # rating = data.get('rating')
        # content = data.get('content')
        # trip_id = data.get('trip_id')
        # Username = data.get('username')
        # models.Review.objects.create(date=date, rating=rating, content=content, delete_status=0, Trip_id = trip_id, User_name = username)
        print(request.POST)
        res = {'status': True}
        json_str = json.dumps(res)
        return HttpResponse(json_str)
