# Quickstart **Example Script Run in Python using the gbdxTools InterfaceExample producing a single band vegetation mask from a tif file.
# First Initialize the Environment

def imafunction():
    from gbdxtools import Interface
    gbdx = Interface()
    status = None
    aop2envi = gbdx.Task("AOP_ENVI_HDR")
    aop2envi.inputs.image = 's3://gbd-customer-data/7d8cfdb6-13ee-4a2a-bf7e-0aff4795d927/ENVI/SI/AOP/055026839010_01/'
    
    workflow = gbdx.Workflow([ aop2envi ])
    workflow.savedata(
       aop2envi.outputs.output_data,
       location='Doctest/hdr/test2'
    )
    workflow.execute()
    
    status = workflow.status["state"] 
    print status
    return {'wfid': 1, 'wfst': '2'}
    
    	
if __name__ == "__main__":
    imafunction()
