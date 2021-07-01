video_path=$1
cd ..
cd src
python demo.py mot --load_model ../models/fairmot_dla34.pth --conf_thres 0.3 --arch dla_34 --input-video $video_path

