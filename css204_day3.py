#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jan 31 09:38:18 2024

@author: C_Thesner
"""

####################################
#
#   packages
#
####################################

import matplotlib.pyplot as plt
import pandas as pd
from ydata_profiling import ProfileReport

# import plotly.express as px


####################################
#
#   Using matplotlib
#
####################################

# reaction_conv = [0.5, 0.6, 0.7, 0.7, 0.9]
# temp = [180, 200, 220, 240, 260]

# plt.plot(temp,reaction_conv)
# plt.xlabel("temp")
# plt.ylabel("reac conv")
# plt.title("chem reac")
# plt.show()

#######################################

# line graph

# fig = px.line(x=temp, y=reaction_conv)

# fig.write_html("plot.html")

##############################################

# day1_attendees = [70, 20, 64, 90, 80]
# day1_names = ["blessing", "mali", "pangi", "tafi", "shini"]

# plt.bar(day1_names,day1_attendees)
# plt.show()

###########################################

# x_scat = [1,2,3,4,5]
# y_scat = [2,4,6,8,10]

# plt.scatter(x_scat,y_scat)
# plt.show()

################################################

# x_hist = [1,2,2,2,3,3,3,3,4,6,6,6,6,6,6,6,]

# plt.hist(x_hist)
# plt.show()

##############################



"""

Pandas profiling

"""

df = pd.read_csv("day2/data_02/iris.csv")

profile = ProfileReport(df, title="Profiling Report")

profile.to_file("yout_report.html")








