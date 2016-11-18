def runfunction():

    try:


# Quickstart **Example Script Run in Python using the gbdxTools InterfaceExample producing a single band vegetation mask from a tif file.
# First Initialize the Environment
        from gbdxtools import Interface
        gbdx = Interface()

        #Insert correct path to image in S3 location
        data1 = "s3://receiving-dgcs-tdgplatform-com/055438828010_01_003"
        data2 = "s3://receiving-dgcs-tdgplatform-com/055690224010_01_003"

        aoptask1 = gbdx.Task("AOP_Strip_Processor", data=data1, enable_acomp=True, enable_pansharpen=False, enable_dra=False, bands='MS')
        aoptask2 = gbdx.Task("AOP_Strip_Processor", data=data2, enable_acomp=True, enable_pansharpen=False, enable_dra=False, bands='MS')

        # Capture AOP task outputs
        #orthoed_output = aoptask.get_output('data')

        envi_ndvi1 = gbdx.Task("ENVI_SpectralIndex")
        envi_ndvi1.inputs.input_raster = aoptask1.outputs.data.value
        envi_ndvi1.inputs.file_types = "hdr"
        envi_ndvi1.inputs.index = "Normalized Difference Vegetation Index"

        envi_ndvi2 = gbdx.Task("ENVI_SpectralIndex")
        envi_ndvi2.inputs.input_raster = aoptask2.outputs.data.value
        envi_ndvi2.inputs.file_types = "hdr"
        envi_ndvi2.inputs.index = "Normalized Difference Vegetation Index"

        envi_II = gbdx.Task("ENVI_ImageIntersection")
        envi_II.inputs.file_types = "hdr"
        envi_II.inputs.input_raster1 = envi_ndvi1.outputs.output_raster_uri.value
        envi_II.inputs.input_raster2 = envi_ndvi2.outputs.output_raster_uri.value
        envi_II.inputs.output_raster1_uri_filename = "NDVI1"
        envi_II.inputs.output_raster2_uri_filename = "NDVI2"
        #envi_II.outputs.output_raster1_uri = "s3://gbd-customer-data/7d8cfdb6-13ee-4a2a-bf7e-0aff4795d927/Benchmark/ENVI_ImageIntersection/fromNDVI1"
        #envi_II.outputs.output_raster2_uri = "s3://gbd-customer-data/7d8cfdb6-13ee-4a2a-bf7e-0aff4795d927/Benchmark/ENVI_ImageIntersection/fromNDVI2"

        envi_IBD = gbdx.Task("ENVI_ImageBandDifference")
        envi_IBD.inputs.file_types = "hdr"
        envi_IBD.inputs.input_raster1 = envi_II.outputs.output_raster1_uri.value
        envi_IBD.inputs.input_raster2 = envi_II.outputs.output_raster2_uri.value

        envi_ACTC = gbdx.Task("ENVI_ChangeThresholdClassification")
        envi_CTC.inputs.increase_threshold = 0.1
        envi_CTC.inputs.decrease_threshold = 0.5
        envi_CTC.inputs.file_types = "hdr"
        envi_CTC.inputs.input_raster = envi_IBD.outputs.output_raster_uri.value


        workflow = gbdx.Workflow([aoptask1, aoptask2, envi_ndvi1, envi_ndvi2, envi_II, envi_IBD, envi_CTC])

        workflow.savedata(
            envi_II.outputs.output_raster1_uri,
                location='Benchmark/ENVI_ImageIntersection/fromNDVI'
        )

        workflow.savedata(
            envi_II.outputs.output_raster2_uri,
                location='Benchmark/ENVI_ImageIntersection/fromNDVI'
        )

        workflow.savedata(
            envi_ACTC.outputs.output_raster_uri,
                location='Benchmark/ENVI_CTC/NDVI_threshold'
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
