"""Synthesizes speech from the input string of text or ssml.

Note: ssml must be well-formed according to:
    https://www.w3.org/TR/speech-synthesis/
"""
from google.cloud import texttospeech
import os
import time


voices = ["en-AU-Standard-A","en-AU-Standard-B","en-AU-Standard-C","en-AU-Standard-D","en-AU-Wavenet-A","en-AU-Wavenet-B"
         ,"en-AU-Wavenet-C","en-AU-Wavenet-D","en-IN-Standard-A","en-IN-Standard-B","en-IN-Standard-C","en-IN-Wavenet-A"
         ,"en-IN-Wavenet-B","en-IN-Wavenet-C","en-GB-Standard-A","en-GB-Standard-B","en-GB-Standard-C","en-GB-Standard-D"
         ,"en-GB-Wavenet-A","en-GB-Wavenet-B","en-GB-Wavenet-C","en-GB-Wavenet-D","en-US-Standard-B","en-US-Standard-C"
         ,"en-US-Standard-D","en-US-Standard-E","en-US-Wavenet-A","en-US-Wavenet-B","en-US-Wavenet-C","en-US-Wavenet-D"
         ,"en-US-Wavenet-E","en-US-Wavenet-F"]

filenames = ["welcome","account_balance","voice_balance","recharge_offers","apply_offers","whatsapp_optin"]

SSML_COPIES = {
    "welcome" : """<speak>
Welcome to Best Tele Network!
<break time="200ms"/> 
<prosody rate="medium">
My name is Ravi, your virtual assistant.
<break strength="strong"/> 
Please describe your issue in a few words. 
<break strength="weak"/>
You can ask me questions related to slow network, account balance or recharge offers.
</prosody>
</speak>""",
    "account_balance":"""<speak>
<prosody volume="medium">
<emphasis level="moderate">Sure!</emphasis> 
</prosody>
<break time="200ms"/>
Are you enquiring about your remaining talktime<break time="100ms"/> 
<prosody rate="slow"><emphasis level="strong">or</emphasis></prosody> 
<break time="100ms"/>
<prosody level="fast">the data balance?</prosody>
</speak>""",
    "voice_balance":"""<speak>
<prosody rate="medium" volume="medium">Hang on</prosody>. 
<break time="300ms"/>
<prosody rate="medium">
Let me quickly check your talktime.
</prosody>
<break time="300ms"/>
<prosody rate="slow">
<emphasis level="strong">
So
</emphasis>
</prosody>
<break time="300ms"/>
<prosody rate="medium">
You have 18 minutes of talktime remaining. 
<break time="1s"/>
I've found a few recharge offers that work well for your usage. 
</prosody>
<break time="300ms"/>
<prosody rate="fast" volume="loud">Would you like to know more?</prosody>
</speak>""",
    "recharge_offers":"""<speak>
<emphasis level="moderate">Great!</emphasis>
<break time="200ms"/>
<prosody rate="medium">
So I took a look at your usage
</prosody>
<break time="200ms"/> 
<prosody rate="medium">
and
I think the 14 day package with unlimited calls at Rs 99 works best for you. 
</prosody>
<break time="1s"/>
Do you want to go ahead with this offer?
</speak>""",
    "apply_offers":"""<speak>
<prosody volume="loud">
<emphasis level="moderate">Sure</emphasis>
</prosody>
<break time="200ms"/>
<prosody rate="medium">
Would you like us to send
a payment link via WhatsApp?
</prosody>
</speak>""",
"whatsapp_optin":"""<speak>
<emphasis level="moderate">Cool!</emphasis>
<break time="200ms"/>
<emphasis level="strong">So...</emphasis>
<prosody rate="medium">
We have sent the payment link on Whatsapp.
</prosody>
<break time="300ms"/>
<prosody rate="medium">
Also you can reply on whatsapp directly for any further support. 
</prosody>
<break time="400ms"/>
<prosody rate="fast">Thank you for calling <break time="100ms"/>  and have a nice day!</prosody>
</speak>"""
}


# voice = "en-IN-Wavenet-C"
# filename = "whatsapp_optin"

# ssml = """
# <speak>
# <emphasis level="moderate">Cool!</emphasis>
# <break time="200ms"/>
# <emphasis level="strong">So...</emphasis>
# <prosody rate="medium">
# We have sent the payment link on Whatsapp.
# </prosody>
# <break time="300ms"/>
# <prosody rate="medium">
# Also you can reply on whatsapp directly for any further support. 
# </prosody>
# <break time="400ms"/>
# <prosody rate="fast">Thank you for calling <break time="100ms"/>  and have a nice day!</prosody>
# </speak>
# """

# Instantiates a client
client = texttospeech.TextToSpeechClient()

# # Set the text input to be synthesized
# synthesis_input = texttospeech.types.SynthesisInput(ssml=ssml)

# # Build the voice request, select the language code ("en-US") and the ssml
# # voice gender ("neutral")
# voice = texttospeech.types.VoiceSelectionParams(
#     language_code='en-US',
#     name= voice,
#     ssml_gender=texttospeech.enums.SsmlVoiceGender.FEMALE)

# # Select the type of audio file you want returned
# audio_config = texttospeech.types.AudioConfig(
#     audio_encoding=texttospeech.enums.AudioEncoding.MP3)

# # Perform the text-to-speech request on the text input with the selected
# # voice parameters and audio file type
# response = client.synthesize_speech(synthesis_input, voice, audio_config)

# # voices = client.list_voices()
# # print(voices)

# # The response's audio_content is binary.
# with open('./outputs/en-IN-Wavenet-C/'+ filename+'.mp3', 'wb') as out:
#     # Write the response to the output file.
#     out.write(response.audio_content)
#     print('Audio content written to file')


for voice in voices:
    path = os.path.join(os.getcwd(),"outputs","generated",voice)
    #create the folders
    if not os.path.exists(path):
        os.makedirs(path)

    # generate the synthesized speech
    for filename in filenames:
        ssml_copy = SSML_COPIES[filename]

        # Set the text input to be synthesized
        synthesis_input = texttospeech.types.SynthesisInput(ssml=ssml_copy)

        # # Build the voice request, select the language code ("en-US") and the ssml
        # # voice gender ("neutral")
        voice_out = texttospeech.types.VoiceSelectionParams(
            language_code='en-US',
            name= voice)

        # Select the type of audio file you want returned
        audio_config = texttospeech.types.AudioConfig(
            audio_encoding=texttospeech.enums.AudioEncoding.MP3)

        # Perform the text-to-speech request on the text input with the selected
        # voice parameters and audio file type
        response = client.synthesize_speech(synthesis_input, voice_out, audio_config)

        # The response's audio_content is binary.
        with open(path+ '/' +filename+'.mp3', 'wb') as out:
            # Write the response to the output file.
            out.write(response.audio_content)
    print('Audio contents written to files for ' + path)
    time.sleep(5)

            

            


