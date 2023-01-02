import json
import time

import io
import os
from _datetime import datetime;

from pyVAD_utils import pyVAD
from GoogleSpeechAPI import GoogleSpeech
from gpt3_chat_utils import ask , append_interaction_to_chat_log , chat_log

# The file we keep all our conversations in during this chat session
thenow = datetime.now().strftime("%Y%m%d%H%M%S")
sessionFileName = "session_data_" + thenow + ".txt"

print('-------------------------------- Say something -----------------------------------')

if __name__ == '__main__':

    #--- Steves google speech wrapper
    speech = GoogleSpeech()

    #--- Steve etl VAD class    
    pyVAD = pyVAD()

    for wav_data in pyVAD.wave_loop():
        
        #--- Send to Google and get speech to text 
        converted_text = speech.SpeechToText(wav_data)
        #debug
        print('Googles response ',converted_text)

        #--- Noise sometimes comes back, so speech lib returns "Nothing" 
        if not converted_text == 'Nothing':
        
            answer = ask(converted_text, chat_log)
            chat_log = append_interaction_to_chat_log(converted_text, answer, chat_log)

            print(chat_log)

            
        
        #Write out this sessions bot data along with google response for later re-learning
        #session_data = aimlKernel.getSessionData()
    
        #f = io.open(sessionFileName, 'w+')
        #f.write("------------------------------------------------")
        #f.write("Google Said {0}".format(converted_text))
        #f.write("Aiml   Said {0}".format(aiml_response))
        #f.write(str(session_data))
        #f.write("------------------------------------------------")
        #f.close()


