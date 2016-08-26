def runfunction():

    try:


# Quickstart **Example Script Run in Python using the gbdxTools InterfaceExample producing a single band vegetation mask from a tif file.
# First Initialize the Environment
        from gbdxtools import Interface
        gbdx = Interface()

        data = "s3://receiving-dgcs-tdgplatform-com/055026839010_01_003"
        aoptask = gbdx.Task('AOP_Strip_Processor', data=data, bands='MS', enable_acomp=True, enable_pansharpen=False, enable_dra=False)     # creates acomp'd multispectral image

        aop2envi = gbdx.Task("AOP_ENVI_HDR")
        aop2envi.inputs.image = aoptask.outputs.data.value

        envi_ndvi = gbdx.Task("ENVI_SpectralIndices")
        envi_ndvi.inputs.input_raster = aop2envi.outputs.output_data.value
        envi_ndvi.inputs.file_types = "hdr"

# Specify a string/list of indicies to run on the input_raster variable.  The order of indicies wi
        envi_ndvi.inputs.index = '["Normalized Difference Vegetation Index", "WorldView Built-Up Index", "WorldView Non-Homogeneous Feature Difference", "WorldView Water Index", "WorldView Soil Index"]'
        workflow = gbdx.Workflow([aoptask, aop2envi, envi_ndvi])
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
