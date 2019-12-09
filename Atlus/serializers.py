from rest_framework import serializers
from .models import predicts

class predictsSerializers(serializers.ModelSerializer):
	class Meta:
		model=predicts
		#feilds=('firstname','lastname','info')
		fields = '__all__'