#!/bin/python3

#For this program we will need the networkx library.
#For Linux we make sure we have pip3 (v3.7/8), as this script is in python 3.7
#Then we open the terminal and type: pip3 install networkx.
#For Windows we will need a Python dist. like ANACODA



#Eulerian circuit

# We import the Networkx library that helps us with Eulerian Circuits.
import networkx as netx
#----------------------------------------------------------
# We create a function that checks if num is a number, and if it is a string we are prompted to enter a valid value.
def incNumNode(num):
	try:
		num = int(num)
		i = 0
	except:
		i = 1
#----------------------------------------------------------

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

#----------------------------------------------------------

G = netx.complete_graph(num)
try:
	print("One Eulerian Circuit is: "+str(list(netx.eulerian_circuit(G))))
except:
	print("There is no Eulerian Circuit for a complete graph with " + str(num) + " nodes.")
