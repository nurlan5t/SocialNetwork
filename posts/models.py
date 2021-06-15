from django.db import models
from users.models import User

class Post(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=150)
    description = models.TextField()

    def __str__(self):
        return self.title

Like = 1
UnLike = 2

like_types = (
    (Like, 'Like'),
    (UnLike, 'UnLike'),
)


class Like(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='likes')
    created = models.DateTimeField(auto_now_add=True)
    like = models.IntegerField(choices=like_types, default=None, blank=True)

    def __str__(self):
        return 'User: {}, Post: {}, - {}'.format(self.user, self.post, self.get_like_display())