Here the objective is to classify and organize the hurricane data below in some dictionary. The main objective here is to practice the operation related with dictionary

# names of hurricanes
names = ['Cuba I', 'San Felipe II Okeechobee', 'Bahamas', 'Cuba II', 'CubaBrownsville', 'Tampico', 'Labor Day', 'New England', 'Carol', 'Janet', 'Carla', 'Hattie', 'Beulah', 'Camille', 'Edith', 'Anita', 'David', 'Allen', 'Gilbert', 'Hugo', 'Andrew', 'Mitch', 'Isabel', 'Ivan', 'Emily', 'Katrina', 'Rita', 'Wilma', 'Dean', 'Felix', 'Matthew', 'Irma', 'Maria', 'Michael']

# months of hurricanes
months = ['October', 'September', 'September', 'November', 'August', 'September', 'September', 'September', 'September', 'September', 'September', 'October', 'September', 'August', 'September', 'September', 'August', 'August', 'September', 'September', 'August', 'October', 'September', 'September', 'July', 'August', 'September', 'October', 'August', 'September', 'October', 'September', 'September', 'October']

# years of hurricanes
years = [1924, 1928, 1932, 1932, 1933, 1933, 1935, 1938, 1953, 1955, 1961, 1961, 1967, 1969, 1971, 1977, 1979, 1980, 1988, 1989, 1992, 1998, 2003, 2004, 2005, 2005, 2005, 2005, 2007, 2007, 2016, 2017, 2017, 2018]

# maximum sustained winds (mph) of hurricanes
max_sustained_winds = [165, 160, 160, 175, 160, 160, 185, 160, 160, 175, 175, 160, 160, 175, 160, 175, 175, 190, 185, 160, 175, 180, 165, 165, 160, 175, 180, 185, 175, 175, 165, 180, 175, 160]

# areas affected by each hurricane
areas_affected = [['Central America', 'Mexico', 'Cuba', 'Florida', 'The Bahamas'], ['Lesser Antilles', 'The Bahamas', 'United States East Coast', 'Atlantic Canada'], ['The Bahamas', 'Northeastern United States'], ['Lesser Antilles', 'Jamaica', 'Cayman Islands', 'Cuba', 'The Bahamas', 'Bermuda'], ['The Bahamas', 'Cuba', 'Florida', 'Texas', 'Tamaulipas'], ['Jamaica', 'Yucatn Peninsula'], ['The Bahamas', 'Florida', 'Georgia', 'The Carolinas', 'Virginia'], ['Southeastern United States', 'Northeastern United States', 'Southwestern Quebec'], ['Bermuda', 'New England', 'Atlantic Canada'], ['Lesser Antilles', 'Central America'], ['Texas', 'Louisiana', 'Midwestern United States'], ['Central America'], ['The Caribbean', 'Mexico', 'Texas'], ['Cuba', 'United States Gulf Coast'], ['The Caribbean', 'Central America', 'Mexico', 'United States Gulf Coast'], ['Mexico'], ['The Caribbean', 'United States East coast'], ['The Caribbean', 'Yucatn Peninsula', 'Mexico', 'South Texas'], ['Jamaica', 'Venezuela', 'Central America', 'Hispaniola', 'Mexico'], ['The Caribbean', 'United States East Coast'], ['The Bahamas', 'Florida', 'United States Gulf Coast'], ['Central America', 'Yucatn Peninsula', 'South Florida'], ['Greater Antilles', 'Bahamas', 'Eastern United States', 'Ontario'], ['The Caribbean', 'Venezuela', 'United States Gulf Coast'], ['Windward Islands', 'Jamaica', 'Mexico', 'Texas'], ['Bahamas', 'United States Gulf Coast'], ['Cuba', 'United States Gulf Coast'], ['Greater Antilles', 'Central America', 'Florida'], ['The Caribbean', 'Central America'], ['Nicaragua', 'Honduras'], ['Antilles', 'Venezuela', 'Colombia', 'United States East Coast', 'Atlantic Canada'], ['Cape Verde', 'The Caribbean', 'British Virgin Islands', 'U.S. Virgin Islands', 'Cuba', 'Florida'], ['Lesser Antilles', 'Virgin Islands', 'Puerto Rico', 'Dominican Republic', 'Turks and Caicos Islands'], ['Central America', 'United States Gulf Coast (especially Florida Panhandle)']]

# damages (USD($)) of hurricanes
damages = ['Damages not recorded', '100M', 'Damages not recorded', '40M', '27.9M', '5M', 'Damages not recorded', '306M', '2M', '65.8M', '326M', '60.3M', '208M', '1.42B', '25.4M', 'Damages not recorded', '1.54B', '1.24B', '7.1B', '10B', '26.5B', '6.2B', '5.37B', '23.3B', '1.01B', '125B', '12B', '29.4B', '1.76B', '720M', '15.1B', '64.8B', '91.6B', '25.1B']

# deaths for each hurricane
deaths = [90,4000,16,3103,179,184,408,682,5,1023,43,319,688,259,37,11,2068,269,318,107,65,19325,51,124,17,1836,125,87,45,133,603,138,3057,74]

# write your update damages function here:
def update_damages(data_damages):
  update_damage = []
  Billion = 1000000000;
  Million = 1000000;
  for damage in data_damages:
    if damage == 'Damages not recorded':
      update_damage.append(damage)
    elif damage[-1] == "M":
      Million_damage = Million * float(damage[:-1])
      update_damage.append(Million_damage)
    elif damage[-1] == "B":
      Billion_damage = Billion * float(damage[:-1])
      update_damage.append(Billion_damage)
  return update_damage

updated_damages = update_damages(damages)
#print(updated_damages)


    
# write your construct hurricane dictionary function here:

def hurricane_dictionaries(name_hurricane):
  name_hurricane_dictionary ={}
  for i in range(len(names)):
    name_hurricane_dictionary[names[i]] = {'Name' : names[i], 'Month' : months[i], 'Year' : years[i], 'Max Sustained Wind' : max_sustained_winds[i], 'Areas Affected': areas_affected[i],'Damage': update_damages(damages)[i], 'Deaths' : deaths[i]}
  return name_hurricane_dictionary

hurricanes = hurricane_dictionaries(names)
#print(hurricanes)

# write your construct hurricane by year dictionary function here:
def year_hurricane_dictionaries(year):
	dictionary = {}
	year_hurr = []
	dictio ={}
	for i in range(len(names)):
		dictionary[names[i]] = {'Name' : names[i], 'Month' : months[i], 'Year' : years[i], 'Max Sustained Wind' : max_sustained_winds[i], 'Areas Affected': areas_affected[i],'Damage': update_damages(damages)[i], 'Deaths' : deaths[i]}
	for datas in dictionary.values():
		#print(datas)
		for data in datas.values():
			#print(data)
			if data == year:
				#print(datas)
				year_hurr.append(datas)
				dictio[year] = year_hurr	
				#print(year_hurr)
	return dictio

year_hurricane = year_hurricane_dictionaries(1932)
#print(year_hurricane)



# write your count affected areas function here:
def hurricane_area(areas_affect):
	count = 0
	area_d = []
	areas_dictio = {}
	for areas in areas_affected:
		for area in areas:
			#print(area)
			area_d.append(area)
			if area == areas_affect:
				count += 1
				areas_dictio[areas_affect] = count

		
	return areas_dictio
area_affected = hurricane_area('The Bahamas') 
#print(area_affected)



# write your greatest number of deaths function here:
def hurricane_death(dictio):
	max_deaths = 0
	for i in range(len(names)):
		cyclone_deaths = dictio[names[i]]['Deaths']
		#print(cyclone_deaths)
		if cyclone_deaths > max_deaths:
			max_deaths = cyclone_deaths
			cyclone_name = dictio[names[i]]['Name']
	#for data in cyclone[name]:
	#	pass
		#print(data)
	return max_deaths, cyclone_name  

death_hurricane =  hurricane_death(hurricanes)
#print(death_hurricane)



# write your catgeorize by mortality function here:
def hurricane_mortality(dictio):

	hurricanes_by_mortality = {0:[],1:[],2:[],3:[],4:[],5:[]}

	for i in range(len(names)):
		cyclone_deaths = dictio[names[i]]['Deaths']
		if cyclone_deaths > 0 and cyclone_deaths < 100:
			hurricanes_by_mortality[1].append(cyclone_deaths)
		elif cyclone_deaths >= 100 and cyclone_deaths < 500:
			hurricanes_by_mortality[2].append(cyclone_deaths)
		elif cyclone_deaths >= 500 and cyclone_deaths < 1000:
			hurricanes_by_mortality[3].append(cyclone_deaths)
		elif cyclone_deaths >= 1000 and cyclone_deaths < 10000:
			hurricanes_by_mortality[4].append(cyclone_deaths)
		else: 
			hurricanes_by_mortality[5].append(cyclone_deaths)
	
	return hurricanes_by_mortality

mortality_hurricane =  hurricane_mortality(hurricanes)
#print(mortality_hurricane)



# write your greatest damage function here:
def hurricane_damage(dictio):
	max_damages = 0
	for i in range(len(names)):
		cyclone_damages = dictio[names[i]]['Damage']
		
		if cyclone_damages == "Damages not recorded":
			cyclone_damages = 0

		if cyclone_damages > max_damages:
			max_damages = cyclone_damages
			cyclone_name = dictio[names[i]]['Name']
	return max_damages, cyclone_name  
damages_hurricane = hurricane_damage(hurricanes)
print(damages_hurricane)



# write your catgeorize by damage function here:
def hurricane_by_damages(dictio):

	hurricanes_by_damage = {0:[],1:[],2:[],3:[],4:[],5:[]}

	for i in range(len(names)):
		cyclone_damages = dictio[names[i]]['Damage']
		if cyclone_damages == "Damages not recorded":
			cyclone_damages = 0
		if cyclone_damages > 0 and cyclone_damages < 100000000:
			hurricanes_by_damage[1].append(cyclone_damages)
		elif cyclone_damages >= 100000000 and cyclone_damages < 1000000000:
			hurricanes_by_damage[2].append(cyclone_damages)
		elif cyclone_damages >= 1000000000 and cyclone_damages < 10000000000:
			hurricanes_by_damage[3].append(cyclone_damages)
		elif cyclone_damages >= 10000000000 and cyclone_damages < 50000000000:
			hurricanes_by_damage[4].append(cyclone_damages)
		else: 
			hurricanes_by_damage[5].append(cyclone_damages)
	
	return hurricanes_by_damage

rating_damage_hurricane =  hurricane_by_damages(hurricanes)
print(rating_damage_hurricane)





