from gbdxtools import Interface
gbdx = Interface()



#QB catIDs : 1010010004F8A100,101001000460B200
#data1 = ""
#data2 = ""

#WV1 catIDs : 102001001BB4F500, 1020010016585600

#data1 =
#data2 =

#WV2 catIDs : 1010010004F8A100,101001000460B200
data1 = ""
data2 = ""

#WV3 catIDs : 1010010004F8A100,101001000460B200
data1 = ""
data2 = ""

#GE catIDs : 1010010004F8A100,101001000460B200
data1 = ""
data2 = ""


aoptask1 = gbdx.Task("AOP_Strip_Processor", data=data1, enable_acomp=True, enable_pansharpen=False, enable_dra=False, bands='MS')
aoptask2 = gbdx.Task("AOP_Strip_Processor", data=data2, enable_acomp=True, enable_pansharpen=False, enable_dra=False, bands='MS')

#aoptask1 = gbdx.Task("AOP_Strip_Processor", data=data1, enable_acomp=True, enable_pansharpen=False, enable_dra=False, bands='PAN')
#aoptask2 = gbdx.Task("AOP_Strip_Processor", data=data2, enable_acomp=True, enable_pansharpen=False, enable_dra=False, bands='PAN')


envi_II = gbdx.Task("ENVI_ImageIntersection")
envi_II.inputs.file_types = "hdr"
envi_II.inputs.input_raster1 = envi_aoptask1.outputs.output_raster_uri.value
envi_II.inputs.input_raster2 = envi_aoptask2.outputs.output_raster_uri.value
envi_II.inputs.output_raster1_uri_filename = "NDVI1"
envi_II.inputs.output_raster2_uri_filename = ""

workflow = gbdx.Workflow([aoptask1, aoptask2, envi_II])


workflow.savedata(
    envi_ACTC.outputs.output_raster_uri,
        location='Benchmark/ENVI_CTC/NDVI_threshold'
)

workflow.execute()

status = workflow.status["state"]
wf_id = workflow.id
