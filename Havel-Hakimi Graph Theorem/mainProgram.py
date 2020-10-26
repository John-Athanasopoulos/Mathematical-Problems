from operator import itemgetter
import networkx as nx
import matplotlib.pyplot as plt

action = input("Input the action you want from the following:\n1. Manual input\n2. Degree sequence from string (format: 2, 2, 2)\n3. Degree sequence from file (format: 2, 2, 2)\n\nAction: ")
while action != "1" and action != "2" and action != "3":
    print("Wrong input for the action. Please try again.")
    action = input("Input the action you want from the following:\n1. Manual input\n2. Degree sequence from string (format: 2, 2, 2)\n3. Degree sequence from file (format: 2, 2, 2)\n\nAction: ")

if action == "1":
    x = input("Enter how many nodes the graph has: ")
    x = int(x)
    nodes = []
    lines = []
    nodesNames = []
    nodesFinal = []
    G = nx.Graph()

    for i in range(x):
        y = input("Enter the degree of the " + str(i + 1) + " node: ")
        while int(y)>=x or int(y)<0:
            y = input("The degree of a node is at most n-1 for n nodes and at least 0. Please enter a correct value.\nEnter the degree of the " + str(i+1) + " node: ")
        nodes.append(int(y))
        
    nodesDictionary = {}

    for s in range(x):
        nodesDictionary["a"+str(s+1)] = nodes[s]

    print("------------------------------------")
    print("The degrees of the nodes are: "),
    print(nodesDictionary)
    print("------------------------------------")
    nodes.sort()
    nodes.reverse()
    print("The degrees when sorted are the following: ")
    print(nodes)
    print("------------------------------------")

    for s in nodes:
        for t in nodesDictionary:
            if nodesDictionary[t] == s and t not in nodesNames:
                nodesNames.append(t)

    print("The nodes sorted by degree are: ")
    print(nodesNames)
    print("------------------------------------\n")

    G.add_nodes_from(nodesNames)

    for i in range(len(nodes)):
        nodesFinal.append([nodesNames[i],nodes[i]])

    enable = True

    while nodesFinal[0][1] != 0:    #While there is at least one node with degree != 0
        for i in range(nodesFinal[0][1]):   #Loop for n times, n being the degree of the first node in the degree sequence
            lines.append((nodesFinal[0][0],nodesFinal[i+1][0]))  #Append in the lines list all the lines consisting of the first node and the n following nodes
            nodesFinal[i+1][1] -= 1  #Decrease the following nodes degrees by 1
        nodesFinal[0][1] = 0  #Make the first node equal to 0
        nodesFinal = sorted(nodesFinal, key=itemgetter(1))  #Sort the nodesFinal list based on the degrees (second dimension of the array)
        nodesFinal.reverse()  #Reverse the sorted list, so that the greater degrees are first in the degree sequence (descending order)
        for i in range(len(nodesFinal)):
            if nodesFinal[i][1] < 0:   #For every node in the nodesFinal list,if there degree is less than 0 after the reduction of the degree of the n following nodes, this means that there is no graph with the given degrees
                print("There isn't a graph with the degrees you have chosen...")
                enable = False
                nodesFinal[0][1] = 0 #Make nodesFinal[0][1] = 0 to exit the while loop
                break
            elif i == len(nodesFinal):
                print("The new degree list is the following: " + str(nodesFinal))

    G.add_edges_from(lines)  #Add to the graph all the lines (edges)

    if enable == True:  
        print("The lines of the graph are: ")
        print(G.edges())
        nx.draw(G, with_labels=True, font_color="white")
        plt.show()

elif action == "2":
    s = input("Input the string containing the degree sequence (Format is: 4, 4, 3, 1, 1 order doesn't count): ")
    s.replace(" ","")
    nodes = []
    nodesNames = []
    nodesFinal = []
    lines = []
    
    for c in s.split(","):
        nodes.append(int(c))
    x = len(nodes)
    nodes.sort()
    nodes.reverse()
    if nodes[0] >= x:
        print("The degree sequence you provided is incorrect (there is a node with degree equal or greater than the number of nodes).")
    else:
        G = nx.Graph()
        for i in range(x):
            G.add_node(str(i+1))
            nodesNames.append(str(i+1))
        enable = True
        
        for k in range(len(nodes)):
            nodesFinal.append([nodesNames[k],nodes[k]])
        print(nodesFinal)
        
        while nodesFinal[0][1] != 0:    #While there is at least one node with degree != 0
            for i in range(nodesFinal[0][1]):   #Loop for n times, n being the degree of the first node in the degree sequence
                lines.append((nodesFinal[0][0],nodesFinal[i+1][0]))  #Append in the lines list all the lines consisting of the first node and the n following nodes
                nodesFinal[i+1][1] -= 1  #Decrease the following nodes degrees by 1
            nodesFinal[0][1] = 0  #Make the first node equal to 0
            nodesFinal = sorted(nodesFinal, key=itemgetter(1))  #Sort the nodesFinal list based on the degrees (second dimension of the array)
            nodesFinal.reverse()  #Reverse the sorted list, so that the greater degrees are first in the degree sequence (descending order)
            for i in range(len(nodesFinal)):
                if nodesFinal[i][1] < 0:   #For every node in the nodesFinal list,if there degree is less than 0 after the reduction of the degree of the n following nodes, this means that there is no graph with the given degrees
                    print("There isn't a graph with the degrees you have chosen...")
                    enable = False
                    nodesFinal[0][1] = 0 #Make nodesFinal[0][1] = 0 to exit the while loop
                    break
                elif i == len(nodesFinal):
                    print("The new degree list is the following: " + str(nodesFinal))
        
        G.add_edges_from(lines)  #Add to the graph all the lines (edges)

        if enable == True:  
            print("The lines of the graph are: ")
            print(G.edges())
            nx.draw(G, with_labels=True, font_color="white")
            plt.show()
        
        
else:
    fileName = input("Input the name of the file that contains the degree sequence(s): ")
    f = open(fileName, "r")
    degreeSequences = f.readlines()
    for ds in degreeSequences:
        nodes = []
        nodesNames = []
        nodesFinal = []
        lines = []
        ds.replace(" ","")
        
        for c in ds.split(","):
            nodes.append(int(c))
        x = len(nodes)
        nodes.sort()
        nodes.reverse()
        if nodes[0] >= x:
            print("The degree sequence you provided is incorrect (there is a node with degree equal or greater than the number of nodes).")
        else:
            G = nx.Graph()
            for i in range(x):
                G.add_node(str(i+1))
                nodesNames.append(str(i+1))
            enable = True
            
            for k in range(len(nodes)):
                nodesFinal.append([nodesNames[k],nodes[k]])
            print(nodesFinal)
            
            while nodesFinal[0][1] != 0:    #While there is at least one node with degree != 0
                for i in range(nodesFinal[0][1]):   #Loop for n times, n being the degree of the first node in the degree sequence
                    lines.append((nodesFinal[0][0],nodesFinal[i+1][0]))  #Append in the lines list all the lines consisting of the first node and the n following nodes
                    nodesFinal[i+1][1] -= 1  #Decrease the following nodes degrees by 1
                nodesFinal[0][1] = 0  #Make the first node equal to 0
                nodesFinal = sorted(nodesFinal, key=itemgetter(1))  #Sort the nodesFinal list based on the degrees (second dimension of the array)
                nodesFinal.reverse()  #Reverse the sorted list, so that the greater degrees are first in the degree sequence (descending order)
                for i in range(len(nodesFinal)):
                    if nodesFinal[i][1] < 0:   #For every node in the nodesFinal list,if there degree is less than 0 after the reduction of the degree of the n following nodes, this means that there is no graph with the given degrees
                        print("There isn't a graph with the degrees you have chosen...")
                        enable = False
                        nodesFinal[0][1] = 0 #Make nodesFinal[0][1] = 0 to exit the while loop
                        break
                    elif i == len(nodesFinal):
                        print("The new degree list is the following: " + str(nodesFinal))
            
            G.add_edges_from(lines)  #Add to the graph all the lines (edges)

            if enable == True:  
                print("The lines of the graph are: ")
                print(G.edges())
                nx.draw(G, with_labels=True, font_color="white")
                plt.show()
