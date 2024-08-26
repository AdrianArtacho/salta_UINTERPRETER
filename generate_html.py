import print_link

def time_to_seconds(time_str):
    """Convert a time string 'mm:ss' or 'hh:mm:ss' to seconds."""
    parts = time_str.split(':')
    parts = [int(part) for part in parts]
    if len(parts) == 2:
        return parts[0] * 60 + parts[1]
    elif len(parts) == 3:
        return parts[0] * 3600 + parts[1] * 60 + parts[2]
    else:
        raise ValueError("Time format should be 'mm:ss' or 'hh:mm:ss'")

def main(youtube_url, timepoints, video_duration, 
         stem_name='Test',
         containing_folder='pub/',
         htmltitle='YouTube Video with Padding'):
        #  output_file="youtube_video_with_padding.html"
        #  ):
    
    output_file=containing_folder+stem_name+".html"

    video_id = youtube_url.split("v=")[-1].split("&")[0]
    
    # Start building the HTML content
    html_content = f"""
    <!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>{stem_name}</title>
        <style>
            body {{
                margin: 0;
                padding: 0;
                font-family: Arial, sans-serif;
                display: flex;
                justify-content: center;
                align-items: center;
                flex-direction: column;
            }}
            .container {{
                width: 100%;
                max-width: 900px; /* Constrain the maximum width */
                padding: 20px;
                box-sizing: border-box;
            }}
            .video-container {{
                position: relative;
                width: 100%;
                height: 0;
                padding-bottom: 56.25%; /* 16:9 aspect ratio */
            }}
            iframe {{
                position: absolute;
                top: 0;
                left: 0;
                width: 100%;
                height: 100%;
                border: none;
            }}
            .timeline {{
                position: relative;
                width: 100%;
                height: 50px;
                background-color: #e0e0e0;
                margin-top: 20px;
                margin-bottom: 20px;
            }}
            .tick-container {{
                position: absolute;
                text-align: center;
                cursor: pointer;
            }}
            .tick {{
                height: 20px;
                width: 2px;
                background-color: red;
                margin: 0 auto;
            }}
            .label {{
                font-size: 12px;
                transform: translateY(25px);
            }}
            .interval-graphic {{
                position: relative;
                width: 100%;
                height: 30px;
                background-color: #f0f0f0;
                margin-bottom: 20px;
            }}
            .interval {{
                position: absolute;
                height: 100%;
                background-color: rgba(0, 0, 255, 0.3); /* Semi-transparent blue */
                margin-left: 2px; /* Padding between intervals */
                margin-right: 2px; /* Padding between intervals */
                display: flex;
                align-items: center;
                justify-content: center;
                font-size: 14px;
                color: black;
                font-weight: bold;
                cursor: pointer;
            }}
        </style>
    </head>
    <body>
        <div class="container">
            <h1>{htmltitle}</h1>
            <div class="video-container">
                <iframe id="youtubePlayer"
                        src="https://www.youtube.com/embed/{video_id}"
                        allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture"
                        allowfullscreen></iframe>
            </div>
            <div class="timeline">
    """

    # Generate tick containers
    ticks_positions = []
    for timepoint in timepoints:
        seconds = time_to_seconds(timepoint)
        position_percent = (seconds / video_duration) * 100
        ticks_positions.append((position_percent, seconds))
        html_content += f"""
        <div class="tick-container" style="left: calc({position_percent}% - 1px);" onclick="document.getElementById('youtubePlayer').src='https://www.youtube.com/embed/{video_id}?start={seconds}&autoplay=1';">
            <div class="tick"></div>
            <div class="label">{timepoint}</div>
        </div>
        """

    # Close the timeline div
    html_content += "</div>"

    # Generate the interval graphic with labels
    html_content += '<div class="interval-graphic">\n'
    alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    label_index = 0

    # First interval: from start to first tick, linking to the start of the video
    if ticks_positions:
        first_tick_position, _ = ticks_positions[0]
        html_content += f"""
        <div class="interval" style="left: 0%; width: calc({first_tick_position}% - 4px);"
             onclick="document.getElementById('youtubePlayer').src='https://www.youtube.com/embed/{video_id}?start=0&autoplay=1';">
            {alphabet[label_index]}
        </div>
        """
        label_index += 1

    # Middle intervals: between ticks, linking to the corresponding tick timestamp
    for i in range(len(ticks_positions) - 1):
        left_position, current_seconds = ticks_positions[i]
        right_position, _ = ticks_positions[i + 1]
        padding_adjustment = 6 if i == 0 else 4  # Add extra padding between 'A' and 'B'
        html_content += f"""
        <div class="interval" style="left: {left_position}%; width: calc({right_position}% - {left_position}% - {padding_adjustment}px);"
             onclick="document.getElementById('youtubePlayer').src='https://www.youtube.com/embed/{video_id}?start={current_seconds}&autoplay=1';">
            {alphabet[label_index]}
        </div>
        """
        label_index += 1

    # Last interval: from last tick to end, linking to the last tick timestamp
    if ticks_positions and label_index < len(alphabet):
        last_tick_position, last_seconds = ticks_positions[-1]
        html_content += f"""
        <div class="interval" style="left: {last_tick_position}%; width: calc(100% - {last_tick_position}% - 2px);"
             onclick="document.getElementById('youtubePlayer').src='https://www.youtube.com/embed/{video_id}?start={last_seconds}&autoplay=1';">
            {alphabet[label_index]}
        </div>
        """

    html_content += "</div>\n"

    # Close the HTML content
    html_content += """
        </div>
    </body>
    </html>
    """

    # Write the content to an HTML file
    with open(output_file, 'w') as file:
        file.write(html_content)

    print(f"HTML file '{output_file}' has been generated successfully.")

# # Example usage:
# youtube_url = "https://www.youtube.com/watch?v=dQw4w9WgXcQ"  # Replace with your YouTube video URL
# timepoints = ["1:22", "3:21", "5:45"]  # Replace with your list of timepoints
# video_duration = 213  # Video duration in seconds (e.g., 3:33 = 213 seconds)

# generate_html(youtube_url, timepoints, video_duration)

############
    return output_file



if __name__ == "__main__":
    # Example usage:
    youtube_url = "https://www.youtube.com/watch?v=5JXEPltfCes"  # Replace with your YouTube video URL
    timepoints = ["1:22", "2:21", "3:45"]  # Replace with your list of timepoints
    video_duration = 279 # Seconds?

    output_file = main(youtube_url, timepoints, video_duration)
    print_link.main(output_file)
    # main()