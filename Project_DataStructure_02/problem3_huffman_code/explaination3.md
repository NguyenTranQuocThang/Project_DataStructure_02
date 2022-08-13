Before I'am really sorry about my solution, because it's hard to understand. I will explain it , hope u understand

Explain a little special handle

1. I use queue priority like recommend solution to order queue what i will insert data after each loop

2. I use Stack and State to implement traverse tree with depth first search traversal
   ( what you teach me in lecture )
   ( I customize it - a little in State)

3. U can see when i put element to queue i will put format: (value,count,key)
   In here: count is element number auto increase 1 after each loop
   I use that to prevent exception : Cast type error of PriorityQueue (I know u understand if i just put (value,key))

   Furthermore I put value before to queue auto sort by value (frequence)

Explain a function

1.huffman_encoding
Step1: I check case zero data and 1 element in text (text will encode) -> i will not explain it

Step2: I loop all character and add it to dictionary with key and value to get frequence of each character

Step3: I convert dictionary to PriorityQueue to help me sort

Step4: I loop in queue

Step5: I will get 2 element in queue(with frequence is lowest)
-> Create two nodes what corresponding with node_left and right
-> Create father node and set left right with 2 nodes (above)

Step6: I will call function traverse_node() when loop in queue have size is one

Step7: I get dictionary what have couple of key and value (key is characer and value is huffman code)

Step8: I replace all character with huffman code

2.huffman_decoding

Step0: I check for case empty and case 1 character

Step1: I iterate code

Step2: I check if 0 -> left, 1 -> right and if get leaves -> add to new blank string

Complexity of this code:
Very complex :( - sorry, i'm very busy to make cleaner

I think :

encode: it is tree -> time complexity log(n) (actually greater a lot than log n )
Space complexity: log(n)

decode: time complexity : O(n) 
Space complexity: O(n)
