from django.shortcuts import get_object_or_404
from rest_framework.response import Response
from rest_framework import status

from forum.permissions import IsAuthenticatedOrReadOnly
from forum.utils import View
from core.models import Discussion, Reply
from core.serializers import DiscussionSerializer, ReplySerializer


class StartDiscussionAPI(View):

    serializer_class = DiscussionSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]
    queryset = Discussion.objects.all()

    # POST /discussion/
    def post(self, request):
        discussion_data = request.data

        create_discussion_serializer = self.get_serializer(data=discussion_data)
        create_discussion_serializer.is_valid(raise_exception=True)
        create_discussion_serializer.save(user_id=self.user["id"])

        return Response(
            create_discussion_serializer.data, status=status.HTTP_201_CREATED
        )

    # GET /discussion/
    def get(self, request):
        serialized_discussions = self.get_serializer(self.get_queryset(), many=True)

        return Response(serialized_discussions.data, status=status.HTTP_200_OK)


class RetriveUpdateDestroyDiscussionAPI(View):

    serializer_class = DiscussionSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]

    # GET /discussion/:discussion_id
    def get(self, request, discussion_id):
        discussion = get_object_or_404(Discussion, id=discussion_id)

        discussion_serializer = self.get_serializer(discussion)

        return Response(discussion_serializer.data, status=status.HTTP_200_OK)

    # PUT /discussion/:discussion_id
    def put(self, request, discussion_id):
        discussion = get_object_or_404(Discussion, id=discussion_id)
        discussion_update_data = request.data

        update_discussion_serializer = self.get_serializer(
            discussion, data=discussion_update_data, partial=True
        )
        update_discussion_serializer.is_valid(raise_exception=True)
        update_discussion_serializer.save()

        return Response(update_discussion_serializer.data, status=status.HTTP_200_OK)

    # DELETE /discussion/:discussion_id
    def delete(self, request, discussion_id):
        discussion = get_object_or_404(Discussion, id=discussion_id)
        discussion.delete()

        return Response(None, status=status.HTTP_204_NO_CONTENT)


class ReplyDiscussionAPI(View):

    serializer_class = ReplySerializer
    permission_classes = [IsAuthenticatedOrReadOnly]

    # POST /reply/:discussion_id/new/
    def post(self, request, discussion_id):
        reply_data = request.data
        discussion = get_object_or_404(Discussion, id=discussion_id)

        reply_serializer = self.get_serializer(data=reply_data)
        reply_serializer.is_valid(raise_exception=True)
        reply_serializer.save(user_id=self.user["id"], discussion=discussion)

        return Response(reply_serializer.data, status=status.HTTP_201_CREATED)


class RetrieveUpdateDestroyReplyAPI(View):

    serializer_class = ReplySerializer
    permission_classes = [IsAuthenticatedOrReadOnly]

    # GET /reply/:reply_id/
    def get(self, request, reply_id):
        reply = get_object_or_404(Reply, id=reply_id)

        reply_serializer = self.get_serializer(reply)

        return Response(reply_serializer.data, status=status.HTTP_201_CREATED)

    # PUT /reply/:reply_id/
    def put(self, request, reply_id):
        reply = get_object_or_404(Reply, id=reply_id)
        update_reply_data = request.data

        update_reply_serializer = self.get_serializer(
            reply, data=update_reply_data, partial=True
        )
        update_reply_serializer.is_valid(raise_exception=True)
        update_reply_serializer.save()

        return Response(update_reply_serializer.data, status=status.HTTP_200_OK)

    # DELETE /reply/:reply_id/
    def delete(self, request, reply_id):
        reply = get_object_or_404(Reply, id=reply_id)
        reply.delete()

        return Response(None, status=status.HTTP_204_NO_CONTENT)
