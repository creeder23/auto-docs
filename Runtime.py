from datetime import datetime
import numpy as np

#def timedelta(starttime,endtime):
#    if starttime > endtime:
#        return endtime - starttime

def tasknamefromtaskhash(taskhash):
    splitname = taskhash.split('_')
    nametask = ''
    for s in splitname[:-1]:
        nametask += s+'_'
    nametask = nametask[:-1]
    return nametask

def getworkflow(events,taskname):
    isrunning = False
    iscomplete = False


    nametask = tasknamefromtaskhash(taskname)

    for event in events:
        print event
        if tasknamefromtaskhash(event["task"]) == nametask:
            print "***", event["state"]
            if not isrunning and event["state"] == "running":
                isrunning = True #starttime = event["timestamp"]
                starttime = np.datetime64(event["timestamp"])
            elif not iscomplete and event["state"] == "complete":
                iscomplete = True #endtime = event["timestamp"]
                endtime = np.datetime64(event["timestamp"])

                #return timedelta(starttime,endtime)
                return   (endtime - starttime) / np.timedelta64(1, 's')



'''
2016-09-07 17:23:15.204995

from datetime import datetime
import numpy as np
dt = datetime.utcnow()
dt
datetime.datetime(2012, 12, 4, 19, 51, 25, 362455)
dt64 = np.datetime64(dt)
ts = (dt64 - np.datetime64('1970-01-01T00:00:00Z')) / np.timedelta64(1, 's')
ts
1354650685.3624549
datetime.utcfromtimestamp(ts)
datetime.datetime(2012, 12, 4, 19, 51, 25, 362455)
np.__version__
'1.8.0.dev-7b75899'
'''
