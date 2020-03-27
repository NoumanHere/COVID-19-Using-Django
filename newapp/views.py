from django.shortcuts import render
import requests
# Create your views here.

def countries(request):
    response_worldwide = requests.get('https://covid19.mathdro.id/api')
    data_worldwide = response_worldwide.json()
    confirmed_worldwide = data_worldwide['confirmed']
    recovered_worldwide = data_worldwide['recovered']
    deaths_worldwide = data_worldwide['deaths']
    country_name = {}
    if 'country' in request.GET:
        country_name = request.GET['country']
        country_name = country_name.title()
        print(country_name)
        url1 = 'https://covid19.mathdro.id/api/countries'
        response1 = requests.get(url1)
        data1 = response1.json()
        countries_name = data1['countries']
        for i in countries_name:
            try:
                if (country_name.title() == i['name']) or (country_name.upper() != i['iso2']) or (country_name.upper() != i['iso3']):
                    url2 = 'https://covid19.mathdro.id/api/countries/%s' % country_name
                    response2 = requests.get(url2)
                    data2 = response2.json()
                    confirmed = data2['confirmed']
                    recovered = data2['recovered']
                    deaths = data2['deaths']

                    return render(request,'Results.html',
                    {
                    'country':country_name,
                    'data':data2,
                    'confirmed_value':confirmed['value'],
                    'recovered_value':recovered['value'],
                    'last_update':data2['lastUpdate'],
                    'death_value':deaths['value'],
                    'confirmed_value_worldwide':confirmed_worldwide['value'],
                    'recovered_value_worldwide':recovered_worldwide['value'],
                    'last_update_worldwide':data_worldwide['lastUpdate'],
                    'death_value_worldwide':deaths_worldwide['value']
                        }
                        )
                
                else:
                    country_name.title()
                    return render(request,'Results.html',
                    {
                    'confirmed_value_worldwide':confirmed_worldwide['value'],
                    'recovered_value_worldwide':recovered_worldwide['value'],
                    'last_update_worldwide':data_worldwide['lastUpdate'],
                    'death_value_worldwide':deaths_worldwide['value']
                        }
                        )
            except:
                return render(request,'Results.html',
                    {
                    
                    'confirmed_value_worldwide':confirmed_worldwide['value'],
                    'recovered_value_worldwide':recovered_worldwide['value'],
                    'last_update_worldwide':data_worldwide['lastUpdate'],
                    'death_value_worldwide':deaths_worldwide['value']
                        }
                        )
        
    return render(request,'corona.html',{
            })
