

def getworkflow(events,taskname):
    isrunning = False
    iscomplete = False

    for event in events:
        if event["task"] == taskname:
            if not isrunning and event["state"] == "running":
                isrunning = True #starttime = event["timestamp"]
                starttime = event["timestamp"]
            elif not iscomplete and event["state"] == "complete":
                iscomplete = True #endtime = event["timestamp"]
                endtime = event["timestamp"]
