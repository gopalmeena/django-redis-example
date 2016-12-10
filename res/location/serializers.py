from rest_framework import serializers
from location.models import Country,State,City

class CountrySerializer(serializers.ModelSerializer):

	# def create(self,validated_data):
	# 	return Country.objects.create(**validated_data)

	# def update(self,instance,validated_data):
	# 	instance.country_id = validated_data.get('country_id',instance.country_id)
	# 	instance.name = validated_data.get('name',instance.name)
	# 	instance.code = validated_data.get('code',instance.code)
	# 	instance.save()
	# 	return instance

	class Meta:
		model = Country
		# fields = ('country_id','name','code')
		fields = '__all__'

class StateSerializer(serializers.ModelSerializer):

	# def create(self,validated_data):
	# 	return State.objects.create(**validated_data)

	# def update(self,instance,validated_data):
	# 	instance.state_id = validated_data.get('state_id',instance.state_id)
	# 	instance.name = validated_data.get('name',instance.name)
	# 	instance.code = validated_data.get('code',instance.code)
	# 	instance.country = validated_data.get('country',instance.country)
	# 	instance.save()
	# 	return instance

	class Meta:
		model = State
		# fields = ('state_id','name','code','country')
		fields = '__all__'

class CitySerializer(serializers.ModelSerializer):

	# def create(self,validated_data):
	# 	return City.objects.create(**validated_data)

	# def update(self,instance,validated_data):
	# 	instance.city_id = validated_data.get('city_id',instance.city_id)
	# 	instance.name = validated_data.get('name',instance.name)
	# 	instance.code = validated_data.get('code',instance.code)
	# 	instance.state = validated_data.get('state',instance.state)
	# 	instance.save()
	# 	return instance

	class Meta:
		model = City
		# fields = ('city_id','name','code','state')
		fields = '__all__'