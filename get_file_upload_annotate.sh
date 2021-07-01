pred_file=$1
echo "Convert pred file ${pred_file} to gt format"
python norm.py --target_file $pred_file

sleep 2

if [ $# -eq 2 ] 
then
	tar_video=$2
	arrIN=(${tar_video//./ })
	save_video_name="results/video_new_resolution.${arrIN[1]}"

	echo "Process ${arrIN[0]}"
	echo "Start convert video to default size (1920, 1080) which is default output of FairMot"
	echo "New video save in ${save_video_name}"
	ffmpeg -i $tar_video -vf "fps=20,scale=1920:1080" $save_video_name
else
	echo "Finish!!!"
fi