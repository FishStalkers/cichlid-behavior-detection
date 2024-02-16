import glob
import os
import pickle

print(os.getcwd())
from behavior_detection.BehavioralVideo import BehavioralVideo


def bower_circling_in_batches(config: str, batches: str, shuffle=1):
    for batch in os.listdir(batches):
        curr_dir = os.path.join(batches, batch)
        vid_name = glob.glob(os.path.join(curr_dir, '*.mp4'))[0]
        vid_path = os.path.join(curr_dir, vid_name)
        tracklets_path = glob.glob(os.path.join(curr_dir, '*filtered.h5'))[0]
        vid = BehavioralVideo(video_path=vid_path, config=config, shuffle=shuffle, tracklets=tracklets_path)
        vid.calculate_velocities()
        vid.check_bower_circling(threshold=90, extract_clips=True, bower_circling_length=32)
        print(f"Successfully extracted bower circling clips for {batch}")



def main():
   vid = r"/Users/ben/Downloads/0001_vid.mp4"
   pose_data = r"/Users/ben/Downloads/0001_vidDLC_dlcrnetms5_dlc_modelJul26shuffle4_100000_el_filtered.csv"
   velocities_path = r"/Users/ben/Downloads/0001_vidDLC_dlcrnetms5_dlc_modelJul26shuffle4_100000_el_filtered_velocities.pickle"

   with open(velocities_path, 'rb') as handle:
      velocities = pickle.load(handle)

   #print(f'velocities: {velocities}')
   behave = BehavioralVideo(video_path=vid, tracklets_path=pose_data)
   behave.set(velocities=velocities)
   behave.check_bower_circling(threshold=120, bower_circling_length=1, extract_clips=True, buffer=5)



if __name__ == "__main__":
    main()
