# Code from: https://github.com/omarshammas/pyPoker-Texas-HoldEm/blob/master/holdem.py

# Function takes the hand as an argument and returns a number representing the type of hand (Straight, Flush, etc.)
def score(hand):
        
    score = 0
    kicker = []
        
    #------------------------------------------------
    #-------------Checking for Pairs-----------------
    #------------------------------------------------
    pairs = {}
    prev = 0
    
    #Keeps track of all the pairs in a dictionary where the key is the pair's card value
    #and the value is the number occurrences. Eg. If there are 3 Kings -> {"13":3} 
    for card in hand:
        if prev == card[0]:
            key = card[0]
            if key in pairs:
                pairs[key] += 1
            else:
                pairs[key] = 2
        prev = card[0]
    
    #Keeps track of the number of pairs and sets. The value of the previous dictionary
    #is the key. Therefore if there is a pair of 4s and 3 kings -> {"2":1,"3":1}
    nop = {}
    for k, v in pairs.items():
        if v in nop:
            nop[v] += 1
        else:
            nop[v] = 1
        
    #Here we determine the best possible combination the hand can be knowing if the
    #hand has a four of a kind, three of a kind, and multiple pairs.
        
    if 4 in nop:        #Has 4 of a kind, assigns the score and the value of the 
        score = 7
        kicker = pairs.keys()
        #ensures the first kicker is the value of the 4 of a kind
        kicker = [key for key in kicker if pairs[key] == 4] 
        key = kicker[0]

        #Gets a list of all the cards remaining once the the 4 of a kind is removed
        temp = [card[0] for card in hand if card[0] != key]
        #Gets the last card in the list which is the highest remaining card to be used in 
        #the event of a tie
        card_value = temp.pop()
        kicker.append(card_value)
            
        return [score, kicker] # Returns immediately because this is the best possible hand
        #doesn't check get the best 5 card hand if all users have a 4 of a kind
            
    elif 3 in nop:      #Has At least 3 of A Kind
        if nop[3] == 2 or 2 in nop:     #Has two 3 of a kind, or a pair and 3 of a kind (fullhouse)
            score = 6
                
            #gets a list of all the pairs and reverses it
            kicker = [k for k in pairs]   #Gets the card value of all the pairs 
            kicker = kicker[::-1]
            temp = kicker
                
            #ensures the first kicker is the value of the highest 3 of a king
            kicker = [key for key in kicker if pairs[key] == 3]
            if( len(kicker) > 1):   # if there are two 3 of a kinds, take the higher as the first kicker
                kicker.pop() #removes the lower one from the kicker
                
            #removes the value of the kicker already in the list
            temp.remove(kicker[0])
            #Gets the highest pair or 3 of kind and adds that to the kickers list
            card_value = temp[0]
            kicker.append(card_value)
            
        else:           #Has Only 3 of A Kind
            score = 3
                
            kicker = [k for k in pairs]       #Gets the value of the 3 of a kind
            key = kicker[0]
                
            #Gets a list of all the cards remaining once the three of a kind is removed
            temp = [card[0] for card in hand if card[0] != key]
            #Get the 2 last cards in the list which are the 2 highest to be used in the 
            #event of a tie
            card_value = temp.pop()
            kicker.append(card_value)
                
            card_value = temp.pop()
            kicker.append(card_value)
    
    elif 2 in nop:      #Has at Least a Pair
        if nop[2] >= 2:     #Has at least 2  or 3 pairs
            score = 2
            kicker = [k for k in pairs]   #Gets the card value of all the pairs 
            kicker = kicker[::-1]
            if ( len(kicker) == 3 ):    #if the user has 3 pairs takes only the highest 2
                kicker.pop()
                    
            key1 = kicker[0]
            key2 = kicker[1]
                
            #Gets a list of all the cards remaining once the the 2 pairs are removed
            temp = [card[0] for card in hand if card[0] != key1 and card[0] != key2]
                
        else:           #Has only a pair
            score = 1 
                
            kicker = [k for k in pairs]   #Gets the value of the pair
            key = kicker[0] 
     
            #Gets a list of all the cards remaining once pair are removed
            temp = [card[0] for card in hand if card[0] != key]
            #Gets the last 3 cards in the list which are the highest remaining cards
            #which will be used in the event of a tie
        for card in temp:
            kicker.append(temp.pop())
                
        
    #------------------------------------------------
    #------------Checking for Straight---------------
    #------------------------------------------------    
    #Doesn't check for the ace low straight
    counter = 0
    high = 0
    straight = False
        
    #Checks to see if the hand contains an ace, and if so starts checking for the straight
    #using an ace low
    if (hand[-1][0] == 14): 
        prev = 1
    else: 
        prev = None
            
    #Loops through the hand checking for the straight by comparing the current card to the
    #the previous one and tabulates the number of cards found in a row
    #***It ignores pairs by skipping over cards that are similar to the previous one
    for card in hand:
        if prev and card[0] == (prev + 1):
            counter += 1
            if counter == 4: #A straight has been recognized
                straight = True
                high = card[0]
        elif prev and prev == card[0]: #ignores pairs when checking for the straight
            pass
        else:
            counter = 0
        prev = card[0]
        
    #If a straight has been realized and the hand has a lower score than a straight
    if (straight or counter >= 4) and score < 4:
        straight = True  
        score = 4
        kicker = [high] #Records the highest card value in the straight in the event of a tie
    
    
    #------------------------------------------------
    #-------------Checking for Flush-----------------
    #------------------------------------------------
    flush = False
    total = {}
        
    #Loops through the hand calculating the number of cards of each symbol.
    #The symbol value is the key and for every occurrence the counter is incremented
    for card in hand:
        key = card[1]
        if key in total:
            total[key] += 1
        else:
            total[key] = 1
        
    #key represents the suit of a flush if it is within the hand
    key = -1
    for k, v in total.items():
        if v >= 5:
            key = int(k)
        
    #If a flush has been realized and the hand has a lower score than a flush
    if key != -1 and score < 5:
        flush = True
        score = 5
        kicker = [card[0] for card in hand if card[1] == key]        
        
        
    #------------------------------------------------
    #-----Checking for Straight & Royal Flush--------
    #------------------------------------------------
    if flush and straight:
            
        #Doesn't check for the ace low straight
        counter = 0
        high = 0
        straight_flush = False
            
        #Checks to see if the hand contains an ace, and if so starts checking for the straight
        #using an ace low
        if (kicker[len(kicker)-1] == 14): 
            prev = 1
        else: 
            prev = None
                
        #Loops through the hand checking for the straight by comparing the current card to the
        #the previous one and tabulates the number of cards found in a row
        #***It ignores pairs by skipping over cards that are similar to the previous one
        for card in kicker:
            if prev and card == (prev + 1):
                counter += 1
                if counter >= 4: #A straight has been recognized
                    straight_flush = True
                    high = card
            elif prev and prev == card: #ignores pairs when checking for the straight
                pass
            else:
                counter = 0
            prev = card
            
        #If a straight has been realized and the hand has a lower score than a straight
        if straight_flush:
            if high == 14:
                score = 9
            else:
                score = 8
            kicker = [high]
            return [score, kicker]
        
    if flush:     #if there is only a flush then determines the kickers
        kicker.reverse()
            
        #This ensures only the top 5 kickers are selected and not more.
        length = len(kicker) - 5
        for i in range (0,length):
            kicker.pop() #Pops the last card of the list which is the lowest
        
    #------------------------------------------------
    #-------------------High Card--------------------
    #------------------------------------------------
    if score == 0:      #If the score is 0 then high card is the best possible hand
        # Had to redo this code because the github guy didn't do it for hands < 7
        hand.sort()
        kicker = [hand[-2][0]]
        
    #Return the score, and the kicker to be used in the event of a tie
    return [score, kicker[0]]