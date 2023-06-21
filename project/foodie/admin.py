from django.contrib import admin
from .models import User, BusinessProfile, Review, Follower, Post, Comment, Like

admin.site.register(User)
admin.site.register(BusinessProfile)
admin.site.register(Review)
admin.site.register(Follower)
admin.site.register(Post)
admin.site.register(Comment)
admin.site.register(Like)