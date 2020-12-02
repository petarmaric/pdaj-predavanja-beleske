from rest_framework import serializers


class ComputeParams(serializers.Serializer):
    # input params
    broj_virsli = serializers.IntegerField(min_value=10)

    # results
    pi_estimate = serializers.FloatField(read_only=True)

