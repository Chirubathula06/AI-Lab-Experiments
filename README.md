# 🤖 Artificial Intelligence Lab Experiments

This repository contains implementations of various Artificial Intelligence algorithms and problem-solving techniques as part of lab experiments.

All programs are implemented using Python and organized based on experiment numbers.

---

## 📚 List of Experiments

1.	Write a program to implement DFS and BFS  
2.	Write a Program to find the solution for traveling salesman Problem  
3.	Write a program to implement Simulated Annealing Algorithm  
4.	Write a program to find the solution for the wumpus world problem  
5.	Write a program to implement 8 puzzle problem   
6.	Write a program to implement Towers of Hanoi problem  
7.	Write a program to implement A* Algorithm  
8.	Write a program to implement Hill Climbing Algorithm 
9.	Build a Chatbot using AWS Lex, Pandora bots. 
10.	Build a bot that provides all the information related to your college. 
11.	Build a virtual assistant for Wikipedia using Wolfram Alpha and Python 
12.	The following is a function that counts the number of times a string occurs in another string: # Count the number of times string s1 is found in string s2 defcountsubstring(s1,s2): 
count = 0 
for i in range(0,len(s2)-len(s1)+1): if s1 == s2[i:i+len(s1)]: 
count += 1 return count 
For instance, count substring (’ab’,’cabalaba’) returns 2. 
Write a recursive version of the above function. To get the rest of a string (i.e. everything but the first character).  
13.	Higher order functions. Write a higher-order function count that counts the number of elements in a list that satisfy a given test. For instance: count (lambda x: x>2, [1, 2, 3, 4, 5]) should return 3, as there are three elements in the list larger than 2. Solve this task without using any existing higher order function. 
14.	Brute force solution to the Knapsack problem. Write a function that allows you to generate random problem instances for the knapsack program. This function should generate a list of items containing N items that each have a unique name, a random size in the range     1 ....... 5 and a random value in the range 1..... 10. 
Next, you should perform performance measurements to see how long the given knapsack solver take to solve different problem sizes. You should perform at least 10 runs with different randomly generated problem instances for the problem sizes 10,12,14,16,18,20 and 22. Use a backpack size of 2:5 x N for each value problem size N. Please note that the method used to generate random numbers can also affect performance, since different distributions of values can make the initial conditions of the problem slightly more or less demanding. 
How much longer time does it take to run this program when we increase the number of items? Does the backpack size affect the answer? 
Try running the above tests again with a backpack size of 1 x N and with 4:0 x N.  
15.	Assume that you are organising a party for N people and have been given a list L of people who, for social reasons, should not sit at the same table. Furthermore, assume that you have C tables (that are infinitely large). 
Write a function layout (N,C,L) that can give a table placement (i.e. a number from 0 : : :C -1) for each guest such that there will be no social mishaps. 
For simplicity we assume that you have a unique number 0 ......N-1 for each guest and that the list of restrictions is of the form [(X, Y) ...] denoting guests X, Y that are not allowed to sit together. Answer with a dictionary mapping each guest into a table assignment, if there are no possible layouts of the guests you should answer False. 


---

## 📂 File Structure

Each program is saved with its corresponding experiment number:

| Experiment | File Name |
|----------|----------|
| 1 | 1.py |
| 2 | 2.py |
| 3 | 3.py |
| ... | ... |
| 15 | 15.py |

---

## 💻 Technologies Used

- Python 🐍
- AI Algorithms
- Problem Solving Techniques

---

## 🎯 Purpose

This repository is created for:
- Academic learning
- AI algorithm practice
- Lab record reference

---

## 👨‍💻 Author

**BATHULA CHIRANJEEVI**  
BTech Computer Science Student  
Aspiring Software Developer 🚀

---

## ⭐ Note

Each file corresponds to a specific lab experiment. Refer to the experiment list above to understand the implementation.
