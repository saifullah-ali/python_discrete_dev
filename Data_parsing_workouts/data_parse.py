#!/usr/bin/python

# python executables

import yaml
import json
from array import *
from Tkinter import *


def func(value):
    print(value)

root = Tk()
options = ["1", "2", "3"]
var = StringVar()
drop = OptionMenu(root, var, *options, command=func)
drop.place(x=10, y=10)

#import networkx as nx
#G = nx.Graph()


b=1

if b == 0:
	print "---------------------------------------------"
	print "------------ General Testing ----------------"
	print "---------------------------------------------"

	#perl hash {} perl list ()  array qw() --> list is not a data structure in perl (data types are - scalar $,array @,hash %)

	#1. hash :: %countries =  ( England => 'English', France => 'French' ) / $countries{England} = 'English' 
	#2. list::  ("Mon","Tue","Wed") 
	#3. Array :: @days = qw(Mon Tue Wed) / @days = ("Mon","Tue","Wed");
	# ==> accessing hash: $countries{England}

	#python dict {} python list [] tuples () array ([]) --> four built-in data structures in Python - list, tuple, dictionary and set, 
	#array is not data structure in python
	#1. Dictionary :: json_object = {
    #								"name":"Topology1",
    #								"description":"This is a topology",
    #								"run_sequentially":False,
    #								"concurrency":10
    #								}
	json_object = {
	"name":"Topology1",
	"description":"This is a topology",
	"run_sequentially":False,
	"concurrency":10
	}

	print "accessing <value> for key >name< in dictionary called json_object >key< <value> pair"
	print (json_object["name"])

	#2. list :: shoplist = ['apple', 'mango', 'carrot', 'banana'] --> list can be modified (mutable)

	shoplist = ['apple', 'mango', 'carrot', 'banana']
	print "accessing element 0 in list called shoplist"
	print (shoplist[0])


	#3. tuples :: zoo = ('python', 'elephant', 'penguin') --> tuple can not be modified (not mutable),example - tuple of user defined fn
	zoo = ('python', 'elephant', 'penguin') 
	print "accessing element 1 in tuple called zoo"
	print (zoo[1])

	#4. Array ::  --> array is not a data structure in python, you need to import array module to use that
	array1 = array('i', [10,20,30,40,50])
	print "accessing element 3 in array called array1"
 	print array1[3]

	#5. Set :: zoo = {'python', 'elephant', 'penguin'} --> A set is an unordered collection with no duplicate elements, does not support indexing

	zoo = {'python', 'elephant', 'penguin'}
	print "Printing the set called zoo"
	print zoo
	print "Printing the set called bri"
	bri = set(['brazil', 'russia', 'india'])
	print bri


elif b == 1:
	print "---------------------------------"
	print "------------ YAML----------------"
	print "---------------------------------"
	

	
	with open('cloud_info.yaml') as fh:
		struct = yaml.safe_load(fh)
		#struct = json.load(fh)
	print "printing yaml file::"
	print yaml.dump(struct)


	print "check key values"
	print "-----------------"
	print ("FROM verification")
	print (struct["verification"])
	print ("FROM nodes --> description")
	print (struct["nodes"][0]["description"])
	print ("FROM nodes --> (list 1) nics --> data_network")
	print (struct["nodes"][0]["nics"]["data_network"])
	print ("FROM nodes --> (list 2) nics --> data_network")
	print (struct["nodes"][1]["nics"]["data_network"])
	print ("FROM nodes --> item [3]")
	print (struct["nodes"][3])
	print ("FROM nodes --> (list 3) myname --> (list 1)")
	print (struct["nodes"][2]["myname"][0])


else:
	print "------------ JSON ----------------";

	

	print "Accessing json Data dictionary structure";
	with open('topo_info.json') as fh:
		struct = json.load(fh)
	
	#print (struct)
	print json.dumps(struct,indent=4)
	
	
	print "check key values"
	print "-----------------"
	print ("FROM description")
	print (struct["description"])
	print ("FROM nodes --> name")
	print (struct["nodes"][0]["name"])
	print ("FROM nodes --> chef_client_options --> all")
	print (struct["nodes"][0]["chef_client_options"])
	print ("FROM nodes --> chef_client_options --> 2nd option")
	print (struct["nodes"][0]["chef_client_options"][1])
	print ("FROM full-name --> last-name")
	print (struct["full-name"]["last-name"])
