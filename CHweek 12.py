#Create an empty list of services using Python
my_awslist= []

#Populate the list of AWS Service Inventory
my_awslist.append('Simple Notification Service')
my_awslist.append('API Gateway')
my_awslist.append('CloudWatch')
my_awslist.append('Lambda')
my_awslist.append('EC2')
my_awslist.append('S3')
my_awslist.append('DynamoDB')

#Print the list and the length of the list.
print("7 Functions in my AWS Service Inventory")
print(len(my_awslist))
 
#Remove two specific services from the list by name or by index
del my_awslist[0]
del my_awslist[-2]

#Print new list and the new length of the list.
print(my_awslist)
print("5 Functions in my AWS Service Inventory")
print(len(my_awslist))
