def runfunction():

    try:


# Quickstart **Example Script Run in Python using the gbdxTools InterfaceExample producing a single band vegetation mask from a tif file.
# First Initialize the Environment
        from gbdxtools import Interface
        gbdx = Interface()

        shptask = gbdx.Task("ENVI_ClassificationToShapefile")
        data = ' s3://gbd-customer-data/7d8cfdb6-13ee-4a2a-bf7e-0aff4795d927/ENVI/classification/classification_name.hdr'

        shptask.inputs.input_raster = data
        shptask.inputs.file_types = "hdr"

        workflow = gbdx.Workflow([shptask])

        workflow.savedata(
	       shptask.outputs.output_vector_uri,
	          location='Auto-docs/ENVI/SHP'
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
