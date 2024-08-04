'''This script generates links to the points in the youtube video where the transition events are suspected to be'''

# Function to convert timecode to seconds
def timecode_to_seconds(timecode):
    minutes, seconds = timecode.split(":")
    total_seconds = int(minutes) * 60 + float(seconds)
    return int(total_seconds)

def main(youtube_url, timecodes, proj_name='exp?'):
    # Generate the markdown content
    markdown_content = "# "+proj_name+"\n\n"
    for i, timecode in enumerate(timecodes):
        seconds = timecode_to_seconds(timecode)
        markdown_content += f"[transition #{i+1} ({timecode})]({youtube_url}&t={seconds}s)\n\n"

    # Save to markdown file
    with open("pub/"+proj_name+"_transitions.md", "w") as file:
        file.write(markdown_content)

    print("Markdown file generated successfully.")

if __name__ == "__main__":
    # Define the inputs
    youtube_url = "https://youtu.be/FXzPxJcDD-M"    
    timecodes = ["3:04.23", "5:12.34", "7:45.67"]
    main(youtube_url, timecodes, proj_name='exp15a')