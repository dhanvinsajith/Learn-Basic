import matplotlib.pyplot as plt
import matplotlib.font_manager as fm
import pandas as pd
import numpy as np



font_thick = fm.FontProperties(fname = 'Montserrat-SemiBold.otf', size = 18)
font = fm.FontProperties(fname = 'Montserrat-Regular.otf', size = 14)
#https://jonathansoma.com/lede/data-studio/matplotlib/list-all-fonts-available-in-matplotlib-plus-samples/
font_thick_dict = {'fontname':'Verdana', 'size':'20', 'color':'black', 'weight':600,
                   'verticalalignment':'bottom'}
font_dict = {'fontname':'Verdana', 'size':'15', 'color':'black'}



#BASIC GRAPH
'''
x = [0, 1, 2, 3, 5, 6, 7, 8]
y = [0, 2, 4, 6, 10, 12, 14, 16]
plt.plot(x, y, label = '2x', color = 'red') #y = 2x line

# plt.title("Basic Line Graph", fontdict = {'fontname': 'Montserrat', 'fontsize': 18})
#OR
plt.title("Basic Line Graph", fontproperties = font_thick)

# plt.xlabel("x values", fontdict = {'fontname': 'Montserrat', 'fontsize': 12})
# plt.ylabel("y values", fontdict = {'fontname': 'Montserrat', 'fontsize': 12})
#OR
plt.xlabel("x values", fontproperties = font)
plt.ylabel("y values", fontproperties = font)

plt.xticks([0, 1, 2, 3, 4, 5])
plt.yticks([0, 2, 4, 6, 8, 10])
plt.plot([0, 1, 2, 3, 4], [0, 1, 4, 9, 16], label = 'x^2', color = '#40E0D0')
plt.legend()

plt.show()
'''



#COOLER BASIC GRAPH
'''
plt.title("Cooler Basic Graph", fontproperties = font_thick)
plt.xlabel("x values", fontproperties = font)
plt.ylabel("y values", fontproperties = font)
#plt.plot([0, 1, 2, 3, 4, 5], [0, 3, 6, 9, 12, 15], label = '3x', color = "#ED2939", linewidth = 2.5, linestyle = '--', marker = 'o', markersize = 7, markeredgecolor = '#B22222')
plt.plot([0, 1, 2, 3, 4, 5], [0, 3, 6, 9, 12, 15], '--o', color = '#ED2939', linewidth = 2.5, markeredgecolor = '#B22222', label = '3x') #shorthand notation for above commented line
plt.plot([0, 1, 2, 3, 4], [0, 1, 4, 9, 16], label = '$\mathregular{x^2}$', color = '#40E0D0', linewidth = 2.5, marker = '.', markersize = 10, markeredgecolor = 'blue')
plt.xticks([0, 1, 2, 3, 4])
plt.yticks([0, 2, 4, 6, 8, 10, 12, 14, 16])
plt.legend()

plt.show()
'''



#GRAPH WITH FORMULA
'''
x = np.arange(0, 21, 2)
# plt.figure(figsize = (2, 3), dpi = 500) #changing graph size
plt.title("Cooler Basic Graph", fontproperties = font_thick)
plt.xlabel("x values", fontproperties = font)
plt.ylabel("$\mathregular{x^2}$ values", fontproperties = font)
plt.plot(x[:7], 3*x[:7], 'r-o', linewidth = 2.5, markeredgecolor = '#B22222', label = '3x')
plt.plot(x[6:], 3*x[6:], 'r:.', linewidth = 2.5, markersize = 10, markeredgecolor = '#B22222')
plt.plot(x, x**2, '-o', color = '#40E0D0', linewidth = 2.5, markersize = 5, markeredgecolor = 'b', label = '$\mathregular{x^2}$')
plt.xticks(x)
plt.yticks(np.arange(0, 401, 50))
plt.legend()

#saving graph
plt.savefig('coolgraph.png', dpi = 300)

plt.show()
'''



#BAR GRAPHS
'''
#titles, changing size, labels, font everything is the same as normal graph
labels = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H']
values = [10, 15, 12, 11, 14, 8, 17, 15]

bars = plt.bar(labels, values)
patterns = ['/', 'o', '*', 'O', '|', '-', '+', '.', 'x']
for bar in bars:
    bar.set_hatch(patterns.pop(0))
bars[0].set_hatch('/')
bars[1].set_hatch('o')
bars[2].set_hatch('*')
bars[3].set_hatch('O')

plt.show()
'''



#GAS PRICES - LINE GRAPH
'''
gas_data = pd.read_csv('gas_prices.csv')
'''
'''
#formatted selected countries
plt.figure(figsize = (10, 6))
plt.plot(gas_data.Year, gas_data.Australia, 'b.-',label = 'Australia', linewidth = 2.5, markersize = 10)
plt.plot(gas_data.Year, gas_data.Canada, 'r.-', label = 'Canada', linewidth = 2.5, markersize = 10)
plt.plot(gas_data.Year, gas_data['South Korea'], 'g.-',label = 'South Korea', linewidth = 2.5, markersize = 10)
plt.title('Gas Prices Worldwide Over Time (in USD)', fontdict = font_thick_dict)
plt.xlabel('Years', fontdict = font_dict)
plt.ylabel('Price per Gallon', fontdict = font_dict)
plt.xticks(gas_data.Year[::3])
plt.legend()
plt.show()
'''
'''
#all countries
plt.figure(figsize = (10, 6))
for country in gas_data:
    if country != 'Year':
        plt.plot(gas_data.Year, gas_data[country], marker = '.', linewidth = 2.5, label = country)
plt.title('Gas Prices Worldwide Over Time (in USD)', fontdict = font_thick_dict)
plt.xlabel('Years', fontdict = font_dict)
plt.ylabel('Price per Gallon', fontdict = font_dict)
plt.xticks(gas_data.Year[::3])
plt.legend()
plt.savefig('gas.png', dpi = 300)
plt.show()
'''
'''
#another way to plot specific countries
plt.figure(figsize = (10, 6))
countries = ['USA', 'Canada', 'Japan', 'France']
for country in gas_data:
    if country in countries:
        plt.plot(gas_data.Year, gas_data[country], marker = '.', linewidth = 2.5, label = country)
plt.title('Gas Prices Worldwide Over Time (in USD)', fontdict = font_thick_dict)
plt.xlabel('Years', fontdict = font_dict)
plt.ylabel('Price per Gallon', fontdict = font_dict)
plt.xticks(gas_data.Year[::3])
plt.legend()
plt.show()
'''



#FIFA DATA - HISTOGRAM
'''
fifa_data = pd.read_csv('fifa_data.csv')

bins = [40, 50, 60, 70, 80, 90, 100]
plt.figure(figsize = (8, 8))
plt.hist(fifa_data.Overall, bins = bins, color = '#40e0d0')
plt.title('Distribution of Overall Score of Fifa Players', fontdict = font_thick_dict)
plt.xlabel('Overall Score', fontdict = font_dict)
plt.ylabel('Frequency', fontdict = font_dict)
plt.xticks(bins)
plt.show()
'''



#FIFA DATA - PIE CHART
'''
fifa_data = pd.read_csv('fifa_data.csv')

left = fifa_data.loc[fifa_data['Preferred Foot'] == 'Left'].count()[0]
right = fifa_data.loc[fifa_data['Preferred Foot'] == 'Right'].count()[0]
print(left, right)

plt.pie([left, right], labels = ['Left', 'Right'], colors = ['#00BFFF', '#00FF7F'], autopct = '%.2f%%')
plt.title('Foot Preference')
plt.show()
'''


#FIFA DATA - COMPLEX PIE CHART
'''
fifa_data = pd.read_csv('fifa_data.csv')

#collecting data
fifa_data.Weight = [int(x.strip('lbs')) if type(x) == str else x for x in fifa_data.Weight]
light = fifa_data.loc[fifa_data.Weight < 125].count()[0]
light_medium = fifa_data.loc[(fifa_data.Weight >= 125) & (fifa_data.Weight < 150)].count()[0]
medium = fifa_data.loc[(fifa_data.Weight >= 150) & (fifa_data.Weight < 175)].count()[0]
heavy_medium = fifa_data.loc[(fifa_data.Weight >= 175) & (fifa_data.Weight < 200)].count()[0]
heavy = fifa_data.loc[fifa_data.Weight >= 200].count()[0]

#formatting data
weights = [light, light_medium, medium, heavy_medium, heavy]
labels = ['<125', '125-150', '150-175', '175-200', '>200']
# colors = ['#D5F3FE', '#3C99DC', '#66D3FA', '#2565AE', '#0F5298'] #OR you can use mpl styles https://matplotlib.org/3.1.0/gallery/style_sheets/style_sheets_reference.html
explode = (0.4, 0.2, 0, 0, 0.4)

plt.style.use('fivethirtyeight')
plt.figure(figsize = (10, 8))
plt.pie(weights, labels = labels, autopct = '%.2f%%', pctdistance = 0.8, explode = explode) #colors = colors
plt.title('Weight Distribution of Fifa Players', fontdict = font_thick_dict)
plt.show()
'''



#FIFA DATA - BOX AND WHISKERS CHART
'''
fifa_data = pd.read_csv('fifa_data.csv')

barcelona = fifa_data.loc[fifa_data.Club == 'FC Barcelona']['Overall']
madrid = fifa_data.loc[fifa_data.Club == 'Real Madrid']['Overall']
revs = fifa_data.loc[fifa_data.Club == 'New England Revolution']['Overall']

teams = [barcelona, madrid, revs]
labels = ['FC Barcelona', 'Real Madrid', 'New England Revolution']

plt.figure(figsize = (7, 8))
plt.style.use('default')
boxes = plt.boxplot(teams, labels = labels, patch_artist = True, medianprops = {'linewidth': 2.5, 'color': '#00aa8b'}, whiskerprops = {'linewidth': 2.5, 'color': '#00008b'}, capprops = {'linewidth': 2.5, 'color': '#00008b'}) #patch_artist allows using face color
plt.title('Professional Football Clubs Comparison', fontdict = font_thick_dict)
plt.xlabel('Teams', fontdict = font_dict)
plt.ylabel('Overall Score', fontdict = font_dict)

#styling
for box in boxes['boxes']:
    box.set(color = '#6A5ACD', linewidth = 2.5) #edge style
    box.set(facecolor = '#bbeeff') #inside fill color

plt.show()
'''