def runfunction():

    try:


# Quickstart **Example Script Run in Python using the gbdxTools InterfaceExample producing a single band vegetation mask from a tif file.
# First Initialize the Environment
        from gbdxtools import Interface
        gbdx = Interface()

        ndvi1
        ndvi2

        ENVI_ACTC = gbdx.Task("ENVI_AutoChangeThresholdClassification")
        ENVI_ACTC.inputs.input_raster = 's3://gbd-customer-data/7d8cfdb6-13ee-4a2a-bf7e-0aff4795d927/Benchmark/ENVI_ACTC/055438828010_01/'
        ENVI_ACTC.inputs.input_raster = 's3://gbd-customer-data/7d8cfdb6-13ee-4a2a-bf7e-0aff4795d927/Benchmark/ENVI_ACTC/055690224010_01/'


# Specify a string/list of indicies to run on the input_raster variable.  The order of indicies wi
        envi_ndvi.inputs.index = '["Normalized Difference Vegetation Index", "WorldView Soil Index"]'

        workflow = gbdx.Workflow([aop2envi, envi_ndvi])
        workflow.savedata(
	       aop2envi.outputs.output_data,
	          location='Auto-docs/ENVI/SIS'
        )

        workflow.savedata(
	       envi_ndvi.outputs.output_raster_uri,
	          location='Auto-docs/ENVI/SIS'
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
