
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
# - Weight: The weight lifted in pounds
# - Reps: The number of repetitions performed

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import tkinter as tk

class main:
        def __init__(self):
            # TKinter window creation
            self.root = tk.Tk()
            self.root.title("Workout Progress Analyzer")
            self.root.geometry("1920x1080")


            # Setting up main label
            self.label = tk.Label(self.root, text = "Welcome to Workout Progress Analyzer", 
                                  font=('Arial', 30))
            self.label.pack(padx=20, pady=20)

            ## Button executes display_data for BenchPress data
            self.button = tk.Button(self.root, text = "Display Data (Bench Press)", 
                                    font=('Arial', 15), width= 20, height = 10, 
                                    command= lambda: display_data("bench_press"))
            self.button.pack (padx=50, pady=20)

            ## Button executes display_data for DumbbellCurl data
            self.button2 = tk.Button(self.root, text = "Display Data (Dumbbell Curl)", 
                                     font=('Arial', 15), width= 20, height = 10, 
                                     command= lambda: display_data("dumbbell_curl"))
            self.button2.pack (padx=50, pady=20)


            # Start the GUI loop
            self.root.mainloop()

# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - 

def display_data(choice):
    # Read file of workout of choice
    if(choice == "bench_press"):
        bp_data = pd.read_csv('data/BenchPress_Progress.csv')
    elif(choice == "dumbbell_curl"):
         bp_data = pd.read_csv('data/DumbbellCurl_Progress.csv')

    
    weight = bp_data.Weight
    reps = bp_data.Reps

    volume = (weight*reps).sum()
    PR = (weight).max()

    # Averages
    print(f" Average weight:{weight.mean()} lbs")
    print(f"Average number of reps in working sets: {reps.mean()}")
    print(f"Total volume: {volume} lbs")
    print(f"Personal Record: {PR} lbs")


    # One Rep Max
    oneRepMax =  weight.mean() * (1 + 0.0333 * reps.mean())
    print(f"Your estimated 1RM based on your averages is: {oneRepMax}")

    # Calculating Estimated 1RM per workout.
    # Group the data by Date and take the mean out of that.
    averagePerWorkout = bp_data.groupby('Date').mean()

    # Create a new column using Epley's fomula using the avg weight and reps of their respective column
    averagePerWorkout['1RM'] = averagePerWorkout['Weight'] * (1 + 0.0333 * averagePerWorkout['Reps'])
    # Now we will make a plot graph of the 1RPM per workout
    # Set XY to their desired values. In this case in averagePerWorkout the Date became the index
    X = averagePerWorkout.index
    Y = averagePerWorkout['1RM']

    ## Show graph using matplotlib
    fig, ax = plt.subplots()
    ax.plot(X, Y, color = 'green')
    ax.set_title("1RM over time")
    ax.set_xlabel("Date")
    ax.set_ylabel("1RM")
    plt.show()

main()