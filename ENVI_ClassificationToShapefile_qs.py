def runfunction():

    try:


# Quickstart **Example Script Run in Python using the gbdxTools InterfaceExample producing a single band vegetation mask from a tif file.
# First Initialize the Environment
    from gbdxtools import Interface
    gbdx = Interface()

    isodata = gbdx.Task("ENVI_ISODATAClassification")
    isodata.inputs.input_raster = "s3://gbd-customer-data/7d8cfdb6-13ee-4a2a-bf7e-0aff4795d927/Benchmark/WV2/054876618060_01/"
    isodata.inputs.file_types = "tif"

    shp = gbdx.Task("ENVI_ClassificationToShapefile")
    shp.inputs.input_raster = isodata.outputs.output_raster_uri.value
    shp.inputs.file_types = "hdr"

    workflow = gbdx.Workflow([isodata, shp])

    workflow.savedata(
        isodata.outputs.output_raster_uri,
        location="Benchmark/classification/isodata"
        )

        workflow.savedata(
        shp.outputs.output_vector_uri,
        location="Benchmark/classification/shp"
        )


# print wf_id
# print status

    except:

        wf_id = 0
        status = 'failed'

    finally:

        return {'wfid': wf_id, 'wfst': status}


if __name__ == "__main__":
    runfunction()
