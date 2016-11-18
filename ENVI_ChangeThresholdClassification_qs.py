def runfunction():

    try:


# Quickstart **Example Script Run in Python using the gbdxTools InterfaceExample producing a single band vegetation mask from a tif file.
# First Initialize the Environment
        from gbdxtools import Interface
        gbdx = Interface()

        #Insert correct path to image in S3 location
        NDVI1 = "s3://gbd-customer-data/7d8cfdb6-13ee-4a2a-bf7e-0aff4795d927/Benchmark/ENVI_ImageIntersection/fromNDVI/TIFF/NDVI1/NDVI1.tif"
        NDVI2 = "s3://gbd-customer-data/7d8cfdb6-13ee-4a2a-bf7e-0aff4795d927/Benchmark/ENVI_ImageIntersection/fromNDVI/TIFF/NDVI2/NDVI2.tif"

        envi_IBD = gbdx.Task("ENVI_ImageBandDifference")
        envi_IBD.inputs.file_types = "tif"
        envi_IBD.inputs.input_raster1 = NDVI1
        envi_IBD.inputs.input_raster2 = NDVI2

        envi_CTC = gbdx.Task("ENVI_ChangeThresholdClassification")
        envi_CTC.inputs.increase_threshold = "0.1"
        envi_CTC.inputs.decrease_threshold = "0.5"
        envi_CTC.inputs.file_types = "hdr"
        envi_CTC.inputs.input_raster = envi_IBD.outputs.output_raster_uri.value

        workflow = gbdx.Workflow([envi_IBD, envi_CTC])

        workflow.savedata(
            envi_IBD.outputs.output_raster_uri,
                location='Benchmark/ENVI_CTC/IBD'
        )

        workflow.savedata(
            envi_CTC.outputs.output_raster_uri,
                location='Benchmark/ENVI_CTC/IDB/CTC'
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
