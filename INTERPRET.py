import gui.gui_browse_t as gui_browse
import gui.gui_enterstring_t as gui_enterstring
import plot_time_series
import analyze_json
import scale_timecode
import pyt.math.unscale as unscale
import pyt.time.parse_timecode as parse_timecode
import pandas as pd
import plot_timepoints
import pyt.paths.parse_path as parse_path

import pub_markdown

verbose = True
generate_markdown = True

def create_and_save_dataframe(peaks_scaled, peaks_unscaled, peaks_timecode, peaks_m, peaks_s, output_file):
    # Create a dictionary with column names as keys and corresponding lists as values
    data = {
        'peaks_scaled': peaks_scaled,
        'peaks_unscaled': peaks_unscaled,
        'peaks_timecode': peaks_timecode,
        'peaks_m': peaks_m,
        'peaks_s': peaks_s
    }
    
    # Create DataFrame
    df = pd.DataFrame(data)
    
    # Save DataFrame to CSV file
    df.to_csv(output_file, index=False)
    
    print(f"DataFrame successfully saved to {output_file}")

def extract_stem_name(json_path, verbose=False):
    name_string, ext_string = parse_path.main(json_path)
    if verbose:
        print("ddfdf", name_string)
        
    return name_string

def output_image_path(stem_name, output_folder="OUTPUT/"):
    image_path = output_folder+stem_name+'/'+stem_name+'_SEGM.png'
    print("image_path:", image_path)
    return image_path


# Select the .json file exported from the APP
print('>>> Select the .json file exported from the APP')
json_path = gui_browse.main(params_title='Select the .json file exported from the APP', 
         params_initbrowser='INPUT',
         params_extensions='.json',               # E.g. '.csv'
        #  size=(40,20),
         verbose=False)

# exit()
stem_name = extract_stem_name(json_path)
image_path = output_image_path(stem_name)
# exit()
if verbose:
    print("json_path:", json_path)

# exit()
x_range = scale_timecode.main() # In miliseconds
x_range_seconds = x_range / 1000.
# exit()
if verbose:
    print("x_range:", x_range)
    print("x_range_seconds:", x_range_seconds)


# exit()
peaks_scaled, result_file_path = plot_time_series.main(json_path)

print(peaks_scaled)

peaks_unscaled = []
peaks_timecode = []
peaks_m = []
peaks_s = []
for peak in peaks_scaled:
    unscaled_value = unscale.main(peak, x_range)
    peaks_unscaled.append(unscaled_value)
    minutes, seconds, remaining_ms = parse_timecode.main(unscaled_value)
    if verbose:
        print("minutes:", minutes, "seconds:", seconds, "remaining_ms:", remaining_ms)
    peaks_m.append(minutes)

    milis = int(remaining_ms) / 1000.
    minutes_plus_miliseconds = seconds + milis
    # if verbose:
    print("minutes_plus_miliseconds:", minutes_plus_miliseconds)
    peaks_s.append(minutes_plus_miliseconds)
    peaks_timecode.append(str(minutes)+'m'+str(minutes_plus_miliseconds)+'s')

    if verbose:
        print(unscaled_value, '['+str(peak)+']', str(minutes)+'m', str(seconds)+'s', str(int(milis))+'ms')

create_and_save_dataframe(peaks_scaled, peaks_unscaled, peaks_timecode, peaks_m, peaks_s, result_file_path)

if verbose:
    print(peaks_unscaled)   # Miliseconds
    print(stem_name)
    print(x_range_seconds)
plot_timepoints.main(peaks_unscaled, image_path, x_range=x_range_seconds, name=stem_name)
analyze_json.main(json_path)

######
print("peaks_unscaled:", peaks_unscaled)
# Convert to a list of floats
peaks_float_list = [float(x) for x in peaks_unscaled]
print("peaks_float_list:", peaks_float_list)

# Convert to a list of floats and sort the list
float_list = sorted([float(x) for x in peaks_unscaled])

# Function to format milliseconds to "mm:ss.SS"
def format_time(ms):
    minutes = int(ms // 60000)           # Calculate minutes
    seconds = int((ms % 60000) // 1000)  # Calculate seconds
    milliseconds = int(ms % 1000 // 10)  # Calculate hundredths of a second
    return f"{minutes}:{seconds:02}.{milliseconds:02}"

# Create a formatted list of strings
formatted_time_list = [format_time(x) for x in float_list]
######

if generate_markdown:
    youtube_url = gui_enterstring.main("This will generate dynamic links.", 
                                       "URL", "Enter youtube URL", 
            #  font=("Arial", 16), 
            default_text="https://youtu.be/FXzPxJcDD-M", 
            verbose=False)

    # youtube_url = "https://youtu.be/FXzPxJcDD-M" 
    # timecodes = ["3:04.23", "5:12.34", "7:45.67"]
    timecodes = formatted_time_list
    pub_markdown.main(youtube_url, timecodes, proj_name=stem_name, savefolder="OUTPUT/"+stem_name+"/")