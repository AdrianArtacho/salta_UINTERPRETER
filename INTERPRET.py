import gui.gui_browse as gui_browse
import plot_time_series
import analyze_json
import scale_timecode
import pyt.math.unscale as unscale
import pyt.time.parse_timecode as parse_timecode
import pandas as pd
import plot_timepoints
import pyt.paths.parse_path as parse_path

verbose = True

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
json_path = gui_browse.main(params_title='Browse files', 
         params_initbrowser='INPUT',
         params_extensions='.json',               # E.g. '.csv'
         size=(40,20),
         verbose=False)

stem_name = extract_stem_name(json_path)
image_path = output_image_path(stem_name)
# exit()
if verbose:
    print("json_path:", json_path)

# exit()
x_range = scale_timecode.main() # In miliseconds
x_range_seconds = x_range / 1000.

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
plot_timepoints.main(peaks_unscaled, image_path, x_range=x_range_seconds, name=stem_name)
analyze_json.main(json_path)