#### Please add your answers to the ***Analysis of  Algorithms*** exercises here.

## Exercise I

a) Time: O(n), Space: O(1)
Time complexity is O(n) since its a while loop that will be iterated linearly with respect to n.
Space complexity is O(1) since its a simple mathematical equation

b) Time: O(n), Space: O(1)
Time complexity for the inner loop seems to be logarithmically related to n. And the outer loop will be iterated n times. It can be simplified to O(n)
Space complexity is 1 since its simple mathematical variables, even though there are two of them

c) Time: O(n), Space: O(n)
time complexity is O of n because of recursion.
Space complexity is O of n again because of its stored in memory through the whole recursion stack

## Exercise II

The building has n floors.
Egg is broken if thrown from floor f and higher.

Number of eggs:0 [counter]
Number of drops: 0 [counter]

Strategy: Start at the middle and use binary search method to either go up or down. Every attempt will change the floor to half of the remaining floors, either up or down. Until if you move down, it doesn't break.

Since its binary search, the time complexity will be O(log(n). And the space complexity will be O(n) or slightly more, but can be rounded off to O(n).


def test(min_floor, max_floor, Number_of_eggs, Number_of_drops)

   if max_floor - min_floor == 1
        return(min_floor, Number_of_eggs, Number_of_drops)

   try_floor = (max_floor - min_floor)/2
   if egg is not broken:      
        Number_of_drops += 1
        min_floor = try_floor + 1        
        return test(min_floor, max_floor, Number_of_eggs, Number_of_drops)

    else
        Number_of_eggs += 1
        Number_of_drops += 1        
        max_floor = try_floor - 1
        return test(min_floor, max_floor, Number_of_eggs, Number_of_drops)
