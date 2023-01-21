# Mathematical Problems
A repository with calculation programs for mathematical problems

In this repository there are programs with which you can find the answer for mathematical problems, as finding an Eulerian Circuit for a 5 node graph, if it exists (spoiler: it does).

## There are the following programs:
**1. Eulerian Circuit Finder**

The name is pretty self explanatory. When you run the program, you will be prompted to enter a number of nodes. Don't worry, if it is incorrect you will be asked again until a valid value is entered. Afterwards, it will automatically find if an Eulerian Circuit (closed path) of the said nodes exists, and if it does, it will be printed as a sequence of numbers (the nodes' names are the numbers from 0 to n-1 for n nodes). Keep in mind that in order for the program to work, you will need the **NetworkX** library.

**2. Havel-Hakimi Theorem (for Graphs)**

The Havel–Hakimi algorithm is an algorithm in graph theory solving the graph realization problem. That is, it answers the following question: Given a finite list of non-negative integers, is there a simple graph such that its degree sequence is exactly this list? The degree sequence is a list of numbers that for each vertex of the graph states how many neighbors it has. For a positive answer, the list of integers is called graphic. The algorithm constructs a special solution if one exists or proves that one cannot find a positive answer. This construction is based on a recursive algorithm. There are 3 options:
<ul>Option 1: You enter all the data manually
<br>Option 2: You enter a string containing the degree sequence
<br>Option 3: You enter the name of a file containing one (or more) degree sequence(s).</ul>
<br>In order to run this program, you will need **networkx** and **matplotlib**

