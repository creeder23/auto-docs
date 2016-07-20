def runfunction():

    import os

    result = None

    result = 1+1

    print result
    print os.getcwd()

    return {'wfid': 1, 'wfst': 'pending'}

if __name__ == "__main__":
    runfunction()