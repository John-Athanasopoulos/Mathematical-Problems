#!/bin/python3
import networkx as netx

# We create a function that checks if num is a number, and if it is a string we are prompted to enter a valid value.
def incNumNode(num):
	try:
		num = int(num)
		i = 0
	except:
		i = 1

num = (input("Enter the number of nodes: "))
i = 1
while i == 1:
	try:
		num = int(num)
		i = 0
	except:
		print("The number of nodes was incorrect. Please enter the number again.")
		incNumNode(num)
		num = (input("Enter the number of nodes: "))

#I have made it for a complete graph. Of course you can make whatever graph you want.
G = netx.complete_graph(num)
try:
	print("One Eulerian Circuit is: "+str(list(netx.eulerian_circuit(G))))
except:
	print("There is no Eulerian Circuit for a complete graph with " + str(num) + " nodes.")
