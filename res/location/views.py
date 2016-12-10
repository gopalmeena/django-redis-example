from django.shortcuts import render
from rest_framework.generics import ListAPIView
from rest_framework.views import APIView
from location.models import Country,State,City
from location.serializers import CountrySerializer,StateSerializer,CitySerializer
from rest_framework_swagger.views import get_swagger_view
from rest_framework.response import Response
from rest_framework.renderers import JSONRenderer
from rest_framework.parsers import JSONParser
from rest_framework.response import Response
from rest_framework import status
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse
import json
import requests
import redis
# from rest_framework.response import Response


# Create your views here.
# class CountryListView(ListAPIView):

# 	serializer_class = CountrySerializer

r = redis.StrictRedis(host='localhost',port=6379,db=0)

p = r.pubsub()
p.subscribe('channel1','channel2','channel3')
a = True
c = 'country_'
st = 'state_'
ci = 'city_'

while a:
	s = p.get_message()
	import pdb
	pdb.set_trace()
	if s:
		s['data'] = int(s['data'])
		if s['channel']=='channel1':
			if s['data']=='all':
				c_key = c+s['data']
				# r.set(c_key,json.loads(JSONRenderer().render(CountrySerializer(Country.objects.all(),many=True).data)))
				r.set(c_key,json.loads(CountrySerializer(Country.objects.all(),many=True).data))
			elif s['data']>0:
				s['data'] = str(s['data'])
				c_key = c+s['data']
				# r.set(c_key,json.loads(JSONRenderer().render(CountrySerializer(Country.objects.get(country_id=s['data'])))))
				r.set(c_key,json.loads(CountrySerializer(Country.objects.get(country_id=s['data']))))
		elif s['channel']=='channel2':
			if s['data']=='all':
				c_key = st+s['data']
				# r.set(c_key,json.loads(JSONRenderer().render(StateSerializer(State.objects.all(),many=True).data)))
				r.set(c_key,json.loads(StateSerializer(State.objects.all(),many=True).data))
			elif s['data']>0:
				s['data'] = str(s['data'])
				c_key = st+s['data']
				# r.set(c_key,json.loads(JSONRenderer().render(StateSerializer(State.objects.get(state_id=s['data'])))))
				r.set(c_key,json.loads(StateSerializer(State.objects.get(state_id=s['data']))))
		elif s['channel']=='channel3':
			if s['data']=='all':
				c_key = ci+s['data']
				# r.set(c_key,json.loads(JSONRenderer().render(CitySerializer(City.objects.all(),many=True).data)))
				r.set(c_key,json.loads(CitySerializer(City.objects.all(),many=True).data))
			elif s['data']>0:
				s['data'] = str(s['data'])
				c_key = ci+s['data']
				# r.set(c_key,json.loads(JSONRenderer().render(CitySerializer(City.objects.get(city_id=s['data'])))))
				r.set(c_key,json.loads(CitySerializer(City.objects.get(city_id=s['data']))))
	else:
		print 'Nothig there in pubusb()'
	print 'Caching done'

@csrf_exempt
def country_list(request):
	if request.method == 'GET':
		try:
			if r.get(c+'all')!=None:
				data1 = r.get(c+'all')
				print 'from Cache'
			else:
				countries = Country.objects.all()
				print "Countries = ",countries
				serializer = CountrySerializer(countries,many=True)
				data1 = JSONRenderer().render(serializer.data)
				data1 = json.loads(data1)
				print 'from DB'

			return JsonResponse({'data':data1},status=status.HTTP_200_OK)
		except:
			return JsonResponse({'Status':'No Data in Country List'},status = status.HTTP_200_OK)
	elif request.method == 'POST':
		# import pdb; pdb.set_trace()
		# data = JSONParser().parse(request.data)
		country_obj = Country.objects.create(code=request.POST.get('code'), 
				name=request.POST.get('name'))
		# serializer = CountrySerializer(data=data)
		# if serializer.is_valid():
		# 	serializer.save()
		r.publish('channel1','all')
		r.publish('channel1',country_obj.country_id)
		return JsonResponse({'Status':'Country Successfully Added'},status=status.HTTP_201_CREATED)
		# return JsonResponse(serializer.errors,status=status.HTTP_400_BAD_REQUEST)

@csrf_exempt
def country_list_with_pk(request,pk):

	if request.method == 'GET':
		try:
			if r.get(c+pk)!=None:
				data1 = r.get(c+pk)
				print 'from cache'
			else:
				print 'from DB'
				country = Country.objects.get(country_id=pk)
				serializer = CountrySerializer(country)
				data1 = JSONRenderer().render(serializer.data)
				data1 = json.loads(data1)

			return JsonResponse({'data':data1},status=status.HTTP_200_OK)
		except Country.DoesNotExist:
			return JsonResponse({'Status':'Invalid Country Primary Key'},status = status.HTTP_400_BAD_REQUEST)

# class StateListView(ListAPIView):

# 	serializer_class = StateSerializer


# class CityListView(ListAPIView):

# 	serializer_class = CitySerializer


@csrf_exempt
def state_list(request):
	if request.method == 'GET':
		try:
			states = State.objects.all()
			serializer = StateSerializer(states,many=True)
			data1 = JSONRenderer().render(serializer.data)
			data1 = json.loads(data1)
			return JsonResponse({'data':data1},status=status.HTTP_200_OK)
		except:
			return JsonResponse({'Status':'No Data in State List'},status = status.HTTP_200_OK)
	elif request.method == 'POST':
		# import pdb; pdb.set_trace()
		# data = JSONParser().parse(request.data)
		state_obj = State.objects.create(code=request.POST.get('code'), 
				name=request.POST.get('name'),country_id=request.POST.get('country_id'))
		# serializer = CountrySerializer(data=data)
		# if serializer.is_valid():
		# 	serializer.save()
		return JsonResponse({'Status':'State Successfully Added'},status=status.HTTP_201_CREATED)
		return JsonResponse(serializer.errors,status=status.HTTP_400_BAD_REQUEST)

@csrf_exempt
def state_list_with_pk(request,pk):
	try:
		state = State.objects.get(state_id=pk)
	except State.DoesNotExist:
		return JsonResponse({'Status':'Invalid State Primary Key'},status=HTTP_400_BAD_REQUEST)

	if request.method == 'GET':
		try:
			serializer = StateSerializer(state)
			data1 = JSONRenderer().render(serializer.data)
			data1 = json.loads(data1)
			return JsonResponse({'data':data1},status=status.HTTP_200_OK)
		except:
			return JsonResponse({'Status':'No Data in State List'},status = status.HTTP_200_OK)



@csrf_exempt
def city_list(request):
	if request.method == 'GET':
		try:
			cities = City.objects.all()
			serializer = CitySerializer(cities,many=True)
			data1 = JSONRenderer().render(serializer.data)
			data1 = json.loads(data1)
			return JsonResponse({'data':data1},status=status.HTTP_200_OK)
		except:
			return JsonResponse({'Status':'No Data in City List'},status = status.HTTP_200_OK)
	elif request.method == 'POST':
		# import pdb; pdb.set_trace()
		# data = JSONParser().parse(request.data)
		city_obj = City.objects.create(code=request.POST.get('code'), 
				name=request.POST.get('name'),state_id=request.POST.get('state_id'))
		# serializer = CountrySerializer(data=data)
		# if serializer.is_valid():
		# 	serializer.save()
		return JsonResponse({'Status':'City Successfully Added'},status=status.HTTP_201_CREATED)
		return JsonResponse(serializer.errors,status=status.HTTP_400_BAD_REQUEST)

@csrf_exempt
def city_list_with_pk(request,pk):
	try:
		city = City.objects.get(city_id=pk)
	except City.DoesNotExist:
		return JsonResponse({'Status':'Invalid city Primary Key'},status=HTTP_400_BAD_REQUEST)

	if request.method == 'GET':
		try:
			serializer = CitySerializer(city)
			data1 = JSONRenderer().render(serializer.data)
			data1 = json.loads(data1)
			return JsonResponse({'data':data1},status=status.HTTP_200_OK)
		except:
			return JsonResponse({'Status':'No Data in city List'},status = status.HTTP_200_OK)
