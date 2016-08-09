from rest_framework import serializers

from apps.notes.models import Note


class NoteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Note
        fields = (
            'id',
            'owner',
            'tags',
            'created',
            'title',
            'note'
        )
