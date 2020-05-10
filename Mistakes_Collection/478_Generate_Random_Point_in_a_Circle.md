# 478

This problem type is quite rare and interesting, it's a probability problem. 

I quickly got the idea to use the polar coordinate to generate random R and 
random degree, however the answer is incorrect, I can't debug this since it's a probability problem.

After checking the discussion, I did estimate the probability carefully enough. Simply generate random R is not correct, given the area size is Pi * R^2, and we want to make the probability propotional to the size of the area, which, for instance, when Pi = 1, the area size is Pi, when Pi = 2, the area size is Pi * 4, and to make the probability propotional, the sqrt of R should follow uniform distribution.