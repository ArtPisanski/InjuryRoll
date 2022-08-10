import discord
import random
import os
import pyclip
from discord.ext import commands
from replit import db

TOKEN = os.environ['TOKEN']

bot = commands.Bot(command_prefix='!')
# playerID = 0

@bot.event
async def on_ready():
    print('The bot has logged in as {0.user}'.format(bot))
  
@bot.command()
async def info(user):
  await user.send("Usage:\n`!roll [Player Name]`    - Rolls for injury \n\nInjury bot coded by @Arturo\n`Ver 1.2`")

@bot.command()
async def roll(user, *args):

  playername = ' '.join(args)
  type = random.randint(1,7)
  bodypart = 0
  sevStr = 'ERROR'
  bpStr = 'ERROR'
  days = 0

  print (str(user.author) + " initiated an injury roll..")
  
  if type == 1: # Head and Neck
    bodypart = random.randint(1,2)
    if bodypart == 1:
      bpStr = 'Whiplash'
      severity = random.randint(1,2)
      if severity == 1:
        sevStr = 'Minor'
        days = 1
      elif severity == 2:
        sevStr = 'Moderate'
        days = 2
    
    elif bodypart == 2:
      bpStr = 'Concussion'
      severity = random.randint(2,3)
      if severity == 2:
        sevStr = 'Moderate'
        days = 2
      elif severity == 3:
        sevStr = 'Severe'
        days = random.randint(3,4)
  
  elif type == 2: # Shoulder
    bodypart = random.randint(1,3)
    if bodypart == 1:
      bpStr = 'AC Joint Sprain'
      severity = random.randint(1,3)
      if severity == 1:
        sevStr = 'Minor'
        days = 1
      elif severity == 2:
        sevStr = 'Moderate'
        days = 4
      elif severity == 3:
        sevStr = 'Severe'
        days = random.randint(6,8)
    
    elif bodypart == 2:
      bpStr = 'Dislocated Shoulder'
      severity = random.randint(2,3)
      if severity == 1:
        sevStr = 'Minor'
        days = 1
      elif severity == 2:
        sevStr = 'Moderate'
        days = 4
      elif severity == 3:
        sevStr = 'Severe'
        days = random.randint(6,8)
    
    elif bodypart == 3:
      bpStr = 'Fractured Collar Bone'
      sevStr = 'Severe'
      days = random.randint(6,8)
  
  elif type == 3: # Elbow, Wrist, Hand
    bodypart = random.randint(1,3)
    if bodypart == 1:
      bpStr = 'Elbow Fracture'
      sevStr = 'Severe'
      days = random.randint(10,12)
    
    elif bodypart == 2:
      bpStr = 'Wrist Fracture'
      sevStr = 'Severe'
      days = random.randint(6,8)
    
    elif bodypart == 3:
      bpStr = 'Hand Fracture'
      severity = random.randint(2,3)
      if severity == 1:
        sevStr = 'Minor'
        days = 1
      elif severity == 2:
        sevStr = 'Moderate'
        days = random.randint(2,3)
      elif severity == 3:
        sevStr = 'Severe'
        days = random.randint(6,8)
  
  elif type == 4: # Lower Back
    bodypart = random.randint(1,2)
    if bodypart == 1:
      bpStr = 'Muscle Strain'
      severity = random.randint(1,3)
      if severity == 1:
        sevStr = 'Minor'
        days = 1
      elif severity == 2:
        sevStr = 'Moderate'
        days = random.randint(2,3)
      elif severity == 3:
        sevStr = 'Severe'
        days = random.randint(3,4)
    
    elif bodypart == 2:
      bpStr = 'Slipped Disc'
      severity = random.randint(1,3)
      if severity == 1:
        sevStr = 'Minor'
        days = random.randint(3,4)
      elif severity == 2:
        sevStr = 'Moderate'
        days = random.randint(4,6)
      elif severity == 3:
        sevStr = 'Severe'
        days = 8
  
  elif type == 5: # Hip and Groin
    bodypart = random.randint(1,3)
    if bodypart == 1:
      bpStr = 'Abdominal Strain'
      severity = random.randint(1,3)
      if severity == 1:
        sevStr = 'Minor'
        days = random.randint(1,2)
      elif severity == 2:
        sevStr = 'Moderate'
        days = random.randint(3,5)
      elif severity == 3:
        sevStr = 'Severe'
        days = random.randint(6,8)
    
    elif bodypart == 2:
      bpStr = 'Groin Strain'
      severity = random.randint(1,3)
      if severity == 1:
        sevStr = 'Minor'
        days = random.randint(1,2)
      elif severity == 2:
        sevStr = 'Moderate'
        days = random.randint(3,5)
      elif severity == 3:
        sevStr = 'Severe'
        days = random.randint(6,8)
    
    elif bodypart == 3:
      bpStr = 'Hip Flexor Strain'
      severity = random.randint(1,3)
      if severity == 1:
        sevStr = 'Minor'
        days = random.randint(1,2)
      elif severity == 2:
        sevStr = 'Moderate'
        days = random.randint(3,5)
      elif severity == 3:
        sevStr = 'Severe'
        days = random.randint(6,8)
  
  elif type == 6: # Knee and Leg
    bodypart = random.randint(1,7)
    if bodypart == 1:
      bpStr = 'ACL'
      sevStr = 'Severe (Season Ending)'
      days = random.randint(24,32)
    
    elif bodypart == 2:
      bpStr = 'Calf Muscle Strain'
      severity = random.randint(1,3)
      if severity == 1:
        sevStr = 'Minor'
        days = random.randint(1,2)
      elif severity == 2:
        sevStr = 'Moderate'
        days = random.randint(3,5)
      elif severity == 3:
        sevStr = 'Severe'
        days = random.randint(6,8)
    
    elif bodypart == 3:
      bpStr = 'Cartilage Tear'
      severity = random.randint(1,3)
      if severity == 1:
        sevStr = 'Minor'
        days = random.randint(2,3)
      elif severity == 2:
        sevStr = 'Moderate'
        days = random.randint(4,6)
      elif severity == 3:
        sevStr = 'Severe'
        days = random.randint(8,16)

    elif bodypart == 4:
      bpStr = 'Hamstring Strain/Tear'
      severity = random.randint(1,3)
      if severity == 1:
        sevStr = 'Minor'
        days = random.randint(1,2)
      elif severity == 2:
        sevStr = 'Moderate'
        days = random.randint(3,6)
      elif severity == 3:
        sevStr = 'Severe'
        days = random.randint(8,16)
        
    elif bodypart == 5:
      bpStr = 'Thigh Strain'
      severity = random.randint(1,3)
      if severity == 1:
        sevStr = 'Minor'
        days = random.randint(1,2)
      elif severity == 2:
        sevStr = 'Moderate'
        days = random.randint(3,5)
      elif severity == 3:
        sevStr = 'Severe'
        days = random.randint(6,8)

    elif bodypart == 6:
      bpStr = 'PCL'
      severity = random.randint(1,3)
      if severity == 1:
        sevStr = 'Minor'
        days = random.randint(4,6)
      elif severity == 2:
        sevStr = 'Moderate'
        days = random.randint(6,8)
      elif severity == 3:
        sevStr = 'Severe'
        days = random.randint(12,16)

    elif bodypart == 7:
      bpStr = 'Tibia/Fibula Fracture'
      sevStr = 'Severe (Season Ending)'
      days = random.randint(24,32) 
        
  elif type == 7: # Ankle and Leg
    bodypart = random.randint(1,3)
    if bodypart == 1:
      bpStr = 'Ankle Sprain'
      severity = random.randint(1,3)
      if severity == 1:
        sevStr = 'Minor'
        days = random.randint(2,3)
      elif severity == 2:
        sevStr = 'Moderate'
        days = random.randint(4,6)
      elif severity == 3:
        sevStr = 'Severe'
        days = random.randint(6,8)
    
    elif bodypart == 2:
      bpStr = 'Calf Muscle Strain'
      severity = random.randint(1,3)
      if severity == 1:
        sevStr = 'Minor'
        days = random.randint(1,2)
      elif severity == 2:
        sevStr = 'Moderate'
        days = random.randint(3,5)
      elif severity == 3:
        sevStr = 'Severe'
        days = random.randint(6,8)

    elif bodypart == 3:
      bpStr = 'Fractured/Dislocated Ankle'
      sevStr = 'Severe (Season Ending)'
      days = random.randint(24,32)
      
  print (str(playername) + ": " + str(sevStr) + " " + str(bpStr))
  
  await user.send(f':ambulance: {playername} \n:clipboard: Subbed Out:\n:adhesive_bandage: {sevStr} {bpStr} \n:hourglass: Out for {days} matches \n:calendar: `gameweek` `match` \n:arrows_counterclockwise: `return date` \n`  `  `@manager`')
  
bot.run (TOKEN)