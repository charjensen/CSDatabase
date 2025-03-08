import pymongo
import pprint

from pymongo import MongoClient

client = MongoClient()

db = client.Performances

group1 = {"name": "g1", "numberMembers": "1", "costToBook": "1", "genre": "genre1"}
group2 = {"name": "g2", "numberMembers": "2", "costToBook": "2", "genre": "genre2"}
group3 = {"name": "g3", "numberMembers": "3", "costToBook": "3", "genre": "genre3"}
group4 = {"name": "g4", "numberMembers": "4", "costToBook": "4", "genre": "genre4"}
group5 = {"name": "g5", "numberMembers": "5", "costToBook": "5", "genre": "genre5"}

groups = db.Groups

group1id = groups.insert_one(group1).inserted_id
print("\nid returned from insert: " + str(group1id)) 
group2id = groups.insert_one(group2).inserted_id
print("\nid returned from insert: " + str(group2id))
group3id = groups.insert_one(group3).inserted_id
print("\nid returned from insert: " + str(group3id))
group4id = groups.insert_one(group4).inserted_id
print("\nid returned from insert: " + str(group4id))
group5id = groups.insert_one(group5).inserted_id
print("\nid returned from insert: " + str(group5id))

venues = db.Venue

venue1 = {"name": "v1", "city": "1", "seatingCapacity": "1"}
venue2 = {"name": "v2", "city": "2", "seatingCapacity": "2"}
venue3 = {"name": "v3", "city": "3", "seatingCapacity": "3"}

v1id = venues.insert_one(venue1).inserted_id
v2id = venues.insert_one(venue2).inserted_id
v3id = venues.insert_one(venue3).inserted_id

print("\nid returned from insert: " + str(v1id))
print("\nid returned from insert: " + str(v2id))
print("\nid returned from insert: " + str(v3id))

up = db.UpcomingPerformances

up1 = {"groupName": "n1", "venueName_and_date": ["venueName1", "date1"]}
up2 = {"groupName": "n2", "venueName_and_date": ["venueName2", "date2"]}
up3 = {"groupName": "n3", "venueName_and_date": ["venueName3", "date3"]}

upid1 = up.insert_one(up1).inserted_id
upid2 = up.insert_one(up2).inserted_id
upid3 = up.insert_one(up3).inserted_id

print("\nid returned from insert: " + str(upid1))
print("\nid returned from insert: " + str(upid2))
print("\nid returned from insert: " + str(upid3))

find1 = groups.find( {'name': {'$regex': 'v'}})
pprint.pprint(find1)
groups.delete_one({'name': 'v1'})
print("deleting v1")
pprint.pprint( {'name': 'v1'})
groups.delete_many({'name': {'$regex': 'v'}})
print("deleting a lot of vs")
for objs in groups.find():
    pprint.pprint(objs)