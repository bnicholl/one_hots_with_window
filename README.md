# one_hots_with_window
creates one hot vectors with corresponding labels based on window size
This algorithm is espicailly useful for setting up a skip gram word2vector neural network, but can be used for other one hot binary classifcaiton tasks where they may be more than one output as well. 

Example of what algorithm does:
Here we have 5 words in a sentence that we put in a dictionry where the keys are the words and the values are the integers assigned to their respective words:
dict = {'Joe's.': 0, 'haircut.': 1, 'resembles.': 2, 'pubic': 3, 'hair': 4}

Our goal here is to find associations with words that are close together. For instance, if we set this algorithm up with a window size of three, and our target word is Joe's, than our context words (the words that are going to be close to joe, in this case, 3 words to the left and right) will be 'haircut', 'resembles', 'pubic'. Since there are no words to the left of joe, we only get three words to the right. The descriptions and arrays below will give more insight. 

When we run the first method with a window size of 3, we get our one hot encoded vecotrs. For eample, the first three vectors are for the word 'Joe's', the next 4 vectors are for the word 'haircut', etc. The array below the one you are seeing are for the repsecive labels, and may give more insight as to why each word has a different number of vecotrs in the array

      [[ 1.,  0.,  0.,  0.,  0.],
       [ 1.,  0.,  0.,  0.,  0.],
       [ 1.,  0.,  0.,  0.,  0.],
       [ 0.,  1.,  0.,  0.,  0.],
       [ 0.,  1.,  0.,  0.,  0.],
       [ 0.,  1.,  0.,  0.,  0.],
       [ 0.,  1.,  0.,  0.,  0.],
       [ 0.,  0.,  1.,  0.,  0.],
       [ 0.,  0.,  1.,  0.,  0.],
       [ 0.,  0.,  1.,  0.,  0.],
       [ 0.,  0.,  1.,  0.,  0.],
       [ 0.,  0.,  1.,  0.,  0.],
       [ 0.,  0.,  0.,  1.,  0.],
       [ 0.,  0.,  0.,  1.,  0.],
       [ 0.,  0.,  0.,  1.,  0.],
       [ 0.,  0.,  0.,  1.,  0.],
       [ 0.,  0.,  0.,  0.,  1.],
       [ 0.,  0.,  0.,  0.,  1.],
       [ 0.,  0.,  0.,  0.,  1.]]
       
Since our window for this example is three, you can see that for our first three vectors below, those are the coresponding label vectors for our first three vectors above which are associated with Joe's.  The next four vectors below are our coresponding label vectors for the four one hot encoded vectors above, and so on.  
       
       [ 0.,  1.,  0.,  0.,  0.],
       [ 0.,  0.,  1.,  0.,  0.],
       [ 0.,  0.,  0.,  1.,  0.],
       [ 0.,  0.,  1.,  0.,  0.],
       [ 0.,  0.,  0.,  1.,  0.],
       [ 0.,  0.,  0.,  0.,  1.],
       [ 1.,  0.,  0.,  0.,  0.],
       [ 0.,  0.,  0.,  1.,  0.],
       [ 0.,  0.,  0.,  0.,  1.],
       [ 0.,  1.,  0.,  0.,  0.],
       [ 1.,  0.,  0.,  0.,  0.],
       [ 0.,  0.,  0.,  0.,  1.],
       [ 0.,  0.,  1.,  0.,  0.],
       [ 0.,  1.,  0.,  0.,  0.],
       [ 1.,  0.,  0.,  0.,  0.],
       [ 0.,  0.,  0.,  1.,  0.],
       [ 0.,  0.,  1.,  0.,  0.],
       [ 0.,  1.,  0.,  0.,  0.],
       [ 0.,  0.,  0.,  0.,  0.]
