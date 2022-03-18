from rest_framework import serializers

from core.models import Discussion, Reply


class DiscussionSerializer(serializers.ModelSerializer):

    user = serializers.SerializerMethodField()

    class Meta:
        model = Discussion
        fields = "__all__"
        ready_only_fields = ["id", "user", "slug"]
        write_only_fields = ["user_id"]

    def get_user(self, obj):
        return obj.user


class ReplySerializer(serializers.ModelSerializer):

    user = serializers.SerializerMethodField()

    class Meta:
        model = Reply
        fields = "__all__"
        ready_only_fields = ["id", "user"]
        write_only_fields = ["user_id"]

    def get_user(self, obj):
        return obj.user
