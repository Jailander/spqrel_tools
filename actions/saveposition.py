import qi
import argparse
import sys
import time
import threading
import json

import action_base
from action_base import *


actionName = "say"

def actionThread_exec (params):
    t = threading.currentThread()
    memory_service = getattr(t, "mem_serv", None)
    tts_service = getattr(t, "session", None).service("ALTextToSpeech")
    print "Action "+actionName+" started with params "+params
    # action init
    count = 1
    position_name = params
    # action init
    while (getattr(t, "do_run", True) and count>0): 
        print "Action "+actionName+" "+params+" exec..."
        # action exec
        count = count - 1
        print "saved" + position_name
        memory_service.insertData(position_name+"/coordinates",[car_x,car_y]) 
        # action exec
        time.sleep(0.1)

    print "Action "+actionName+" "+params+" terminated"
    # action end

    # action end
    memory_service.raiseEvent("PNP_action_result_"+actionName,"success");


def init(session):
    print actionName+" init"
    action_base.init(session, actionName, actionThread_exec)


def quit():
    print actionName+" quit"
    actionThread_exec.do_run = False



if __name__ == "__main__":

    app = action_base.initApp(actionName)
        
    init(app.session)

    #Program stays at this point until we stop it
    app.run()

    quit()


