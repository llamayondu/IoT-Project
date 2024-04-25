import requests
import thingspeak

key='RJUI9PUKJTWMP7ZB'
talkback_id='52131'
turn_on='41161931'
turn_off='41161933'

def execute(talkback_id,api_key,command_string):
    command_id = requests.post('https://api.thingspeak.com/talkbacks/52131/commands',params={'api_key':'RJUI9PUKJTWMP7ZB','command_string':command_string})
    # form = requests.post(f'https://api.thingspeak.com/talkbacks/{talkback_id}/commands/execute.json',params={'api_key':api_key})
    # print(form.text)
    # details of executed command

#example:
#execute(talkback_id,key,'turn_on')

#PRABUSSY HELLO MAKE THIS FUNCTION EXECUTE WHEN USER CLICKS A BUTTON
#IF USER CLICKS AC ON THEN MAKE THE COMMAND STRRING "TURN_ON" AND IF HE CLICKS AC OFF MAKE IT "TURN OFF"