import discord
import random
import os
from discord.ext import commands

TOKEN = os.environ['TOKEN']

#variables
medic = 0
days = 0
goldEmoji = "<:Gold:1006939406130749470>"
silverEmoji = "<:Silver:1006939173070065844>"
bronzeEmoji = "<:Bronze:1006939431632117790>"

bot = commands.Bot(command_prefix='!')
# playerID = 0

@bot.event
async def on_ready():
    print('The bot has logged in as {0.user}'.format(bot))
  
@bot.command()
async def info(user):
  await user.send("Usage:\n`!roll [Player Name]`                - Rolls for injury \n`!rollSilver [Player Name]`   - Rolls a Silver Medic\n`!rollGold [Player Name]`       - Rolls a Gold Medic\n\nInjury bot coded by @Arturo (ver 1.84)")

@bot.command()
async def roll(user, *args):

  playername = ' '.join(args)

  await injuryRoll(user)
  await medicRoll(user, playername, 'Bronze')

@bot.command()
async def rollSilver(user, *args):

  playername = ' '.join(args)

  await injuryRoll(user)
  await medicRoll(user, playername, 'Silver')

@bot.command()
async def rollGold(user, *args):

  playername = ' '.join(args)

  await injuryRoll(user)
  await medicRoll(user, playername, 'Gold')

async def medicRoll(user, playername, medicType):
  global sevStr
  global bpStr
  global medic
  global days
  medic = 0

  if medicType == 'Bronze':
    if sevStr == 'Minor':
      medic = random.randint (1,4) # 25%
      if medic == 1:
        days = days - medic
      else:
        medic = 0
      print ("Medic Bonus: " + str(medic) + " (" + medicType + ")")
    await output(user, playername, sevStr, bpStr, bronzeEmoji, medic, days)

  elif medicType == 'Silver':
    if sevStr == 'Minor' or 'Moderate':
      medic = random.randint (1,8) # 25%
      if medic <= 2:
        days = days - medic
      else:
        medic = 0
      print ("Medic Bonus: " + str(medic) + " (" + medicType + ")")
    await output(user, playername, sevStr, bpStr, silverEmoji, medic, days)

  elif medicType == 'Gold':
    if sevStr == 'Minor' or 'Moderate':
      medic = random.randint (1,4) # 50%
      if medic <= 2:
        days = days - medic
      else:
        medic = 0
    elif sevStr == 'Severe' or 'Severe (Season Ending)':
      medic = random.randint (1,12) # 25%
      if medic <= 3:
        days = days - medic
      else:
        medic = 0
    print ("Medic Bonus: " + str(medic) + " (" + medicType + ")")

    await output(user, playername, sevStr, bpStr, goldEmoji, medic, days)
    
async def output(user, playername, sevStr, bpStr, emoji, medic, days):

  await user.send(f':ambulance: {playername} \n:clipboard: Subbed Out: \n:adhesive_bandage: {sevStr} {bpStr} \n{emoji} Medical Staff Bonus: {medic*-1} days \n:hourglass: Out for {days} matches \n:calendar: `gameweek` `match` \n:arrows_counterclockwise: `return date` \n`  ` `@manager`')

async def silverRoll():
  global sevStr
  global bpStr
  global medic
  global days
  
  if sevStr == 'Minor':
    bronze = random.randint (1,4)
    if bronze == 1:
      days = days - bronze
    else:
      bronze = 0

async def goldRoll():
  global sevStr
  global bpStr
  global medic
  global days
  
  if sevStr == 'Minor':
    bronze = random.randint (1,4)
    if bronze == 1:
      days = days - bronze
    else:
      bronze = 0

async def injuryRoll(user):

  print ("-----------------------------------------------")

  type = random.randint(1,7)
  severity = random.randint(1,5)
  global sevStr
  global bpStr
  global days
  
  if type == 1: # Head and Neck
    bodypart = random.randint(1,2)
    
    if bodypart == 1:
      bpStr = 'Whiplash'
      severity = random.randint(1,3)
      if severity <= 2:
        sevStr = 'Minor'
        days = 1
      elif severity == 3:
        sevStr = 'Moderate'
        days = 2
    
    elif bodypart == 2:
      bpStr = 'Concussion'
      severity = random.randint(1,5)
      if severity <= 4:
        sevStr = 'Moderate'
        days = 2
      elif severity == 5:
        sevStr = 'Severe'
        days = random.randint(3,4)
  
  elif type == 2: # Shoulder
    bodypart = random.randint(1,3)
    
    if bodypart == 1:
      bpStr = 'AC Joint Sprain'
      severity = random.randint(1,5)
      if severity <= 2:
        sevStr = 'Minor'
        days = 1
      elif severity <= 4:
        sevStr = 'Moderate'
        days = 4
      elif severity == 5:
        sevStr = 'Severe'
        days = random.randint(6,8)
    
    elif bodypart == 2:
      bpStr = 'Dislocated Shoulder'
      severity = random.randint(1,5)
      if severity <= 2:
        sevStr = 'Minor'
        days = 1
      elif severity <= 4:
        sevStr = 'Moderate'
        days = 4
      elif severity == 5:
        sevStr = 'Severe'
        days = random.randint(6,8)
    
    elif bodypart == 3:
      bpStr = 'Fractured Collar Bone'
      sevStr = 'Severe'
      days = random.randint(6,8)
  
  elif type == 3: # Elbow, Wrist, Hand
    bodypart = random.randint(1,4)
    
    if bodypart == 1:
      bpStr = 'Elbow Fracture'
      sevStr = 'Severe'
      days = random.randint(10,12)
    
    elif bodypart == 2:
      bpStr = 'Wrist Fracture'
      sevStr = 'Severe'
      days = random.randint(6,8)
    
    elif bodypart <= 4:
      bpStr = 'Hand Fracture'
      severity = random.randint(1,5)
      if severity <= 2:
        sevStr = 'Minor'
        days = 1
      elif severity <= 4:
        sevStr = 'Moderate'
        days = random.randint(2,3)
      elif severity == 5:
        sevStr = 'Severe'
        days = random.randint(6,8)
  
  elif type == 4: # Lower Back
    bodypart = random.randint(1,3)
    
    if bodypart <= 2:
      bpStr = 'Muscle Strain'
      severity = random.randint(1,5)
      if severity <= 2:
        sevStr = 'Minor'
        days = 1
      elif severity <= 4:
        sevStr = 'Moderate'
        days = random.randint(2,3)
      elif severity == 5:
        sevStr = 'Severe'
        days = random.randint(3,4)
    
    elif bodypart == 3:
      bpStr = 'Slipped Disc'
      severity = random.randint(1,5)
      if severity <= 2:
        sevStr = 'Minor'
        days = random.randint(3,4)
      elif severity <= 4:
        sevStr = 'Moderate'
        days = random.randint(4,6)
      elif severity == 5:
        sevStr = 'Severe'
        days = 8
  
  elif type == 5: # Hip and Groin
    bodypart = random.randint(1,3)
    
    if bodypart == 1:
      bpStr = 'Abdominal Strain'
      severity = random.randint(1,5)
      if severity <= 2:
        sevStr = 'Minor'
        days = random.randint(1,2)
      elif severity <= 4:
        sevStr = 'Moderate'
        days = random.randint(3,5)
      elif severity == 5:
        sevStr = 'Severe'
        days = random.randint(6,8)
    
    elif bodypart == 2:
      bpStr = 'Groin Strain'
      severity = random.randint(1,5)
      if severity <= 2:
        sevStr = 'Minor'
        days = random.randint(1,2)
      elif severity <= 4:
        sevStr = 'Moderate'
        days = random.randint(3,5)
      elif severity == 5:
        sevStr = 'Severe'
        days = random.randint(6,8)
    
    elif bodypart == 3:
      bpStr = 'Hip Flexor Strain'
      severity = random.randint(1,5)
      if severity <= 2:
        sevStr = 'Minor'
        days = random.randint(1,2)
      elif severity <= 4:
        sevStr = 'Moderate'
        days = random.randint(3,5)
      elif severity == 5:
        sevStr = 'Severe'
        days = random.randint(6,8)
  
  elif type == 6: # Knee and Leg
    bodypart = random.randint(1,10)
    
    if bodypart == 1:
      bpStr = 'ACL'
      sevStr = 'Severe (Season Ending)'
      days = random.randint(24,32)
    
    elif bodypart <= 3:
      bpStr = 'Calf Muscle Strain'
      severity = random.randint(1,5)
      if severity <= 2:
        sevStr = 'Minor'
        days = random.randint(1,2)
      elif severity <= 4:
        sevStr = 'Moderate'
        days = random.randint(3,5)
      elif severity == 5:
        sevStr = 'Severe'
        days = random.randint(6,8)
    
    elif bodypart == 4:
      bpStr = 'Cartilage Tear'
      severity = random.randint(1,5)
      if severity <= 2:
        sevStr = 'Minor'
        days = random.randint(2,3)
      elif severity <= 4:
        sevStr = 'Moderate'
        days = random.randint(4,6)
      elif severity == 5:
        sevStr = 'Severe'
        days = random.randint(8,16)

    elif bodypart == 5:
      bpStr = 'Hamstring Strain/Tear'
      severity = random.randint(1,5)
      if severity <= 2:
        sevStr = 'Minor'
        days = random.randint(1,2)
      elif severity <= 4:
        sevStr = 'Moderate'
        days = random.randint(3,6)
      elif severity == 5:
        sevStr = 'Severe'
        days = random.randint(8,16)
        
    elif bodypart <= 7:
      bpStr = 'Thigh Strain'
      severity = random.randint(1,5)
      if severity <= 2:
        sevStr = 'Minor'
        days = random.randint(1,2)
      elif severity <= 4:
        sevStr = 'Moderate'
        days = random.randint(3,5)
      elif severity == 5:
        sevStr = 'Severe'
        days = random.randint(6,8)

    elif bodypart <= 9:
      bpStr = 'PCL'
      severity = random.randint(1,5)
      if severity <= 2:
        sevStr = 'Minor'
        days = random.randint(4,6)
      elif severity <= 4:
        sevStr = 'Moderate'
        days = random.randint(6,8)
      elif severity == 5:
        sevStr = 'Severe'
        days = random.randint(12,16)

    elif bodypart == 10:
      bpStr = 'Tibia/Fibula Fracture'
      sevStr = 'Severe (Season Ending)'
      days = random.randint(24,32) 
        
  elif type == 7: # Ankle and Leg
    bodypart = random.randint(1,7)
    
    if bodypart <= 3:
      bpStr = 'Ankle Sprain'
      severity = random.randint(1,5)
      if severity <= 2:
        sevStr = 'Minor'
        days = random.randint(2,3)
      elif severity <= 4:
        sevStr = 'Moderate'
        days = random.randint(4,6)
      elif severity == 5:
        sevStr = 'Severe'
        days = random.randint(6,8)

    elif bodypart <= 6:
      bpStr = 'Calf Muscle Strain'
      severity = random.randint(1,5)
      if severity <= 2:
        sevStr = 'Minor'
        days = random.randint(1,2)
      elif severity <= 4:
        sevStr = 'Moderate'
        days = random.randint(3,5)
      elif severity == 5:
        sevStr = 'Severe'
        days = random.randint(6,8)
    
    elif bodypart == 7:
      bpStr = 'Fractured/Dislocated Ankle'
      sevStr = 'Severe (Season Ending)'
      days = random.randint(24,32)

  print (str(user.author) + " initiated an injury roll..")
  print ("Type: " + str(type) + ", Body Part: (" + str(bodypart) + ")" + bpStr + ", Severity: (" + str(severity) + ")" + sevStr + ", Days: " + str(days))
  
bot.run (TOKEN)