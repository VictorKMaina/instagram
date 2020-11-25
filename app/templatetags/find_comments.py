from django import template
from ..models import Comment

register = template.Library()

@register.filter(name="by_image")
def by_image(comments, image):
    """
    Return comments filtered by image id
    """
    
    comments = Comment.find_by_image(image).reverse()
    return comments

@register.filter(name="by_image_short")
def by_image_short(comments, image):
    """
    Return comments filtered by image id
    """
    all_comments = by_image(comments, image)
    
    return all_comments[0:2]