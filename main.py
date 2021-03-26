# Daryl Augustin SID#: 001197863

import csv
from Hash_Table import HashMap
hash_table = HashMap()

with open('c950_names.csv') as csvfile:
    readCSV = csv.reader(csvfile, delimiter=',')
    addressList = []
    for raw in readCSV:
        addressList.append(raw[2]) #addessList stores address info
    #print(addressList)



class Package:
	"""docstring for Package"""
	def __init__(self, id, address, city,state,zip,deadline, weight, notes=None):
		self.id = id
		self.address = address
		self.addressID = None
		self.city = city
		self.state = state
		self.zip = zip
		self.deadline = deadline
		self.weight = weight
		self.notes = notes
		self.delivered = 'HUB'
		self.deliveryTime = None
		self.truck_no = None


	def deliver(self,deliveryTime):
		self.delivered = 'Delivered'
		self.deliveryTime = deliveryTime

	def get_addressID(self,addressList):
		for i in range(len(addressList)):
			if self.address in addressList[i]:
				self.addressID = i #Here addressID is addressList index
				break

	def get_truck_no(self):
		if(self.deadline!='EOD'):
			if('Delayed' in self.notes):
				self.truck_no = 2
			elif('Can only be' in self.notes):
				self.truck_no = 2
			elif('300 State' in self.address):
				self.truck_no = 2
			else:
				self.truck_no = 1
		else:
			if('Wrong' in self.notes):
				#print('yes')
				self.address='410 S State St'
				self.city='Salt Lake City'
				self.zip='84111'
				self.truck_no = 3
			elif('Can only be' in self.notes):
				#print('yesc')
				self.truck_no = 2
			elif('410 S' in self.address or '300 State' in self.address or '5883' in self.address):
				self.truck_no = 2
			elif('177 W' in self.address or '1330' in self.address or '380 W' in self.address or '3365 S' in self.address):
				self.truck_no = 1
			else:
				self.truck_no = 3

	def show_package(self):
		#'{0:02.0f}:{1:02.0f}'.format(*divmod(float(time) * 60, 60)) to convert float to time format
		#id + 1 used bexuase I calcuated it with (0 to 39) index and Want to show as (1 to 40)
		print("{:<8} {:<10} {:<10} {:<10} {:<10}".format(self.id+1, self.addressID, self.truck_no, self.deadline,self.delivered),'\t','{0:02.0f}:{1:02.0f}'.format(*divmod(float(self.deliveryTime) * 60, 60)))
		#print(self.id,'\t',self.addressID,'\t',self.truck_no,'\t', self.deadline,'\t', self.delivered,'\t','{0:02.0f}:{1:02.0f}'.format(*divmod(float(self.deliveryTime) * 60, 60)))


#taking values from csv files and store them in Package type object
#Then appending all package in hash_table and packagelist

with open('c950inputs.csv') as csvfile:
    read_inputCSV = csv.reader(csvfile, delimiter=',')
    packageList = []
    index = 0
    for row in read_inputCSV:
        id = index
        index = index + 1
        address = row[1]
        city = row[2]
        state = row[3]
        zip = row[4]
        delivery = row[5]
        size = row[6]
        note = row[7]
        p1 = Package(id, address, city,state,zip,delivery, size, note)
        packageList.append(p1)  #appending packages in packageLList
        hash_table.insert(id,p1) #inserting packages in hash_map

#truck1, truck2, truck3 will store packages of specific truck based on requirements(.get_truck_no)
truck1=[]
truck2=[]
truck3=[]
for i in range(len(packageList)):
	packageList[i].get_truck_no()
	packageList[i].get_addressID(addressList) #each package address id from address 
	#packageList[i].show_package()
	if(packageList[i].truck_no == 1):
		truck1.append(packageList[i])
	elif(packageList[i].truck_no == 2):
		truck2.append(packageList[i])
	else:
		truck3.append(packageList[i])
print('No. of package in Truck 1: ',len(truck1))
print('No. of package in Truck 2: ',len(truck2))
print('No. of package in Truck 3: ',len(truck3))

'''
to_visit1=[]
to_visit2=[]
to_visit3=[]
for i in range(len(truck1)):
	if(truck1[i].addressID not in to_visit1):
		to_visit1.append(truck1[i].addressID)

for i in range(len(truck2)):
	if(truck2[i].addressID not in to_visit2):
		to_visit2.append(truck2[i].addressID)

for i in range(len(truck3)):
	if(truck3[i].addressID not in to_visit3):
		to_visit3.append(truck3[i].addressID)

print(to_visit1)
print(to_visit2)
print(to_visit3)
'''

#dist is a 2D list stores all distance from every distance node. distance node and addressID index are same 
with open('c950_distance.csv') as csvfile:
    readCSV = csv.reader(csvfile, delimiter=',')
    dist = []
    for raw in readCSV:
        dist.append(raw)

    for i in range(len(dist)):
        for j in range(len(dist[i])):
            if(i<j):
                dist[i][j] = float(dist[j][i])
            else:
                dist[i][j] = float(dist[i][j])
'''
current_node = 0
total_distance = 0
deli_time = 8
while(len(to_visit1)>0):
    min_value = 999999999
    for i in range(len(to_visit1)):
        if min_value > dist[current_node][to_visit1[i]]:
            min_value = dist[current_node][to_visit1[i]]
            index = to_visit1[i]
    
    delivered_list=[]
    for i in range(len(truck1)):
    	if(truck1[i].addressID == index):
    		#print("in")
    		deli_time = deli_time + min_value/18
    		truck1[i].deliver(deli_time)
    		delivered_list.append(i)
    print(delivered_list)
    #removing packages from truck
    #for i in range(len(delivered_list)):
    # 	truck1.pop(delivered_list[i])

    print(current_node,min_value)
    current_node = index
    total_distance = total_distance + min_value
    to_visit1.remove(index)
print(current_node)
print("The end"+ str(total_distance))

#for i in range(len(packageList)):
#	packageList[i].show_package()
#for i in range(len(truck1)):
#	truck1[i].show_package()
'''

#deliver package function 
#takes three arguments truck(list consists of package objects) , dist(a list of distance of each node/addrssID)
# and start delivery time(8/9.25/10.5)
# arguments are truck1,truck2,truck3
#The function then deliver parcels in places using greedy approach(Traveling salesman problem) 
def deliver_package(truck,dist,deli_time):
	to_visit=[] #this is a list with specific address id for delivering parcel for one truck
	for i in range(len(truck)):
		if(truck[i].addressID not in to_visit):
			to_visit.append(truck[i].addressID)
	current_node = 0
	total_distance = 0
	#deli_time = 8
	while(len(to_visit)>0):
	    min_value = 999999999
	    for i in range(len(to_visit)):
	        if min_value > dist[current_node][to_visit[i]]:
	            min_value = dist[current_node][to_visit[i]]
	            index = to_visit[i]  #finding and selecting node with minimal distance from current node
	    
	    #delivered_list=[]
	    deli_time = deli_time + min_value/18 #delivery time is a float value ex: 8:30 = 8.5
	    for i in range(len(truck)):
	    	if(truck[i].addressID == index): #finding packages to deliver in minimal node
	    		#print("in")
	    		truck[i].deliver(deli_time) #update time and delivery status of that package
	    		#delivered_list.append(i)
	    #print(current_node,min_value)
	    current_node = index  
	    total_distance = total_distance + min_value #adding that distance with total distance
	    to_visit.remove(index) #removing node from to_visit list
	#print(current_node)
	#Now we have to return to Hub from current node. As we have visited all nodes
	#So, We have added this value with total distance
	total_distance = total_distance + dist[current_node][0]
	return total_distance	   

#first truck starts at 8:00 and float 8.00
val1 = deliver_package(truck1,dist,8) 
#second truck starts at 9:15 and float 9.25
val2 = deliver_package(truck2,dist,9.25) 

#third truck starts at 10:30 and float 10.5. Here first driver of truck 1 reached Hub
#and start Truck3
val3 = deliver_package(truck3,dist,10.5) 

print('\nMileage visited by truck 1: ',val1)
print('Mileage visited by truck 2: ',val2)
print('Mileage visited by truck 3: ',val3)

print('\nTotal Mileage Visited: ',val1+val2+val3)

print('\n')
print("{:<8} {:<10} {:<10} {:<10} {:<10}".format('PackID', 'Add_ID', 'Truck no', 'deadline','status'),'\t','Delivery Time')
for i in range(len(packageList)):
	hash_table.get_value(i).show_package() #show all packages with delivery time


#print(hash_table.get(11).show_package())
while True:
	print("\n\nType 'stop' to stop the program or Enter a time(Format HH:MM PM) to check status of all packages(Ex. 09:30 AM): ")
	var = input()
	if(var=='stop' or var=='Stop' or var=='STOP'):
		break
	h,mt= var.split(':')
	m,t= mt.split(' ')
	float_time = int(h) + int(m)/60
	if(t=='pm' or t =='PM' or t=='Pm' or t=='pM'):
		if float_time<12:
			float_time = float_time + 12
	#print(float_time)

	for i in range(40):
		expected_delivery_time = hash_table.get_value(i).deliveryTime # We have already counted and stored value in hash/object
		if (expected_delivery_time>float_time):
			#fixing delivery status based on specific time
			if (hash_table.get_value(i).truck_no == 1):
				if(float_time<8): #start time of truck 1: 8:00
					hash_table.get_value(i).delivered = 'at HUB'
					#hash_table.get_value(i).deliveryTime = ''
				else:
					hash_table.get_value(i).delivered = 'en route'
					#hash_table.get_value(i).deliveryTime = ''
			elif (hash_table.get_value(i).truck_no == 2):
				if(float_time<9.25): #start time of truck 2: 9:15
					hash_table.get_value(i).delivered = 'at HUB'
					#hash_table.get_value(i).deliveryTime = ''
				else:
					hash_table.get_value(i).delivered = 'en route'
					#hash_table.get_value(i).deliveryTime = ''
			elif (hash_table.get_value(i).truck_no == 3):
				if(float_time<10.5): #start time of truck 3: 10:30
					hash_table.get_value(i).delivered = 'at HUB'
					#hash_table.get_value(i).deliveryTime = ''
				else:
					hash_table.get_value(i).delivered = 'en route'

	#show all packages satus
	print("\nStaus of all packages:")
	print("{:<8} {:<10} {:<10} {:<10} {:<10}".format('PackID', 'Add_ID', 'Truck no', 'deadline','status'),'\t','Delivery Time/ Expected delivery time')
	for i in range(40):
		hash_table.get_value(i).show_package()

	#changing delivery status to 'Delivered' for showing currect values in next query
	for i in range(40):
		hash_table.get_value(i).delivered = 'Delivered'




