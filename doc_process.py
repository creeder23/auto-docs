import os.path
from gbdxtools import Interface
import json


def get_default(description):
    """Find the default value stated in the description.
      If there is no default value, return None.
    """
    ind1 = description.find('Default is')
    if ind1 == -1: return
    ind2 = description.find('.', ind1) # Find the first period.
    return description[ind1+len('Default is')+1:ind2]


wf_pass_list = ['pending', 'running']

fail_string = 'I failed, so no code for you'

markdown_template_file_name = 'DOCUMENT_TEMPLATE.md'

description_footer_text = 'This task can be run with Python using ' \
                          '[gbdxtools](https://github.com/DigitalGlobe/gbdxtools) or through the ' \
                          '[GBDX Web Application](https://gbdx.geobigdata.io/materials/)'

quickstart_header_test = 'Quick start example.'

advanced_header_test = 'Include example(s) with complicated parameter settings and/or example(s) where the task is ' \
                       'used as part of a workflow involving other GBDX tasks.'


inputs_header = 'The following table lists all taskname inputs.\n' \
                'Mandatory (optional) settings are listed as Required = True (Required = False).\n\n' \
                '  Name  |  Required  |  Default  |  Valid Values  |  Description  \n' \
                '--------|:----------:|-----------|----------------|---------------'

outputs_header = 'The following table lists all taskname outputs.\n' \
                 'Mandatory (optional) settings are listed as Required = True (Required = False).\n\n' \
                 '  Name  |  Required  |  Default  |  Valid Values  |  Description  \n' \
                 '--------|:----------:|-----------|----------------|---------------'


# Instantiating the GBDx Tools Interface
gbdx = Interface()

# Getting a list of known tasks on GBDx
known_tasks = gbdx.workflow.list_tasks()['tasks']

# This data object will contain the names of all of the tasks, the status of the tests,
# and the content for the markdown document.
# The associated files will be named exactly the same as the task name in this list.
list_of_tasks = [
                    {'name': 'AOP_ENVI_HDR'},
                    {'name': 'protogenV2RAV'}
                ]

# Loop through the list of tasks and mark whether the docs/code already exist
# Also, if the task has a quickstart or an advanced example, load that module so we can call the function
# to test that it passes
for i in list_of_tasks:

    i['markdown'] = False
    i['quickstart'] = False
    i['advanced'] = False
    i['knowntask'] = False

    i['markdown_file_name'] = '%s.md' % i['name']

    if i['name'] in known_tasks:
        i['knowntask'] = True

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


# For each task in the list, check to see if it is a valid task and hit the API and get the task details
for i in list_of_tasks:
    if i['knowntask'] is True:
        # retrieve task info and store it in the task data object
        task = gbdx.Task(i['name'])
        i['description'] = task.definition['description']
        i['input_ports'] = task.input_ports
        i['output_ports'] = task.output_ports


# For each task that has a quickstart or an advanced example, call the function and load the test results
for i in list_of_tasks:
    for j in ['quickstart', 'advanced']:
        if i[j] is True:

            # # We don't want to run these 100 times. This is just for testing.
            # i['%s_wfid' % j] = 1
            # i['%s_wfst' % j] = 'pending'
            # i['%s_pass' % j] = True

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

                with open(i['%s_file_name' % j]) as f:
                    s = f.read()

                start = s.index('runfunction():\n') + len('runfunction():\n')
                end = s.index('return', start)

                i['%s_text' % j] = s[start:end]

            else:

                i['%s_text' % j] = fail_string


# Now that we have all of the information, we can write it to the markdown file
# load template
for i in list_of_tasks:
    if i['knowntask'] is True:
        if i['markdown'] is True:
            with open(i['markdown_file_name']) as f:
                s = f.read()
        else:
            with open(markdown_template_file_name) as f:
                s = f.read()

        # Note that this will prepare the document with the correct task name on the first run as it will use the
        # template.
        # On subsequent runs, this will not be needed as the task name should not change.
        s = s.replace('taskname', i['name'])

        # This code will replace anything between the description and table of contents sections with the
        # description from the tasks API response.
        # Note the use of the footer, which is defined at the start of this code.
        if i['knowntask'] is True:
            start = s.index('### Description') + len('### Description')
            end = s.index('### Table of Contents', start)

            ins_str = '\n%s\n\n%s\n\n' % (i['description'], description_footer_text)

            s = s[:start] + ins_str + s[end:]

        # This code will replace anything between the Inputs and Outputs sections
        # Note the use of the header, which is defined at the start of this code.
        if i['knowntask'] is True:

            start = s.index('### Inputs') + len('### Inputs')
            end = s.index('### Outputs', start)

            port_strings = []
            for p in i['input_ports']:
                default = get_default(p['description'])
                if not default:
                    default = 'None'
                port_strings.append('|'.join([p['name'],
                                              str(p['required']),
                                              default,
                                              ' ',
                                              p['description']]))

            ins_str = '\n%s\n%s\n\n' % (inputs_header, '\n'.join(port_strings))

            s = s[:start] + ins_str + s[end:]

        # This code will replace anything between the Outputs and Output structure sections
        # Note the use of the header, which is defined at the start of this code.
        if i['knowntask'] is True:

            start = s.index('### Outputs') + len('### Outputs')
            end = s.index('**Output structure**', start)

            port_strings = []
            for p in i['output_ports']:
                default = get_default(p['description'])
                if not default:
                    default = 'None'
                port_strings.append('|'.join([p['name'],
                                              str(p['required']),
                                              default,
                                              ' ',
                                              p['description']]))

            ins_str = '\n%s\n%s\n\n' % (outputs_header, '\n'.join(port_strings))

            s = s[:start] + ins_str + s[end:]


        # This code will replace anything between the Quickstart and Inputs sections with the quickstart example code
        # Note the use of the header, which is defined at the start of this code.
        if i['quickstart'] is True:

            start = s.index('### Quickstart') + len('### Quickstart')
            end = s.index('### Inputs', start)

            ins_str = '\n%s\n\n%s\n%s\n%s\n\n' % (quickstart_header_test, "```python", i['quickstart_text'], "```")

            s = s[:start] + ins_str + s[end:]

        # This code will replace anything between the Advanced and Issues sections with the advanced example code
        # Note the use of the header, which is defined at the start of this code.
        if i['advanced'] is True:
            start = s.index('### Advanced') + len('### Advanced')
            end = s.index('### Issues', start)

            ins_str = '\n%s\n\n%s\n%s\n%s\n\n' % (advanced_header_test, "```python", i['advanced_text'], "```")

            s = s[:start] + ins_str + s[end:]

        # This code writes the modified contents to the new markdown file, replacing the old file if it is present.
        with open(i['markdown_file_name'], 'w') as f:
            f.write(s)


# TODO: We should either dump out some JSON here or create a report of what made and what failed
# and output that as a log file. For now, I'm just printing the data object.

print(json.dumps(list_of_tasks, sort_keys=False, indent=4))
