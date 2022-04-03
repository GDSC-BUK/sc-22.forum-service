from django.db import models

from forum.utils import BaseModel


class Discussion(BaseModel):

    user_id = models.UUIDField(db_index=True)
    title = models.CharField(max_length=255, blank=False)
    body = models.TextField()
    slug = models.SlugField(max_length=255, unique=True, blank=True)

    class Meta:
        verbose_name = "Discussion"
        verbose_name_plural = "Disucssions"

    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        if not self.slug:
            self.unique_slugify(self.title, "slug")

        super(Discussion, self).save(*args, **kwargs)

    # custom methods / properties

    @property
    def user(self):
        return self.user_id

    @property
    def replies(self):
        return Reply.objects.filter(discussion_id=self.id)


class Reply(BaseModel):

    user_id = models.UUIDField()
    discussion = models.ForeignKey(Discussion, on_delete=models.CASCADE)
    body = models.TextField(blank=False)
    reply = models.ForeignKey(
        "self", on_delete=models.SET_NULL, null=True, related_name="discussion_reply"
    )

    class Meta:
        verbose_name = "Reply"
        verbose_name_plural = "Replies"

    def __str__(self):
        return self.user_id

    # custom methods / properties

    @property
    def user(self):
        return self.user_id
