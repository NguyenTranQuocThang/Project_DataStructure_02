1. Directory : is Path of my project , please keep it for avoid error
   u can change it if u defind a good path because with bad path , it can make exception
   and i don't want to handle it right now

2. Function find_files(suffix,path):
   I use that function to get list file and call recursive of loop_recursive() fuction

3. Function loop_recursive(suffix,path,list):
   I use that function to loop in list what get from find_files() function
   list parameter can control base case recursive (size of list is 0 -> stop recursive)

process: i will loop to the end element -> check directory + element is file or not -> if is file

-> ok -> check end file with suffix -> ok -> add to array
-> not ok -> call function find_files() -> get new list in this path -> continue recursive

4. Complexity : I think i must to loop file what stay in directory -> O(n). But each directory have more file -> I will get O(n)[n is size of sub directory].
   Can u help me to find exactly complexity ... i still confuse about that
