"Mark43 Poker" Judger
=====================

Your task is to implement a program that accepts as its input a collection of hands of cards, and selects the winner from among those hands.

Input Format
------------

The input should be read over `stdin`. Some of the lines will contain collections of cards. These cards will be represented in the format format `<rank><Suit>`. rank will be one of:

* an integer from `2` to `9` for numbered cards less than ten
* `T` for ten
* `J` for jack
* `Q` for queen
* `K` for king
* `A` for ace

Suit will be one of:
* `h` for hearts
* `d` for diamonds
* `s` for spades
* `c` for clubs

Some example cards are `4d` for four of diamonds, `Ts` for ten of spades, and `Ah` for ace of hearts.

Input Data
----------
The first line of input will contain a single integer representing the number of players. This number will always be greater than 0 and less than 24.

The following `n` lines, where `n` is the number of players, will contain a single integer representing the id of the player, followed by three space-separated cards representing a hand belonging to a player.

An example input is as follows:

```
3
0 2c As 4d
1 Kd 5h 6c
2 Jc Jd 9s
```

Output Format
-------------

The output, printed to `stdout`, should simply be the id of the winning player. In the example above, the correct output would be:

```
2
```

as player two has the winning hand.

In the event of a tie, the ids of the winning players should be output on one line, space-separated, in ascending order. For example, for the input:
```
4
0 Qc Kc 4s
1 Ah 2c Js
2 3h 9h Th
3 Tc 9c 3c
```

the correct output would be:

```
2 3
```
as those two players have equivalent hands (flushes, with a ten, a nine, and a three).

"Mark43 Poker" Rules
----------------------

The winner of a round of  is the player with the best hand. The possible types of hands, ranked best to worst, are as follows:

* **Straight Flush:** A straight flush is a hand that is both a straight and a flush. That is to say, all three cards have the same suit, and their ranks form a "run" (check out the explanation for a straight).

* **Three Of A Kind:** A three of a kind is a hand in which all three of the cards have the same rank. An example might be `4c 4h 4d`, as all three cards are fours.

* **Straight:** A straight is a hand in which the cards have ranks that are in a "run." This means that they are of the format `n, n+1, n+2`. For example, the hand `5h 3c 4d` is a straight, because the cards can be ordered `3c 4d 5h` to form a "run" of `3-4-5`. The full order of the cards is `2, 3, 4, 5, 6, 7, 8, 9, T, J, Q, K, A`. Face cards form runs when they appear in that order, so `Qh Kd As` is a straight, because they form a run of `Q-K-A`. Runs can also include numbers and face cards, so `9h Td Js` is straight because it forms a run of `9-T-J`. When considering a straight, aces can also be used as a 1. That means that `A-2-3` is also a run. An ace cannot, however, be both high and low in the same straight, so `K-A-2` does not qualify.

* **Flush:** A flush is a hand in which all three cards have the same suit. An example might be `Ac 4c 8c`, as all three cards are clubs.

* **Pair:** A pair is a hand in which two of the cards have the same rank, but the third is different. An example is `4c 4d Ah`. This is a "pair of fours", because it has two fours.

* **High Card:** Any hand that doesn't fit into one of the other categories is considered a "high card" hand.

When comparing hands of the same type, the winner is the hand whose highest card is ranked higher. Therefore, `Ah 5h 2h` beats `Qd Jd 7d` because the first hand's highest card, an Ace, is ranked higher than the second hand's highest card, a Queen. If the highest cards are equal, then the second highest cards should be compared. If those are equal, the third highest cards should be compared. If all three are equal, then the hands are tied.

The exception to this comes when comparing pairs. If two hands are both a pair, the winning hand is the hand that has a higher pair. For example `8c 8h 4d` beats `5s 5h 2h` because the pair of `8`s beats the pair of `5`s. If the pair is tied, then the remaining card is used to decide the winner.

(Mark43 poker is actually just 3 Card Poker. You can read more about it [in this wikipedia article.](https://en.wikipedia.org/wiki/Three_card_poker))

Using the test runner
----------------------

We have provided the test runner that we will use to check your solution, along with two sample tests. We have many more tests that we will run internally, so passing the two we sent _does not_ imply that your solution is correct/complete.

To run the tests, first perform any compilation or preprocessing that your solution requires, then use the `run_tests` python script and pass the command that runs your program in as a string argument. For example, if your test is a python file called `poker.py` then you might run `./run_tests "python poker.py"`. Make sure you run this from the directory that the `run_tests` script is located in. Feel free to reach out to us if you have any problems using the test runner.

What to submit
--------------

Your submission should be a zip file containing all the files needed to compile/run your submission, as well as a plain text file titled `README` which should include instructions on how to compile/run your submission along with any notes you think are relevant about design decisions and/or known bugs and limitations in your submission. Please be very explicit in the `README` about how to run your test. Additionally, your program should be able to run all of the included tests using the `run_tests` script included. It is what we will use to grade your test, so if it doesn't run with `run_tests`, then it won't run for us.

If your test requires compilation prior to being run, please include instructions on how to do so. A Makefile is not required, but would be appreciated if the compilation is a multi-step process.
