import os
import subprocess

# generate playlists
order_of_play = [
                    "input/ring.mp3",
                    "output/welcome.mp3",
                    "input/account_balance.mp3",
                    "input/silence.mp3",
                    "output/account_balance.mp3",
                    "input/talktime.mp3",
                    "input/silence.mp3",
                    "output/voice_balance.mp3",
                    "input/recharge_offers.mp3",
                    "input/silence.mp3",
                    "output/recharge_offers.mp3",
                    "input/apply_offers.mp3",
                    "input/silence.mp3",
                    "output/apply_offers.mp3",
                    "input/whatsapp_optin.mp3",
                    "input/silence.mp3",
                    "output/whatsapp_optin.mp3"]

voices = ["en-AU-Standard-A","en-AU-Standard-B","en-AU-Standard-C","en-AU-Standard-D","en-AU-Wavenet-A","en-AU-Wavenet-B"
         ,"en-AU-Wavenet-C","en-AU-Wavenet-D","en-IN-Standard-A","en-IN-Standard-B","en-IN-Standard-C","en-IN-Wavenet-A"
         ,"en-IN-Wavenet-B","en-IN-Wavenet-C","en-GB-Standard-A","en-GB-Standard-B","en-GB-Standard-C","en-GB-Standard-D"
         ,"en-GB-Wavenet-A","en-GB-Wavenet-B","en-GB-Wavenet-C","en-GB-Wavenet-D","en-US-Standard-B","en-US-Standard-C"
         ,"en-US-Standard-D","en-US-Standard-E","en-US-Wavenet-A","en-US-Wavenet-B","en-US-Wavenet-C","en-US-Wavenet-D"
         ,"en-US-Wavenet-E","en-US-Wavenet-F"]


for voice in voices:
    sox_playlist = []
    for item in order_of_play:
        if 'input/' in item:
            item = item.replace("input/","/Users/hap-156/Documents/haptik/ivr/tts/inputs/")
            sox_playlist.append(item)
        elif 'output/' in item:
            item = item.replace("output/","/Users/hap-156/Documents/haptik/ivr/tts/outputs/generated/"+voice+"/")
            sox_playlist.append(item)
    subprocess.call(['sox'] + sox_playlist + ['/Users/hap-156/Documents/haptik/ivr/tts/playlists/'+voice+'.mp3'])
    


# import subprocess
# sound_output_path = "/tmp"
# sox_filenames = ['/Users/hap-156/Documents/haptik/ivr/tts/outputs/en-IN-Wavenet-C/test.mp3', '/Users/hap-156/Documents/haptik/ivr/tts/outputs/en-IN-Wavenet-C/test.mp3']
# subprocess.call(['sox'] + sox_filenames + ['out.mp3'])