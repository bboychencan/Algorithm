# Randomized Algorithm

In codejam 2019 round1A, I got stuck with the `pylon` problem.
It's a NP problem, I tried using state compression and dp but can not reduce the time
complexity into decent scope. 

Then I investigated Gennady and ACRush's solutions. A new world opened up in front of me.
It's my first time to come across the `Randomized Algorithm` it is very smart.
For traditional dfs or other solution, we always iterate all conditions using a for loop.
And the i,j increments by 1 each time. For this problem, it's obviously not good to search
in this way,(the contrain says, the next jump should not be in same row, col, even diagnoal)
So, if we use the original way to do our dfs, it will be super slow. 

BUT, if we shuffle the options we want to dfs, it will much easier for us to quickly find a 
solution, because there are many solutions to this problem (That requires skill to identify this.)

Then, given that the problem only requires us to output any of the solution, and there are many
possible solutions, randomized algorithm comes in the way perfectly. 
