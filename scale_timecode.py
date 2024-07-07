import gui.gui_browse as gui_browse
import analyze_salta
import pyt.time.parse_timecode as parse_timecode

# def convert_ms_to_min_sec_ms(milliseconds):
#     # Convert milliseconds to minutes, seconds, and remaining milliseconds
#     total_seconds = milliseconds / 1000  # Convert milliseconds to seconds
#     minutes = total_seconds // 60  # Calculate total minutes
#     seconds = total_seconds % 60  # Calculate remaining seconds
#     remaining_ms = milliseconds % 1000  # Calculate remaining milliseconds
    
#     return int(minutes), int(seconds), remaining_ms

# Select the SALTA file that was fed to the APP
def main(verbose=False):
    filepath = gui_browse.main(params_title='Search for the original SALTA .csv file', 
            params_initbrowser='../featurestructure/OUTPUT',
            params_extensions='.csv',               # E.g. '.csv'
            size=(40,20),
            verbose=False)
    
    if verbose:
        print(filepath)

    x_range_across_features = analyze_salta.main(filepath, output_path='INTER/analysis.csv')

    if verbose:
        print("x_range_across_features:", x_range_across_features)

    minutes, seconds, remaining_ms = parse_timecode.main(x_range_across_features)

    if verbose:
        print("The captured section is",str(minutes),'minutes', str(seconds)+"'"+str(remaining_ms), "seconds")

    return x_range_across_features # in miliseconds

if __name__ == "__main__":
    main()