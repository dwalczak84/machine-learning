# -*- coding: utf-8 -*-
"""
Created on Mon Apr 03 22:31:17 2017

@author: Dariusz
"""

# import necesarry libraries 
import os
import pandas as pd
import re
from collections import Counter

# preprocessing text function for train and test data
# be interested only in A-Za-z0-9 and $ characters
R = range(65, 91) + range(97, 123) + [36] + range(48, 58)
def preprocess_text(s): 
    if isinstance(s, str):
        s1 = ''        
        for c in s:
            if ord(c) in R:
                s1 += c
            else:
                s1 += ' '
        s1 = s1.lower()
        s1 = s1.replace('the', '')
        s1 = s1.replace('job', '')
        s1 = s1.replace('looking for', '')
        s1 = s1.replace('this', '')
        s1 = s1.replace('successfully', '')
        s1 = s1.replace('successful', '')
        s1 = s1.replace('individual', '')
        s1 = s1.replace(' a ', ' ')
        s1 = s1.replace(' an ', ' ')
        s1 = re.sub(' {2,}', ' ', s1)
        s1 = s1.replace('example com', ' ')
        s1 = s1.replace('www', ' ')
        s1 = re.sub(' {2,}', ' ', s1)
        return s1
        
# read the train data in for investigation.
# preprocess the data
# play with and inspect the data using pandas and Counter
train_path = os.getcwd() + '\\train.tsv'
df = pd.read_table(train_path)
clean_train_list = []

for i in range(len(df)):
    if not pd.isnull(df['tags'][i]):
        clean_train_list.append((df['tags'][i], df['description'][i]))
        
df2 = pd.DataFrame(clean_train_list, columns = df.columns)
for i in range(len(df2)):
    df2['description'][i] = preprocess_text(df2['description'][i])
    df2['tags'][i] = sorted(df2['tags'][i].split())

# commit varoius tests and experiments on train data and compare it with the 
# categories also obtained from the train data
A = []
for i in range(len(df2)):
    if '5-plus-years-experience-needed' in df2['tags'][i]:
        A.append(df2['description'][i])
B = [Counter(i.split()) for i in A]
C = map(lambda x: x.most_common(), B)

# detection functions for each of twelve tags based on personal experiments
# and tests with the train data
# create bag of words related mostly to each tag and maybe antibag of words
# which should be avoided based on correlation of train description -> tags
# then for each string start with an empty tag list and if nothing is found, 
# return an empty tag. otherwise add tags found by words in bags.

# Explanation on choosing the tacling method for this problem:
# =============================================================================
# This solution may be considered as quite primitive, simple and naive. 
# However results generated on a test file are satisfactory and show quite 
# high accuracy of ~ 60%.
# Therefore it is not a bad idea to further edit and develop below 
# functions and their order of execution for matching the job tags and based on
# the training data.


def detect_part_time_job(s, tags):
    bag = ('part time', 'temporary')    
    for word in bag:
        if word in s:
            tag.append('part-time-job')
            return
        
def detect_full_time_job(s, tag):
    bag = ('full time', 'permanent')        
    for word in bag:
        if word in s:
            if 'part-time-job' not in tag:
                tag.append('full-time-job')
                return

def detect_hourly_wage(s, tag):
    bag = ('hourly', 'per hour', ' hr ')
    anti_bag = ('monthly', 'hour of', 'hours')
    for word in anti_bag:
        if word in s:
            return
    for word in bag:
        if word in s:
            tag.append('hourly-wage')
            return

def detect_salary(s, tag):
    if any(re.findall('\$', s)) or 'salary' in s:
        if 'hourly-wage' not in tag:
            tag.append('salary')

def detect_bs_degree(s, tag):
    bag = ('college degree', 'bachelor s degree', 'bachelor', 'entry lev', 
    'ba degree')
    for word in bag:
        if word in s:
            tag.append('bs-degree-needed')
            return
        
def detect_ms_or_phd(s, tag):
    bag = ('phd', 'doctoral', 'doctorate', 'master s degree', 'master')
    if 'bs-degree-needed' not in tag:
        for word in bag:
            if word in s:
                tag.append('ms-or-phd-needed')
                return

def detect_licence(s, tag):
    bag = ('license', 'certification', 'certified', 'registered')
    if 'drivers license' not in s:
        for word in bag:
            if word in s:
                tag.append('licence-needed')
                return

def detect_2_4years_experience(s, tag):
    bag = ('two years', 'three years',  'four years', '2 years', '3 years', 
           '4 years', 'few years', 'no more than 3')
    for word in bag:
        if word in s:
            tag.append('2-4-years-experience-needed')
            return

def detect_1year_experience(s, tag):
    bag = ('at least year', 'at least one year', 'one year', '1 year')
    anti_bag = ('1 year long', 'one year commitment')
    for word in anti_bag:
        if word in s:
            return
    if '2-4-years-experience-needed' in tag:
        return        
    for word in bag:
        if word in s:
            tag.append('1-year-experience-needed')

def detect_5years_plus_experience(s, tag):
    bag = ('five years', '5 years', '10 years', 'seven years', '7 years', 
    '8 years', 'eight years', 'five or more', '6 years', 'six years', 
    '8 or more years', 'six plus years', 'ten years', 'fifteen years', 
    '12 years', '9 years', 'six or more', '10 or more years',
    'ten or more years', '15 years')
    for word in bag:
        if word in s:
            if '1-year-experience-needed' not in tag:        
                tag.append('5-plus-years-experience-needed')
                return

def detect_supervising_job(s, tag):
    bag = ('group leader', 'manager', 'supervisor', 'coordinate', 
           'chief executive officer') 
    anti_bag = ('multiple positions', 'manage content', 'developer')
    for word in anti_bag:
        if word in s:
            return
    for word in bag:
        if word in s:
            tag.append('supervising-job')
            return

def detect_associate_job(s, tag):
    if 'associate' in s:
        if 'supervising-job' not in tag:
            tag.append('associate-needed')        


# Read the test data
test_path = os.getcwd() + '\\test.tsv'
df_test = pd.read_table(test_path)

# Build a preprocessed test data and run through the detection functions
test_data = [preprocess_text(df_test['description'][i]) for i in range(len(df_test))]
results = []

for test in test_data:
    tag = []
    detect_part_time_job(test, tag)
    detect_full_time_job(test, tag)
    detect_hourly_wage(test, tag)
    detect_salary(test, tag)
    detect_associate_job(test, tag)
    detect_bs_degree(test, tag)
    detect_ms_or_phd(test, tag)    
    detect_licence(test, tag)
    detect_1year_experience(test, tag)
    detect_2_4years_experience(test, tag)
    detect_5years_plus_experience(test, tag)
    detect_supervising_job(test, tag)
    if not tag:
        results.append(' ')
    else:
        results.append(' '.join(tag))
                
# generate the output file tags.tsv
output_path = os.getcwd() + '\\tags.tsv'
f = open(output_path, 'w')

# insert the headers for the columns
f.write('tags'  + '\n')

# write the results for each ID
for i in range(len(results)):
    f.write(results[i]  + '\n')

# Close the file
f.close()