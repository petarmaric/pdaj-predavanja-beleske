from rest_framework import serializers

from .monte_pi import chaos_computing


class ComputeParams(serializers.Serializer):
    # input params
    broj_virsli = serializers.IntegerField(min_value=10, max_value=10**7)

    # results
    pi_estimate = serializers.SerializerMethodField()

    def get_pi_estimate(self, obj):
        return chaos_computing(obj['broj_virsli'])

    def create(self, validated_data):
        return self.validated_data
