import matplotlib.pyplot as plt
import pyt.time.parse_timecode as parse_timecode

def title_line(name, x_range, verbose=False):
    if name != None:
        if x_range == None:
            title_text = name
        else:
            title_text = name+' (0 - '+str(x_range)+'s)'
    else:
        title_text = 'Vertical Lines at Timepoints'
    
    if verbose:
        print("title_line:", title_text)
    
    return title_text

def seconds_to_timecode(tp, verbose=False):
    min, sec, ms = parse_timecode.main(tp*1000)
    if verbose:
        print("tp", tp, "min:", min, "sec", sec, "ms", ms)
    
    if min == 0:
        timecode_string = str(sec)+"."+str(int(ms/100))+'s'
    else:
        timecode_string = str(min)+"m"+str(sec)+"."+str(int(ms/100))+'s'
    return timecode_string

def main(timepoints_ms, output_file, x_range=None, name=None, verbose=False):
    title = title_line(name, x_range)

    # Convert timepoints from milliseconds to seconds
    timepoints_s = [tp / 1000 for tp in timepoints_ms]
    
    # Create a figure and axis with adjusted height
    fig, ax = plt.subplots(figsize=(10, 1))  # Adjust the width and height as needed (width, height)
    
    # Plot a thick vertical line for each timepoint and annotate it
    for tp in timepoints_s:
        ax.axvline(x=tp, color='b', linewidth=4)  # Increase the linewidth to 4
        
        timecode_string = seconds_to_timecode(tp)
        if verbose:
            print("timecode:", timecode_string)
        # ax.text(tp, 0.5, f'{tp:.2f}', rotation=90, verticalalignment='center', horizontalalignment='right')  # Display value at each timepoint
        ax.text(tp, 0.5, timecode_string, rotation=90, verticalalignment='center', horizontalalignment='right')  # Display value at each timepoint
    
    # Set axis labels and title
    ax.set_xlabel('Time (seconds)')
    ax.set_title(title)
    
    # Remove y-axis labels and ticks
    ax.yaxis.set_visible(False)
    
    # Set x-axis limits based on the provided x_range or automatically based on data
    if x_range:
        ax.set_xlim([0, x_range])
    else:
        ax.set_xlim([0, max(timepoints_s) + 1])
    
    # Show grid for better readability
    ax.grid(True)
    
    # Save the plot as a PNG file
    plt.savefig(output_file, bbox_inches='tight', dpi=300)
    
    # Show the plot
    plt.show()


if __name__ == "__main__":
    # Example list of timepoints in milliseconds
    timepoints_ms = [125678, 1500, 3000, 4500, 6000]
    output_file = 'OUTPUT/test_segments.png'

    # Plot the timepoints
    main(timepoints_ms, output_file, x_range=None, name='exp1')