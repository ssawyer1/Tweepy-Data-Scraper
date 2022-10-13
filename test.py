from asyncio.streams import FlowControlMixin
from re import M
from operator import itemgetter
import tweepy
import networkx as nx
import matplotlib.pyplot as plt
from matplotlib.patches import Rectangle
import json 
import pandas as pd
import numpy as np

# client = tweepy.Client(bearer_token='AAAAAAAAAAAAAAAAAAAAACBxgQEAAAAAyz%2FFEMlTwxWv3pFf7eqpNn%2FAfMM%3DVVRYG7FYeBCIXcQc0rozUEr8lkWfAJWLQZ7XNDVvN7FJ4G2mOV')

# G1 = nx.Graph()
# nodes = []
# def get_username(id):
#        name = client.get_user(id = id)
#        return name
# with open('anti.json', "r") as json_file:
#    data = json.load(json_file)
#    for i in data:
#        nodes.append(i)
# #***************Graph of anti users follows***************
# G1.add_edges_from(nodes)
# plt.figure(1,figsize = (12,9))
# df = pd.DataFrame(index=G.nodes(), columns=G.nodes())
# for row, data in nx.shortest_path_length(G):
#     for col, dist in data.items():
#         df.loc[row,col] = dist
# df = df.fillna(5)
# pos = nx.kamada_kawai_layout(G, dist=df.to_dict())
# anti_graph = nx.draw(G, with_labels=True, pos=pos, font_size=4, node_size=100)

# G2 = nx.Graph()
# pro_nodes = []
# with open('pro.json', "r") as json_file:
#    data = json.load(json_file)
#    for i in data:
#        pro_nodes.append(i)

# #****************Graph of who the users follow*********************
# G2.add_edges_from(pro_nodes)
# plt.figure(2,figsize=(12,9))
# df = pd.DataFrame(index=G.nodes(), columns=G.nodes())

# for row, data in nx.shortest_path_length(G):
#     for col, dist in data.items():
#         df.loc[row,col] = dist
# df = df.fillna(5)
# pos = nx.kamada_kawai_layout(G, dist=df.to_dict())
# pro_graph = nx.draw(G, with_labels=True, pos=pos, font_size=4, node_size=100)

temp = [0.00131313, 0.023442]
temp1 = [0.001, 0.02]
plt.rcParams["figure.figsize"] = [5, 5]
plt.rcParams["figure.autolayout"] = True

fig1, ax1 = plt.subplots(3, figsize=(10,8))
fig1.canvas.manager.set_window_title('Network Measures')

#Plot diameter

ax1[2].hist(temp,bins=50)
ax1[2].hist(temp1,bins=50)
ax1[2].set_title("Pro/Anti COVID Vaccine User's: Diameter of a network built from the accounts these two parties follow")
ax1[2].legend(['Anti Vaccine Diameter', 'Pro Vaccine Diameter'],loc='upper center')
ax1[2].set_autoscale_on(True)
plt.show()