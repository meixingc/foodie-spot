from django.db import models
from django.contrib.auth.models import AbstractUser
from django.contrib.contenttypes.models import ContentType
from django.contrib.contenttypes.fields import GenericForeignKey

class User(AbstractUser):
    profile_pic = models.ImageField(upload_to='profile_pics', null=True, blank=True)
    bio = models.CharField(max_length=300, null=True, blank=True)
    has_business_profile = models.BooleanField(default=False)
    def __str__(self):
        return self.username

class BusinessProfile(models.Model):
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=50, null=False, blank=False)
    address = models.CharField(max_length=100, null=False, blank=False)
    number = models.CharField(max_length=10, null=True, blank=True)
    website = models.CharField(max_length=100, null=True, blank=True)
    def __str__(self):
        return self.name

class Review(models.Model):
    reviewer = models.ForeignKey(User, on_delete=models.CASCADE)
    business = models.ForeignKey(BusinessProfile, on_delete=models.CASCADE)
    rating = models.IntegerField(null=False, blank=False)
    review = models.CharField(max_length=300, null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return self.reviewer.username + ' reviewed ' + self.business.name

class Follower(models.Model):
    # follower is the user who is following
    follower = models.ForeignKey(User, on_delete=models.CASCADE, related_name='following')
    # followee is the user who is being followed
    followee = models.ForeignKey(User, on_delete=models.CASCADE, related_name='followers')
    class Meta:
        unique_together = ('follower', 'followee')
    def __str__(self):
        return '<' + self.follower.username + '>' + ' followed' + '<' + self.followee.username + '>'

class Post(models.Model):
    poster = models.ForeignKey(User, on_delete=models.CASCADE)
    business = models.ForeignKey(BusinessProfile, on_delete=models.CASCADE, null=True, blank=True)
    manual_business_name = models.CharField(max_length=50, null=True, blank=True)
    manual_business_address = models.CharField(max_length=100, null=True, blank=True)
    post = models.ImageField(upload_to='posts', null=False, blank=False)
    caption = models.CharField(max_length=300, null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return self.poster.username + ' posted'

class Comment(models.Model):
    commenter = models.ForeignKey(User, on_delete=models.CASCADE)
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    comment = models.CharField(max_length=300, null=False, blank=False)
    created_at = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return self.commenter.username + ' commented on ' + self.post.poster.username + "'s post"

class Like(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='likes')
    content_type = models.ForeignKey(ContentType, on_delete=models.CASCADE)
    object_id = models.PositiveIntegerField()
    content_object = GenericForeignKey('content_type', 'object_id')
    def __str__(self):
        return self.user.username + ' liked something'