from rest_framework import serializers

from Tenant.models import Interview,Position, Applicant,User


class InterviewSerializer(serializers.ModelSerializer):
    company = serializers.StringRelatedField()
    interviewer = serializers.StringRelatedField()
    applicant = serializers.StringRelatedField()
    position = serializers.StringRelatedField()

    class Meta:
        model = Interview
        fields = '__all__'


class ApplicantSerializer(serializers.ModelSerializer):
    class Meta:
        model = Applicant
        fields = '__all__'


class PositionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Position
        fields = '__all__'


class GetUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = Interview
        fields = ["name","email","company","username"]
