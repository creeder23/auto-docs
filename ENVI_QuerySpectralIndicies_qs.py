def runfunction():

    try:


# Quickstart **Example Script Run in Python using the gbdxTools InterfaceExample producing a single band vegetation mask from a tif file.
# First Initialize the Environment
        from gbdxtools import Interface
        gbdx = Interface()

        aop2envi = gbdx.Task("AOP_ENVI_HDR")
        aop2envi.inputs.image = 's3://gbd-customer-data/7d8cfdb6-13ee-4a2a-bf7e-0aff4795d927/ENVI/SI/AOP/055026839010_01/'

        envi_query = gbdx.Task("ENVI_QuerySpectralIndices")
        envi_query.inputs.input_raster = aop2envi.outputs.output_data.value
        envi_query.inputs.file_types = "hdr"

        workflow = gbdx.Workflow([aop2envi, envi_query])

        workflow.savedata(
	       envi_query.outputs.output_raster_uri,
	          location='Auto-docs/ENVI/SIS/Query'
        )

        workflow.execute()
        status = workflow.status["state"]
        wf_id = workflow.id

# print wf_id
# print status

    except:

        wf_id = 0
        status = 'failed'

    finally:

        return {'wfid': wf_id, 'wfst': status}


if __name__ == "__main__":
    runfunction()
