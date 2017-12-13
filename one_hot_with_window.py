#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Dec 12 19:22:22 2017

@author: bennicholl
"""
import copy
import numpy as np
from gensim import corpora

np.set_printoptions(threshold=np.nan)

corpus = ' Meet George Beard and Harold Hutchins. George is the kid on the left with the tie and the flat-top. Harold is the one on the right with the T-shirt and the bad haircut. '
# convert to lower case
corpus = corpus.lower()

"""example of getting rid of redundant, non descriptive words"""
del_words = set('for on a is of the and to in'.split())
#
"""example list of all the individual words. dont include periods"""
words = [[i for i in corpus.split() if i != '.' if i not in del_words]]

"""list of sentences, not inculding periods"""
sentences = [i for i in corpus.split('.') ]

"""corpora dictionaries get rid of all repeat words, while keeping the list of words in order"""
"""to get dictionary for (the key/value), type 'diction.token2id'
   you can also get the values in the form of a list by simply indexing. 'diction[1]""" 
diction = corpora.Dictionary(words)


"""to run algorithm, create a one_hot() class object"""
# Ex.  a = one_hit()
"""than run the one_hot() method, and put your list of words as argument"""
# Ex.  a.one_hot(list_of_words = diction)
"""run the labels method to get one_hots repsective labels"""
# Ex.  a.labels
"""to get one_hot vectors atribute, call   a.one_hot_encoded
   to get corespnding label vectors attributes, call a.one_hot_labels"""
class one_hot():
    """list_of_words argument should be a corpora dictionary, a list, or nump array"""
   
    """create a one hot encoded matrix for our words"""
    def one_hot(self, list_of_words, window = 3):
        self.window = window
        """out information in this method will be appended to this list"""
        one_hot = []
        """create a an array with all zeros, that is 
        the len of the total amount of words in our corpus"""
        zero_vector = np.zeros(len(list_of_words))
        for e,i in enumerate(list(list_of_words)):
    
            """accounts for the window size to the left and to the right"""
            if e >= self.window and e < zero_vector.shape[0] - self.window:
                """Ex. if the window size is 5, and the len of elements to the left and right,
                   is 5 or greater, create twice as many one hots as our window size"""                  
                for ii in range(self.window * 2):
                    """add one to the respective element"""        
                    zero_vector[e] = 1        
                    one_hot.append(copy.copy(zero_vector))
                    """turn that element which was one back to zero"""
                    zero_vector[e] = 0
                    
                """this accounts for window if the window to the left is less than window size"""        
            elif e < self.window:
                left_window = abs(e % self.window)
                for ii in range(self.window + left_window):
                    """add one to the respective element""" 
                    zero_vector[e] = 1        
                    one_hot.append(copy.copy(zero_vector))
                    """turn that element which was one back to zero"""
                    zero_vector[e] = 0
                    
                """this accounts for window if the window to the right is less than window size"""  
            else:
                right_window = zero_vector.shape[0] - (e+1)
                for ii in range(right_window + self.window):
                    """add one to the respective element""" 
                    zero_vector[e] = 1        
                    one_hot.append(copy.copy(zero_vector))
                    """turn that element which was one back to zero"""
                    zero_vector[e] = 0 
        
        self.one_hot_encoded = np.array(one_hot)
        return np.array(one_hot)   
                
    def labels(self):      
        """create array of zeros with same shape as our previously created one_hot_encoded object"""
        labels_array = np.zeros(self.one_hot_encoded.shape)
        """creates an np.array list of the index of each vector where the 1 in our 
           one_hot_encoded object is located"""
        find_ones = np.where(self.one_hot_encoded == 1)[1] 
        """the i is used as an index to our find_ones object"""
        i = 0
        """the e is used for an index to our labels array, specifically which vector we add a 1 to"""
        e = 0
        while i < labels_array.shape[0]-1:
            
            """gives us the index of our 1 for our one hot encoded vector for its respective row"""
            index = find_ones[i]
            """used to make sure everytime we can move to the right in our vecotrs"""
            add = 1
            """used to make sure everytime we can move to the left in our vecotrs"""
            subtract = 1
            """this must be below window"""
            right_window_count = 0
            left_window_count = 0
            """as soon as the index holding one changes, break loop"""
            while index == find_ones[i]:
                """index is the index of the 1 in the original 1 hot vector"""
                """add is simply moving one over to the right until we reach our window size"""
                if index + add < labels_array.shape[1] and right_window_count < self.window:
                    labels_array[e][index + add] = 1
                    add += 1
                    e += 1
                    right_window_count += 1
                    """index is the index of the 1 in the original 1 hot vector"""
                    """subtract is simply moving one over to the left until we reach our window size"""    
                elif index - subtract >= 0 and left_window_count < self.window:
                    labels_array[e][index - subtract] = 1
                    e += 1
                    subtract += 1
                    left_window_count += 1
                    
                else:
                    i += 1
                    if i >= len(find_ones):
                        break
        
        self.one_hot_labels = labels_array            
        return(labels_array)    