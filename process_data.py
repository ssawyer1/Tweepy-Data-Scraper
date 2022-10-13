#*************************Reference****************
#The following are required packages and software I used to run this code:
#tweepy             4.10.1
#networkx           2.8.6
from asyncio.streams import FlowControlMixin
from re import M
from operator import itemgetter
import tweepy
import networkx as nx
import matplotlib.pyplot as plt
import json 
import pandas as pd

#*********************PLEASE READ THIS*****************************
#Note: My networks both have around 1000 nodes in them. When executing this code it will take some time for the 
#      graphs to pop up, so please be patient I assure you that the code is executing as intended.

#*****************ACCOUNTS ANTI COVID USERS FOLLOW***********************

G1 = nx.Graph()
anti_nodes = []
with open('anti.json', "r") as json_file:
   data = json.load(json_file)
   for i in data:
       anti_nodes.append(i)
#Graphs the users in nice clusters
G1.add_edges_from(anti_nodes)
anti_fig = plt.figure(1,figsize = (12,9))
anti_fig.canvas.manager.set_window_title('Network of Accounts Anti-Covid Users Follow')
df = pd.DataFrame(index=G1.nodes(), columns=G1.nodes())
for row, data in nx.shortest_path_length(G1):
    for col, dist in data.items():
        df.loc[row,col] = dist
df = df.fillna(5)
pos = nx.kamada_kawai_layout(G1, dist=df.to_dict())
anti_graph = nx.draw(G1, with_labels=True, pos=pos, font_size=4, node_size=100)

#******************Anti Degree Centrality************************

anti_degree_dict = dict(G1.degree(G1.nodes()))
nx.set_node_attributes(G1, anti_degree_dict, 'degree')
anti_sorted_degree = sorted(anti_degree_dict.items(), key=itemgetter(1), reverse=True)
#Plot this
anti_degrees = []
length_d = len(anti_sorted_degree)
for i in range(length_d):
    anti_degrees.append(anti_sorted_degree[i][1])

#*****************Anti Vaccine Diameter***************************

anti_components = nx.connected_components(G1)
anti_largest_component = max(anti_components, key=len)
# Create a "subgraph" of just the largest component
# Then calculate the diameter of the subgraph, just like you did with density.
anti_subgraph = G1.subgraph(anti_largest_component)
anti_diameter = nx.diameter(anti_subgraph)

#*********************Third Network Measure***************

anti_density = nx.density(G1)

#************************ACCOUNTS PRO COVID USERS FOLLOW*************************

G2 = nx.Graph()
pro_nodes = []
with open('pro.json', "r") as json_file:
   data = json.load(json_file)
   for i in data:
       pro_nodes.append(i)
#Graphs the users in nice clusters
G2.add_edges_from(pro_nodes)
pro_fig = plt.figure(2,figsize = (12,9))
pro_fig.canvas.manager.set_window_title('Network of Accounts Pro-Covid Users Follow')
df = pd.DataFrame(index=G2.nodes(), columns=G2.nodes())

for row, data in nx.shortest_path_length(G2):
    for col, dist in data.items():
        df.loc[row,col] = dist
df = df.fillna(5)
pos = nx.kamada_kawai_layout(G2, dist=df.to_dict())
pro_graph = nx.draw(G2, with_labels=True, pos=pos, font_size=4, node_size=100)

#***************Pro Degree Centrality*****************

pro_degree_dict = dict(G2.degree(G2.nodes()))
nx.set_node_attributes(G2, pro_degree_dict, 'degree')
pro_sorted_degree = sorted(pro_degree_dict.items(), key=itemgetter(1), reverse=True)
#Plot this
pro_degrees = []
length_d = len(pro_sorted_degree)
for i in range(length_d):
    pro_degrees.append(pro_sorted_degree[i][1])

#*******************Pro Network Diameter***********************************

pro_components = nx.connected_components(G2)
pro_largest_component = max(pro_components, key=len)
# Create a "subgraph" of just the largest component
# Then calculate the diameter of the subgraph, just like you did with density.
pro_subgraph = G2.subgraph(pro_largest_component)
pro_diameter = nx.diameter(pro_subgraph)

#********************Pro Network Density**************

pro_density = nx.density(G2) 

#****************PLOT FORMATTING*******************
#create a 3x3 matrix on which you can put graph elementsplt.rcParams["figure.figsize"] = [5, 5]
plt.rcParams["figure.figsize"] = [5, 5]
plt.rcParams["figure.autolayout"] = True
fig1, ax1 = plt.subplots(3, figsize=(10,8))
fig1.canvas.manager.set_window_title('Network Measures')
#Plot Network Degree Centrality
ax1[0].hist(anti_degrees)
ax1[0].hist(pro_degrees)
ax1[0].set_title("Pro/Anti COVID Vaccine User's: Degree Centrality")
ax1[0].legend(['Anti Vaccine Degree Centrality', 'Pro Vaccine Degree Centrality'], loc='upper center')
ax1[0].set_autoscale_on(True)
ax1[0].set(yscale='log',xlabel='Degrees', ylabel='Frequency')

#Plot Network Diameter
ax1[1].hist(anti_diameter)
ax1[1].hist(pro_diameter)
ax1[1].set_title("Pro/Anti COVID Vaccine User's: Diameter")
ax1[1].legend(['Anti Vaccine Diameter', 'Pro Vaccine Diameter'], loc='upper center')
ax1[1].set_autoscale_on(True)
ax1[1].set(xlabel='Diameter', ylabel='Frequency')

#Plot Network Density 
ax1[2].hist(anti_density, bins=20)
ax1[2].hist(pro_density, bins=20)
ax1[2].set_title("Pro/Anti COVID Vaccine User's: Density")
ax1[2].legend(['Anti Vaccine Density', 'Pro Vaccine Density'], loc='upper right')
ax1[2].set_autoscale_on(True)
ax1[2].set(xlabel='Density', ylabel='Frequency')

plt.show()