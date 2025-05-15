import matplotlib.pyplot as plt
import pandas as pd


#task 1
car_data = pd.read_csv('car_info.csv') #reads car data into dataframe object 
print(f'1. Shape of the dataframe: {car_data.shape}\n')

#task 2
v6engines = car_data[car_data['cylinders'] == 6] #create subset of cars with v6 engines
japanese_engines = v6engines[v6engines['origin'] == 'japan'] #create subset of v6 cars that are from Japan

jp_engine_list = []
for i in japanese_engines.name:
    jp_engine_list.append(i) #append name of v6 cars from japan

print(f'2. Japanese v6 cars: {jp_engine_list}\n')

#task 3
filler = car_data.fillna({'horsepower': 'null'}) #fill missing horse power data with 'null'
missing_hp = filler[filler['horsepower'] == 'null'] #extract data with 'null' value
missing_hp_list = []
for i in missing_hp.name: 
    missing_hp_list.append(i) #append name of cars with missing horsepower data

print(f'3. Cars with missing horsepower data: {missing_hp_list}\n')

#task 4
mpg = car_data[car_data['mpg'] >= 20] #subset cars with mpg greater or equal to 20
mpg_list = []

for i in mpg.name:
    mpg_list.append(i) #append cars to list 

tot_mpg = len(mpg_list) #find length of list

print(f'4. Number of cars having mpg greater than 20: {tot_mpg}\n')

#task 5

max_mpg = car_data['mpg'].max() #find highest mpg value
max_mpg_name = car_data[car_data['mpg'] == max_mpg] #locate associated car with highest mpg
result = max_mpg_name['name'].tolist() #retrieve name of car    

print(f'5. Most fuel efficient car: {result}\n')

#task 6
max_weight = car_data['weight'].max()  #find max, min, and average weight
min_weight = car_data['weight'].min()
mean_weight = car_data['weight'].mean()

print(f'6. Minimum weight: {min_weight} | Maximum weight: {max_weight} | Average weight: {mean_weight:.2f}\n')

#task 7
dropped_rows = car_data.dropna(axis = 0) #drop rows with missing values

print(f'7. Shape after removing the missing values: {dropped_rows.shape}')

#task 8
countrys = car_data['origin'].tolist() #turns 'origin' column of dataframe into a list
country_freq = {} #dict for storing country frequencey
for c in countrys:
    if c in country_freq:
        country_freq[c] += 1
    else:
        country_freq[c] = 1

country_names = [] #labels for pie chart
freq = [] #car manufactoring proportion by country 
for country, frequency in country_freq.items(): #iterate through dictionary, appending country names(keys) and associated freuqncies(values) to lists
    country_names.append(f'{country.capitalize()} : {((frequency / len(countrys)) * 100):.0f}%')
    freq.append(frequency)

plt.pie(freq, labels = country_names, colors = ['#c0e6f5', '#065535', '#bccf2b'], explode = (0.07,0.07,0.07),radius = 0.9 ,textprops={'fontsize': 13} )
plt.legend(country_names, loc = 'best')
plt.title('Car Manufacturing Distribution', fontname='Courier New', fontsize = 17, fontweight="bold" )
plt.show()

#task 9
mpg_points = car_data['mpg'].tolist() #turns 'mpg', 'weight', and 'displacement' columns into lists
weight_points = car_data['weight'].tolist()
displacement_points = car_data['displacement'].tolist()


plt.subplot(2,1,1) #subplot created with 2 rows, 1 colomns, and the first graphs index of 1
plt.scatter(mpg_points,weight_points, label = 'Data', s = 1, c = '#510e2c') #scatter plot created using mpg and weight data
plt.xlabel('Miles per Gallon')
plt.ylabel('Weight (lbs)')
plt.legend(fontsize = 7,  markerscale=2.0)
plt.title("Weight's Effect on Mpg", fontname='Courier New', fontsize = 15, fontweight="bold")

plt.subplot(2,1,2)
plt.scatter(mpg_points,displacement_points, label = 'Data', marker = 'o', s= 1, c = '#334894') #scatter plot created using mpg and displacement data
plt.xlabel('Miles per Gallon')
plt.ylabel("Displacement (in³)")
plt.legend(fontsize = 7,  markerscale=2.0)
plt.title("Displacement's Effect on Mpg", fontname='Courier New', fontsize = 15, fontweight="bold")

plt.tight_layout(rect=[0, 0, 0.85, 1]) #cleaner layout for subplot, fights against overlapping graphs or text
plt.show()






