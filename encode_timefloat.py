import math

def main(seconds_float):
    # Round up to the next whole second
    total_seconds = math.ceil(seconds_float)
    
    # Calculate minutes and remaining seconds
    minutes = total_seconds // 60
    seconds = total_seconds % 60
    
    # Format the time as mm:ss
    time_str = f"{minutes}:{seconds:02d}"
    return time_str



if __name__ == "__main__":
    # Example usage
    time_float = 235.8
    formatted_time = main(time_float)
    print(formatted_time)  # Output: 3:56