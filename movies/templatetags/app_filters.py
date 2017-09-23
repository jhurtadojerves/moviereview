from django import template
from movies.models import Review

register = template.Library()




@register.filter(name='ratio')
def ratio(value):
    rating = Review.objects.filter(movie__slug=value)
    sum_rating = 0
    for value in  rating:
        sum_rating = sum_rating + value.rating
    len_rating = len(rating)

    if len(rating):
        ratio = round(sum_rating / len_rating)
    else:
        ratio = 0
    return range(0, ratio)


@register.filter(name='stars')
def stars(value):
    rating = Review.objects.get(id=value)
    return range(0, rating.rating)
