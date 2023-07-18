from Chamaeleo.methods.fixed import Blawat
from Chamaeleo.utils.pipelines import TranscodePipeline


coding_scheme = Blawat(need_logs=True)

pipeline = TranscodePipeline(coding_scheme=coding_scheme, need_logs=True)

# without index

pipeline.transcode(direction="t_c",input_path="fig1.png",output_path="fig1_Blawat.txt", segment_length=160)

#decode
# pipeline.transcode(direction="t_s",input_path="mri_Church.txt",output_path="decode.jpg", segment_length=160)


pipeline.output_records(type="string")