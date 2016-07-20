
from gbdxtools import Interface


def get_default(description):
   """Find the default value stated in the description.
      If there is no default value, return None.
   """
   ind1 = description.find('Default is')
   if ind1 == -1: return
   ind2 = description.find('.', ind1)               # Find the first period.
   return description[ind1+len('Default is')+1:ind2]

gbdx = Interface()
task_names = gbdx.workflow.list_tasks()['tasks']

# load template
with open('DOCUMENT_TEMPLATE.md') as f:
   template = f.read()

for name in task_names:

   # retrieve task info
   task = gbdx.Task(name)
   description = task.definition['description']
   input_ports, output_ports = task.input_ports, task.output_ports

   # fill in template
   this_template = template
   this_template = this_template.replace('taskname', name)
   this_template = this_template.replace('Task description.', description)
   port_strings = []
   for p in input_ports + output_ports:
       default = get_default(p['description'])
       if not default:
           default = 'None'
       port_strings.append('|'.join( [ p['name'],
                                       str(p['required']),
                                       default,
                                       ' ',
                                       p['description']] ))
   this_template = this_template.replace('inputshere',
                                         '\n'.join(port_strings[:len(input_ports)]) )
   this_template = this_template.replace('outputshere',
                                         '\n'.join(port_strings[len(input_ports):]) )

   with open(name + '.md', 'w') as f:
       f.write(this_template)