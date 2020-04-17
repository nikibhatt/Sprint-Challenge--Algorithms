#### Please add your answers to the ***Analysis of  Algorithms*** exercises here.

## Exercise I

a) Time: O(log(n)), Space: O(1)
Time complexity is Log(n) since within the while loop, the n is getting squared. So the iterations is exponentially lesser.
Space complexity is O(1) since its a simple mathematical equation

b) Time: O(n^2), Space: O(1)
Time complexity is N squared because of the nested loops. Even though the J is doubled up and while loop is not running n times, it rounds up to N square.
Space complexity is 1 since its simple mathematical variables, even though there are two of them

c) Time: O(n), Space: O(n)
time complexity is O of n because of recursion.
Space complexity is O of n again because of its stored in memory through the whole recursion stack

## Exercise II

The building has n floors.
Egg is broken if thrown from floor f and higher.
Number of eggs:0 [counter]
Number of drops: 0 [counter]

Strategy: Start at the middle and change one floor at a time. Keep track of result of previous attempt. This is the least efficient way.
Since its linear search kind of Algorithms, the time complexity will be O(n/2) or O(n). And the space complexity will be O(n) or slightly more, but can be rounded off to O(n).

def test(n):
   try_floor = n/2
   prev_attempt = null
   egg is dropped
   while try_floor is not 0 or try_floor is not n:
    If egg is not broken and prev_attempt = true:      
        Number_of_drops += 1
        try_floor = try_floor+1        
    else (egg is broken and prev_attempt = true)
        Number_of_eggs += 1
        Number_of_drops += 1
        try_floor = try_floor - 1
        prev_attempt = false


        egg         prev_attempt      result
        breaks      breaks            keep going
        breaks      didnt breaks      return prev_floor
