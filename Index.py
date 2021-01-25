
#\ Indexes
###############################################################



#\ result frame geometry
result_frame_width = 300
result_frame_height = 450
result_frame_gap = 10

#\ result image geometry
#\ make the height : width = 2 : 3
result_image_width = result_frame_width
result_image_height = result_frame_width*2/3


#\ table headers
result_vertical_table_header= ["Stock photo scoring", "UGC photo scoring(score)", "UGC photo scoring(class)", "Image keyword"]
result_horizontal_table_header = lambda num : ("image " + str(num))


#\ API Key
client_id = "FrUZcCiLsmTZEM1rJbjvmtQh"
client_secret = "iDGW1IZTpCvmg0CZAdnJvmV9JNfvfzYPUxSmv3m2mYqyiiCb"


#\ icon path
icon_path = "src\\image\\icon.png"


#\ api image_quality_ugc class transform
quality_ugc_class_TF = {1 : "very bad",
                        2 : "bad",
                        3 : "normal",
                        4 : "good",
                        5 : "very good"}


#\ loading gif
LoadingGif = "src/image/loading.gif"