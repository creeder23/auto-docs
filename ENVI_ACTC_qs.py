from gbdxtools import Interface
gbdx = Interface()

NDVI1 = "s3://gbd-customer-data/7d8cfdb6-13ee-4a2a-bf7e-0aff4795d927/Benchmark/ENVI_ImageIntersection/fromNDVI/TIFF/NDVI1/NDVI1.tif"
NDVI2 = "s3://gbd-customer-data/7d8cfdb6-13ee-4a2a-bf7e-0aff4795d927/Benchmark/ENVI_ImageIntersection/fromNDVI/TIFF/NDVI2/NDVI2.tif"

envi_IBD = gbdx.Task("ENVI_ImageBandDifference")
envi_IBD.inputs.file_types = "tif"
envi_IBD.inputs.input_raster1 = NDVI1
envi_IBD.inputs.input_raster2 = NDVI2

envi_ACTC = gbdx.Task("ENVI_AutoChangeThresholdClassification")
envi_ACTC.inputs.threshold_method = "Otsu"
envi_ACTC.inputs.file_types = "tif"
envi_ACTC.inputs.input_raster = envi_IBD.outputs.output_raster_uri.value


workflow = gbdx.Workflow([envi_IBD, envi_ACTC])

workflow.savedata(
    envi_IBD.outputs.output_raster_uri,
        location='Benchmark/ENVI_ACTC/IBD'
)


workflow.savedata(
    envi_ACTC.outputs.output_raster_uri,
        location='Benchmark/ENVI_ACTC/IDB/ACTC'
)

workflow.execute()

status = workflow.status["state"]
wf_id = workflow.id
