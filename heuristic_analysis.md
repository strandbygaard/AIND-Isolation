# Overall Summary
The custom score isn't fully able to beat the AB_Improved player.

Results of the tournament were as follows:

```
 Match #   Opponent    AB_Improved   AB_Custom   AB_Custom_2  AB_Custom_3 
                        Won | Lost   Won | Lost   Won | Lost   Won | Lost 
    1       Random       7  |   3     9  |   1     6  |   4     9  |   1  
    2       MM_Open      7  |   3     6  |   4     7  |   3     6  |   4  
    3      MM_Center     8  |   2     8  |   2     8  |   2     9  |   1  
    4     MM_Improved    8  |   2     8  |   2     4  |   6     5  |   5  
    5       AB_Open      6  |   4     4  |   6     5  |   5     5  |   5  
    6      AB_Center     6  |   4     5  |   5     5  |   5     5  |   5  
    7     AB_Improved    6  |   4     5  |   5     4  |   6     3  |   7  
--------------------------------------------------------------------------
           Win Rate:      68.6%        64.3%        55.7%        60.0%  
```

The best evaluation function to use is custom score heuristic 1. The reasons why this is the best of the three evaluation functions are:

1. It is consistently the function that has the highest win rate of the three implemented functions.
2. It addresses an obvious limitation of custom score heuristic 3, by being able to provide a positive or negative score, even if the available moves count of both players is the same.
3. It is easy to explain and understand its behavior. The other two custom heuristics are simpler, but are also have a lower win rate. It's makes analysis of the programme much simpler, if the scoring function is simple, and easily understood.    

## Custom Score Heuristic 1
This heuristic is an extension of the heuristic covered in the lectures, where the score is proportional to the difference between the number of moves available to the current player and the opponent. 

As long as the number of moves available to each is not the same, then the score is kept proportional to the difference in number of moves.

If the number of moves available is the same, then the score is based on who is closer to the center of the board. This is based on the hypothesis, that being closer to the center of the board is an advantage.

In this case, the score is calculated as the difference in distance to the center, scaled by 1/10. The scale is to ensure, that this position does not result in a higher score, than actually having a 1 or more move advantage over the opponent.

There's a limitation in this scaling. If the board becomes large, then scaling by a fixed 1/10 means that the difference in distance may result in an greater advantage if the board is large enough. But for the board sizes used in this simulation, the 1/10 scaling works fine.

## Custom Score Heuristic 2
This heuristic is an implementation of the basic heuristic covered in the lectures, where the score is proportional to the number of moves left for the current player.

## Custom Score Heuristic 3
This heuristic is an implementation of the heuristic covered in the lectures, where the score is difference between the number of moves left for the current player, and the number of moves left for the opponent.
