# This works
# import task_name
# task_name.imafunction()

# This also works
# module_obj = __import__('task_name')
# globals()['task_name'] = module_obj
# task_name.imafunction()


import os.path
from gbdxtools import Interface
import json



wf_pass_list = ['pending', 'running']
fail_string = 'I failed, so no code for you'

# TODO: Should there be an example that pulls the complete task list somehow?
# This list will contain the names of all of the tasks.
# The associated files will be named exactly the same as the task name in this list.
list_of_tasks = [
                    {'name': 'task_name'},
                    {'name': 'task_name_2'}
                ]

# Loop through the list of tasks and mark whether the docs/code already exist
# Also, if the task has a quickstart or an advanced example, load that module so we can call the function
# to test that it passes
for i in list_of_tasks:

    i['markdown'] = False
    i['quickstart'] = False
    i['advanced'] = False

    if os.path.isfile('%s.md' % i['name']) is True:
        i['markdown'] = True

    if os.path.isfile('%s_qs.py' % i['name']) is True:
        i['quickstart'] = True
        i['quickstart_name'] = '%s_qs' % i['name']
        i['quickstart_file_name'] = '%s_qs.py' % i['name']
        i['quickstart_pass'] = False
        module_obj = __import__(i['quickstart_name'])
        globals()[i['quickstart_name']] = module_obj

    if os.path.isfile('%s_adv.py' % i['name']) is True:
        i['advanced'] = True
        i['advanced_name'] = '%s_adv' % i['name']
        i['advanced_file_name'] = '%s_adv.py' % i['name']
        i['advanced_pass'] = False
        module_obj = __import__(i['advanced_name'])
        globals()[i['advanced_name']] = module_obj


# For each task in the list, hit the API and get their task description
gbdx = Interface()

for i in list_of_tasks:

    name = i['name']

    # retrieve task info
    task = gbdx.Task(name)
    i['description'] = task.definition['description']
    i['input_ports'] = task.input_ports
    i['output_ports'] = task.output_ports

    # # fill in template
    # this_template = template
    # this_template = this_template.replace('taskname', name)
    # this_template = this_template.replace('Task description.', description)
    # port_strings = []
    # for p in input_ports + output_ports:
    #    default = get_default(p['description'])
    #    if not default:
    #        default = 'None'
    #    port_strings.append('|'.join( [ p['name'],
    #                                    str(p['required']),
    #                                    default,
    #                                    ' ',
    #                                    p['description']] ))
    # this_template = this_template.replace('inputshere',
    #                                      '\n'.join(port_strings[:len(input_ports)]) )
    # this_template = this_template.replace('outputshere',
    #                                      '\n'.join(port_strings[len(input_ports):]) )





# For each task that has a quickstart or an advanced example, call the function and load the test results
for i in list_of_tasks:
    for j in ['quickstart', 'advanced']:
        if i[j] is True:
            # Run the function to test the example code
            r = globals()[i['%s_name' % j]].runfunction()

            # Store the workflow id in case we want to run a long running test (did the workflow actually finish)
            i['%s_wfid' % j] = r['wfid']

            # Get the status and check against the list of possible passing values
            i['%s_wfst' % j] = r['wfst']
            if i['%s_wfst' % j] in wf_pass_list:
                i['%s_pass' % j] = True


# For each task that has example code and passes the test, read in the example code and store for inclusion in the
# markdown document

for i in list_of_tasks:
    for j in ['quickstart', 'advanced']:
        if i[j] is True:
            if i['%s_pass' % j] is True:

                f = open(i['%s_file_name' % j], 'r')
                s = f.read()
                f.close()

                start = s.index('runfunction():\n') + len('runfunction():\n')
                end = s.index('return', start)

                i['%s_text' % j] = s[start:end]

            else:

                i['%s_text' % j] = fail_string




print(json.dumps(list_of_tasks, sort_keys=True, indent=4))








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
