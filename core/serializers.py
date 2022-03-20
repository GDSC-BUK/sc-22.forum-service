from rest_framework import serializers

from core.models import Discussion, Reply


class DiscussionSerializer(serializers.ModelSerializer):

    user = serializers.SerializerMethodField()
    replies = serializers.SerializerMethodField()

    class Meta:
        model = Discussion
        fields = "__all__"
        read_only_fields = ["id", "user", "slug"]

    def get_user(self, obj):
        return obj.user

    def get_replies(self, obj):
        return ReplySerializer(obj.replies, many=True).data


class ReplySerializer(serializers.ModelSerializer):

    user = serializers.SerializerMethodField()
    discussion = serializers.SerializerMethodField()

    class Meta:
        model = Reply
        fields = "__all__"
        read_only_fields = ["id", "discussion"]
        depth = 1

    def get_user(self, obj):
        return obj.user

    def get_discussion(self, obj):
        return obj.discussion.id
