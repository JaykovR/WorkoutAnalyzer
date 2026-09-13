
# Written by Jaykov
# This program is solely for the purpose of my personal learning/independent study

# This program has the following simple objectives:
# - How much has my average benchpress increased over time?
# - What is my current average benchpress/working weight?
# - How many reps do I usually perform at average?
# - What is my estimated 1rm (one-rep max) based on my average benchpress and reps?

# The program will read a CSV file containing benchpress data, process the data to calculate the required metrics, and output the results.
# The CSV file is expected to have the following columns:
# - Date: The date of the benchpress session (format: YYYY-MM-DD)
#       Since I do 3 sets of benchpress per session, the date will be repeated 3 times for each session.
# - Weight: The weight lifted in pounds
# - Reps: The number of repetitions performed

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

bp_data = pd.read_csv('data/BenchPress_Progress.csv')
date = bp_data.Date
weight = bp_data.Weight
reps = bp_data.Reps

# Averages
print(f" Average weight:{weight.mean()} lbs")
print(f"Average number of reps in working sets: {reps.mean()}")

# One Rep Max
oneRepMax =  weight.mean() * (1 + 0.0333 * reps.mean())
print(f"Your estimated 1RM based on your averages is: {oneRepMax}")

# Calculating Estimated 1RM per workout.
# For this I will need to group them in their dates and use that data to calculate the 1RM's individually by taking the averages of that.

# Group the data by Date and take the mean out of that.
averagePerWorkout = bp_data.groupby('Date').mean()
# Create a new column using Epley's fomula using the avg weight and reps of their respective column
averagePerWorkout['1RM'] = averagePerWorkout['Weight'] * (1 + 0.0333 * averagePerWorkout['Reps'])
# Now we will make a plot graph of the 1RPM per workout
# Set XY to their desired values. In this case in averagePerWorkout the Date became the index
X = averagePerWorkout.index
Y = averagePerWorkout['1RM']

fig, ax = plt.subplots()
ax.plot(X, Y, color = 'green')
ax.set_title("1RM over time")
ax.set_xlabel("Date")
ax.set_ylabel("1RM")
plt.show()