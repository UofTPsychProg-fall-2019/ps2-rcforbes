#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
scene-cat problem set for PSY 1210 - Fall 2018

@author: Michael Mack
"""

#%% import block 
import numpy as np
import scipy as sp
import scipy.stats
import os
import shutil


#%%
# copy files from testing room folders to raw data, rename files to include
# testing room letter in the filename
#
os.getcwd() # Check current directory
cwd = os.getcwd() # Set current directory path to cwd

testingrooms = ['A','B','C']
for room in testingrooms:
    shutil.copy(cwd + '/testingroom' + room + '/experiment_data.csv', cwd  + '/rawdata/experiment_data_' + room + '.csv') # Copies testing room files to rawdata folder and renames files
...



#%%
# read in all the data files in rawdata directory using a for loop
# columns: subject, stimulus, pairing, accuracy, median RT
#

cwd_raw = os.getcwd() + '/rawdata' # Change current wd to include /rawdata path
data = np.empty((0,5))
for room in testingrooms:
    tmp = sp.loadtxt(cwd_raw + '/experiment_data_'+room+'.csv', delimiter = ',') # load data to temp object
    data = np.vstack([data, tmp]) # stack testingroom data to form a single array
...


#%%
# calculate overall average accuracy and average median RT
#
acc_avg = np.mean(data[:,3])   # 91.48% accuracy column is [:, 3] index
mrt_avg = np.mean(data[:,4])   # 477.3ms median rt column is [:,4] index


#%%
# calculate averages (accuracy & RT) split by stimulus using a for loop and an 
# if statement. (i.e., loop through the data to make a sum for each condition, 
# then divide by the number of data points going into the sum)
#

sumnums1 = 0
sumnums2 = 0
points1 = 0
points2 = 0
index = 0
stim = data[:,1]
acc = data[:,3]
mrt = data[:,4]

for i in np.nditer(stim):
    print(i)
    if i == 1:
        sumnums1 = sumnums1 + acc[index]
        points1 = points1 + 1
    elif i == 2:
        sumnums2 = sumnums2 + acc[index]
        points2 = points2 +  1
    index = index + 1

acc_avg1 = sumnums1 % points1
acc_avg2 = sumnums2 % points2


...

# words: 88.6%, 489.4ms   faces: 94.4%, 465.3ms


#%%
# calculate averages (accuracy & RT) split by congruency using indexing, 
# slicing, and numpy's mean function 
# wp - white/pleasant, bp - black/pleasant
# (hint: only one line of code is needed per average)
#
acc_wp = np.mean((data[data[:,2]==1])[:,3])  # 94.0%
acc_bp = np.mean((data[data[:,2]==2])[:,3])  # 88.9%
mrt_wp = np.mean((data[data[:,2]==1])[:,4])  # 469.6ms
mrt_bp = np.mean((data[data[:,2]==2])[:,4])  # 485.1ms


#%% 
# calculate average median RT for each of the four conditions
# use for loops, indexing/slicing, or both!
# (hint: might be easier to slice data into separate words and faces datasets)
#
words_data = data[data[:,1] == 1]
faces_data = data[data[:,1] == 2]

mrt_wp_words = np.mean((words_data[words_data[:,2]==1])[:,4])  # 478.4ms
mrt_bp_words = np.mean((words_data[words_data[:,2]==2])[:,4])  # 500.3ms
mrt_wp_faces = np.mean((faces_data[faces_data[:,2]==1])[:,4])  # 460.8ms
mrt_bp_faces = np.mean((faces_data[faces_data[:,2]==2])[:,4])  # 469.9ms
...

#%%        
# compare pairing conditions' effect on RT within stimulus using scipy's 
# paired-sample t-test: scipy.stats.ttest_rel()
#
import scipy.stats

mrt_wp_words_array = (words_data[words_data[:,2]==1])[:,4]
mrt_bp_words_array = (words_data[words_data[:,2]==2])[:,4]
mrt_wp_faces_array = (faces_data[faces_data[:,2]==1])[:,4]
mrt_bp_faces_array = (faces_data[faces_data[:,2]==2])[:,4]

words_test = scipy.stats.ttest_rel(mrt_wp_words_array, mrt_bp_words_array) # words: t=-5.36, p=2.19e-5
faces_test = scipy.stats.ttest_rel(mrt_wp_faces_array, mrt_bp_faces_array) # faces: t=-2.84, p=0.0096
...


#%%
# print out averages and t-test results
# (hint: use the ''.format() method to create formatted strings)
#
print('\nOVERALL: {:.2f}%, {:.1f} ms'.format(100*acc_avg,mrt_avg))

# Words
print('\nWP words average: {}')
...