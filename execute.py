import requests
import json
import thingspeak

key='RJUI9PUKJTWMP7ZB'
talkback_id='52131'
turn_on='41161931'
turn_off='41161933'

def check(talkback_id,api_key):
    command_list = requests.get(f'https://api.thingspeak.com/talkbacks/{talkback_id}/commands.json?api_key={api_key}')
    return command_list

def execute(talkback_id,api_key,command_string):
    command_id = requests.post(f'https://api.thingspeak.com/talkbacks/{talkback_id}/commands',params={'api_key':api_key,'command_string':command_string})
    # form = requests.post(f'https://api.thingspeak.com/talkbacks/{talkback_id}/commands/execute.json',params={'api_key':api_key})
    # print(form.text)
    # details of executed command
    return command_id

def delete_command(talkback_id,api_key,command_id):
    requests.delete(f'https://api.thingspeak.com/talkbacks/{talkback_id}/commands/{command_id}.json',params={'api_key':api_key})

def delete_all_commands(talkback_id,api_key):
    command_list = json.loads(check(talkback_id,api_key).text)
    for command in command_list:
        c_id = command['id']
        delete_command(talkback_id,api_key,c_id)

# delete_all_commands(talkback_id,key)
#example:
#execute(talkback_id,key,'turn_on')

#PRABUSSY HELLO MAKE THIS FUNCTION EXECUTE WHEN USER CLICKS A BUTTON
#IF USER CLICKS AC ON THEN MAKE THE COMMAND STRRING "TURN_ON" AND IF HE CLICKS AC OFF MAKE IT "TURN OFF"