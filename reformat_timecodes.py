import math

def main(timecodes, verbose=False):
    reformatted_timecodes = []
    
    for timecode in timecodes:
        if verbose:
            print("timecode:", timecode)
        
        minutes, seconds = timecode.split(':')

        if verbose:
            print("minutes:", minutes, "seconds:", seconds, type(seconds))
        
        secs_rounded = round(float(seconds))

        if verbose:
            print("secs_rounded:", secs_rounded)
        
        mins_and_secs_as_secs = (int(minutes)*60)+secs_rounded

        if verbose:
            print("mins_and_secs_as_secs:", mins_and_secs_as_secs)
        #####
        # mins_and_secs_as_secs = 59
        rounded_mins = int(mins_and_secs_as_secs/60.)

        if verbose:
            print("rounded_mins:", rounded_mins)
        
        rounded_rest = mins_and_secs_as_secs-(rounded_mins*60)
        if verbose:
            print("rounded_rest:", rounded_rest)


        reformatted_timecode = f'{int(rounded_mins)}:{str(int(rounded_rest)).zfill(2)}'

        if verbose:
            print("reformatted_timecode:", reformatted_timecode)

        reformatted_timecodes.append(reformatted_timecode)
    
    return reformatted_timecodes



if __name__ == "__main__":
    # Example usage
    timecodes = ['1:59.90', '2:42.00', '4:06.32', '5:11.69', '6:05.69']
    # timecodes = ['6:05.69']
    reformatted_timecodes = main(timecodes)
    print(reformatted_timecodes)