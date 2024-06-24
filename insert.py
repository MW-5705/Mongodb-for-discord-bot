import discord
from discord.ext import commands
from connection import client

#create database:
db = client["Discord"]
#create table/collection
participants = db["Participants"]
# to data is inserted in form of dictionaries {key:value} where key is field name and value is the value for that field
# for one data/document entry
# participants.insert_one(dictionary)
# for multiple entries
# participants.insert_many(list of dictionaries)

#sample
participants_data = [{"discordid":1136647569745920020,"department":"tech"},{"discordid": 736468011501879388, "department": "HR"},{"discordid": 159985870458322944, "department": "HR"},{"discordid": 1250348605735305248, "department": "Sales"},{"discordid": 719836080110829580, "department": "Sales"}, {"discordid":783708073390112830, "department": "IT"},{"discordid":1145363441524166758, "department": "HR"},{"discordid":1252507951722270731, "department": "tech"},{"discordid":1144326358445609020, "department": "Sales"},{"discordid":1116950361664671825, "department":"tech"},{"discordid": 668075833780469772, "department": "Sales"}, {"discordid":512597152766099478, "department": "tech"}]
participants.insert_many(participants_data)