# -*- coding: utf-8 -*-
"""
Created on Mon Sep 25 22:41:03 2017

@author: Shruthi
"""

def greedy_cow_transport(cows,limit=10):
    """
    Uses a greedy heuristic to determine an allocation of cows that attempts to
    minimize the number of spaceship trips needed to transport all the cows. The
    returned allocation of cows may or may not be optimal.
    The greedy heuristic should follow the following method:

    1. As long as the current trip can fit another cow, add the largest cow that will fit
        to the trip
    2. Once the trip is full, begin a new trip to transport the remaining cows

    Does not mutate the given dictionary of cows.

    Parameters:
    cows - a dictionary of name (string), weight (int) pairs
    limit - weight limit of the spaceship (an int)
    
    Returns:
    A list of lists, with each inner list containing the names of cows
    transported on a particular trip and the overall list containing all the
    trips
    """
    # TODO: Your code here
    #global count = 0
    cows_copy  = dict(cows)
    final_list = []
    #cur_list   = []
    cur_limit  = limit
    count = 10
    #ordered_list = sorted(cows, key = cows.get, reverse = True)
    #print (limit)
    while (cows_copy):
        cur_list   = []
        len_cows = len(cows_copy)
        cows_copy2 = dict(cows_copy)
        ordered_list = sorted(cows_copy, key = cows_copy.get, reverse = True)
        #print(ordered_list)
        for i in range(len_cows):
            if (cows_copy[ordered_list[i]] <= cur_limit):
                del cows_copy2[ordered_list[i]]
                cur_list.append(ordered_list[i])
                cur_limit -= cows_copy[ordered_list[i]]
        count = count - 1
        cur_limit = limit
        #print (cur_list)
        final_list.append(cur_list)
        cows_copy = dict(cows_copy2)
        #print(cows_copy)
        #print(cows_copy2)
        

