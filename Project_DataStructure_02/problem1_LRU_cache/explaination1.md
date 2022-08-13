1. Constructor
   I create 3 variable:
   capacity: number - save maximum capacity
   dict : dictionary - save key and value (parameter)
   history : dictionary - save key (key - parameter) , value (number call get by key)

2. Method get:

- if
  - check value is None -> return -1
- else
  - increase value by key in dictionary history 1
  - and return value

3. Method set

- check number element in history = number capacity -> must to remove element( remove not recently used)
  - get key what value is minimum in dictionary history
  - remove that element by key in dictionary history and dict
- set data to dict
- set data to history with value is 0

Time complexity: I think what make cost is min in method set -> it make O(n)
another method get , or set is O(1)
-> so complex is O(n)
