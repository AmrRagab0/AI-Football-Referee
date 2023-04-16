import json
import os

# read the JSON file
with open('results_spotting_thresholded_0.70 (1).json', 'r') as f:
    markers_data = json.load(f)
    predictions = markers_data["predictions"]

# create the subtitle files
f1 = open("1-720p.srt", "x")
f2 = open("2-720p.srt", "x")

# loop through the markers and create a subtitle for each one
for i, marker in enumerate(predictions):
    # get the game time and split it into parts
    game_time_parts = marker['gameTime'].split(' - ')
    game_time_start = game_time_parts[0]
    game_time_end = game_time_parts[1]

    # get the half, position, label, and confidence
    half = marker['half']
    position = marker['position']
    label = marker['label']
    confidence = marker['confidence'][:4]

    # create the marker label with the label and confidence
    marker_label = f'{label} ({confidence})'

    # create the marker filename based on the game time start
    marker_filename = f'{game_time_start}-720p.mkv'

    # create the marker timestamp based on the game time end
    timestamp_parts = game_time_end.split(':')
    timestamp_minutes = int(timestamp_parts[0])
    timestamp_seconds = int(timestamp_parts[1])
    timestamp_milliseconds = 0
    marker_timestamp_start = f'00:{timestamp_minutes:02d}:{timestamp_seconds:02d},{timestamp_milliseconds:03d}'
    
    
    # calculate the end timestamp by adding 3 seconds to the start timestamp
    timestamp_seconds += 3
    if timestamp_seconds >= 60:
        timestamp_minutes += 1
        timestamp_seconds -= 60
    marker_timestamp_end = f'00:{timestamp_minutes:02d}:{timestamp_seconds:02d},{timestamp_milliseconds:03d}'


    # create the subtitle string
    subtitle_string = f'{i+1}\n{marker_timestamp_start} --> {marker_timestamp_end}\n{marker_label}\n\n'

    # write the subtitle string to the appropriate file based on the half
    if half == "1":
        f1.write(subtitle_string)
    else:
        f2.write(subtitle_string)

    # print the subtitle string
    print(subtitle_string)

# close the subtitle files
f1.close()
f2.close()
