from django.urls import path

from core.api import (
    ReplyDiscussionAPI,
    RetrieveUpdateDestroyReplyAPI,
    RetriveUpdateDestroyDiscussionAPI,
    StartDiscussionAPI,
)

app_name = "core"

urlpatterns = [
    path("discussion/", StartDiscussionAPI.as_view(), name="start_discussion"),
    path(
        "discussion/<uuid:discussion_id>/",
        RetriveUpdateDestroyDiscussionAPI.as_view(),
        name="rud_discussion",
    ),
    path(
        "reply/<uuid:discussion_id>/new/",
        ReplyDiscussionAPI.as_view(),
        name="reply_discussion",
    ),
    path(
        "reply/<uuid:reply_id>/",
        RetrieveUpdateDestroyReplyAPI.as_view(),
        name="rud_reply",
    ),
]
