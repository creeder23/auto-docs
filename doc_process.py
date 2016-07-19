import os
import doctest

list_of_tasks = ['task_name']

for i in list_of_tasks:
    doctest.testfile(os.path.join(os.getcwd(), 'i'+'.txt'))


# Get a list of all task names
#
# For each task name
#
# run the doctext
#
# check the results
#
# If good
#
# determine of the md files exists
#
# if not create the md file from the template
#
# Open the md file
#
# run the api data collect
#
# populate the md file from the API
#
# populate the md file from the code

# Code will check on whether GBDx tools completes, a running workflow is a win, but we need to retain all of the workflow IDs to ensure that the long running tasks complete.
