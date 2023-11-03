from rest_framework import serializers

class Top10PollutedCitiesSerializer(serializers.Serializer):
    class Meta:
        fields = '__all__'


class Top10CleanestCitiesSerializer(serializers.Serializer):
    class Meta:
        fields = '__all__'