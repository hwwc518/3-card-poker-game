1) Submission file is locared in game.py (uses python3)
2) Test can be run using './run_tests "python3 game.py"`
3) - I first created a dictionary of card ranks, mapping them to integers and
then comparing those integers to determine higher card rank.
4) - I read in the file and decided to only look at input where the split list
had a length 4. This also left lines such as "Pair beats high card" that weren't
cards however.
5) - As a result, I had a manual/ hardcoded test that checks length of each
element in the list. This eliminated the "Pair beats high card instance, however,
also means that other strings that may have a similar format might pose a
problem. As an alternative, I think that regex could be used to check/ verify
cards if necessary.
6) - I did not use the provided number of players.
7) - I then appended to the list of hands, a number representing the
classification of hand as well as the highest value card in the hand(except for
a pair, where it is the value of the pair)
8) - I then looped through the list again and compared the values of their
hands, storing the values of the highest hand. I initialized the highest hand to
the first hand, meaning that if there were only one hand, the program would not
work.
9) - Finally, I printed the winning hands
