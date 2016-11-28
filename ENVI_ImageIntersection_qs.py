def runfunction():
    try:
# First Initialize the Environment
        from gbdxtools import Interface
        gbdx = Interface()


        #QB catIDs : 1010010004F8A100,101001000460B200
        data1 = "s3://receiving-dgcs-tdgplatform-com/055664619010_01_003"
        data2 = "s3://receiving-dgcs-tdgplatform-com/055668601010_01_003"

        '''
        #WV1 catIDs : 102001001BB4F500, 1020010016585600
        #data1 = 's3://receiving-dgcs-tdgplatform-com/055940816010_01_003'
        #data2 = 's3://receiving-dgcs-tdgplatform-com/055940817010_01_003'

        #WV2 catIDs : 1030050043F8B400,104001001D66F800
        data1 = "s3://receiving-dgcs-tdgplatform-com/055690224010_01_003"
        data2 = "s3://receiving-dgcs-tdgplatform-com/055438828010_01_003"

        #WV3 catIDs : 1040010002965B00,10400E0001DBBA00
        data1 = ""
        data2 = "s3://receiving-dgcs-tdgplatform-com/055436253010_01_003"

        #GE catIDs : 1050410003F75A00,1050410003F7AF00
        data1 = "s3://receiving-dgcs-tdgplatform-com/055917898010_01_003"
        data2 = "s3://receiving-dgcs-tdgplatform-com/055917899010_01_003"
        '''

        #aoptask1 = gbdx.Task("AOP_Strip_Processor", data=data1, enable_acomp=True, enable_pansharpen=False, enable_dra=False, bands='MS')
        #aoptask2 = gbdx.Task("AOP_Strip_Processor", data=data2, enable_acomp=True, enable_pansharpen=False, enable_dra=False, bands='MS')

        #aoptask1 = gbdx.Task("AOP_Strip_Processor", data=data1, enable_acomp=True, enable_pansharpen=False, enable_dra=False, bands='PAN')
        #aoptask2 = gbdx.Task("AOP_Strip_Processor", data=data2, enable_acomp=True, enable_pansharpen=False, enable_dra=False, bands='PAN')


        envi_II = gbdx.Task("ENVI_ImageIntersection")
        envi_II.inputs.file_types = "hdr"
        envi_II.inputs.input_raster1 = data1
        envi_II.inputs.input_raster2 = data2
        envi_II.inputs.output_raster1_uri_filename = "Image1"
        envi_II.inputs.output_raster2_uri_filename = "Image2"



        workflow = gbdx.Workflow([envi_II])

        '''
        workflow.savedata(
            aoptask1.outputs.data,
                location='Benchmark/ENVI_ImageIntersection/AOP/QB1'
        )

        workflow.savedata(
            aoptask2.outputs.data,
                location='Benchmark/ENVI_ImageIntersection/AOP/QB2'
        )
        '''

        workflow.savedata(
            envi_II.outputs.output_raster1_uri,
                location='Benchmark/ENVI_ImageIntersection/II/QS/QB1'
        )

        workflow.savedata(
            envi_II.outputs.output_raster2_uri,
                location='Benchmark/ENVI_ImageIntersection/II/QS/QB2'
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
