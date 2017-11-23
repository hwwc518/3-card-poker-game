# 3 card poker
import fileinput

# dictionary of card ranks
rank = {
        '2':2,
        '3':3,
        '4':4,
        '5':5,
        '6':6,
        '7':7,
        '8':8,
        '9':9,
        'T':10,
        'J':11,
        'Q':12,
        'K':13,
        'A':14
        }

hands = [];

for line in fileinput.input():
    # remove unwanted input and insert into hands
    hand = line.split()
    if (len(hand) == 4 and len(hand[0]) == 1 and len(hand[1]) == 2 and
            len(hand[2]) == 2 and len(hand[0]) == 1):
        hands.append(hand)

# Loop through the list of hands and append two values, one - the type, ie
# straight flush, pair, etc., the other value - the highest card in the hand
# int high
for hand in hands:
   # create list of card ranks
   cards = []

   # append integer values of card ranks
   cards.append(rank[hand[1][0]])
   cards.append(rank[hand[2][0]])
   cards.append(rank[hand[3][0]])

   # sort the hands
   cards.sort()
   
   # test if same suit
   if (hand[1][1] == hand[2][1] and hand[2][1] == hand[3][1]):
       sameSuit = True
   else:
       sameSuit = False

   # determine hand types
   # first append is the hand type, second is the value of hands's highest card
   # (except for pairs)

   # --Straight Flush (6)
   if (cards[0]+1 == cards[1] and cards[1]+1 == cards[2] and sameSuit):
       hand.append(6)    
       hand.append(cards[2])
     
   # --Three of a Kind (5)
   elif (cards[0] == cards[1] and cards[1] == cards[2]):
       hand.append(5)    
       hand.append(cards[2])
   
   # --Straight (4)
   elif (cards[0]+1 == cards[1] and cards[1]+1 == cards[2]):
       hand.append(4)    
       hand.append(cards[2])
 
   # --Flush (3)
   elif (sameSuit):
       hand.append(3)    
       hand.append(cards[2])

   # --Pair (2)
   elif (cards[0] == cards[1] or cards[1] == cards[2]):
       hand.append(2)   
       hand.append(cards[1])  # in a pair, middle card is always in pair
   
   # --High Card (1)
   else:
       hand.append(1)
       hand.append(cards[2])

# loop through hands and determine winner
# initialize highest hand to first hand
highest = [hands[0][4], hands[0][5]]

# initialize store for winners / duplicates
store = [hands[0][0]]

# comparison phase
for hand in hands[1:]:
    if hand[4] > highest[0]:    # bigger hand
        highest = [hand[4],hand[5]]
        del store[:]
        store.append(hand[0])

    # equal hands - compare highest card
    elif hand[4] == highest[0] and hand[5] > highest[1]:
        highest = [hand[4],hand[5]]
        del store[:]
        store.append(hand[0])        
        
    elif hand[4] == highest[0] and hand[5] == highest[1]:
        store.append(hand[0])

# for hand in hands:
#     print (hand)

# print winners
print (*store)



