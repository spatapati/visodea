#
# Copyright 2008 Darrel Herbst
#
# This file is part of Django-Rabid-Ratings.
#
# Django-Rabid-Ratings is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# Django-Rabid-Ratings is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with Django-Rabid-Ratings.  If not, see <http://www.gnu.org/licenses/>.
#

from django import template
from ratings.models import Rating, RatingEvent
from ratings import settings

register = template.Library()

def show_rating(context, rating_key):
    """ 
    displays necessary html for the rating
    """
    rating, created = Rating.objects.get_or_create(key=rating_key)
    return {
        'rating_key': rating_key,
        'total_votes': rating.total_votes,
        'total_ratings': rating.total_rating,
        'rating': rating.avg_rating,
        'percent': rating.percent,
        'max_stars': 5
        }
register.inclusion_tag("ratings/rating.html", takes_context=True)(show_rating)

def rating_header(context):
    """
    Inserts the includes needed into the html
    """
    return { 'ratings_media_url': settings.MEDIA_URL }

register.inclusion_tag("ratings/rating_header.html", takes_context=True)(rating_header)

