from rest_framework import serializers
from .models import predicts

class predictsSerializers(serializers.Modelserializers):
	class Meta:
		model=predicts
		feilds=('firstname','lastname','info')