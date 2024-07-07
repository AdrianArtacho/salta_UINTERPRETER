import json
import matplotlib.pyplot as plt
import numpy as np
import scipy.ndimage as ndimage
from scipy.signal import find_peaks
import os
import csv
import pyt.paths.parse_path as parse_path
import pyt.paths.create_folder as create_folder

def output_folder_path(file_path, output_path, verbose=False):
    # Extract the directory part of the path
    folder_path = os.path.dirname(file_path)
    if verbose:
        print(folder_path)

    # exit()
    name_string, ext_string = parse_path.main(file_path, verbose=False)

    if verbose:
        print("name_string:",name_string, "ext_string:", ext_string)
    
    create_folder.main(name_string, local_folder = 'OUTPUT')
    output_folder_path = output_path+name_string+'/'+name_string
    return output_folder_path

def main(file_path, sigma=2, output_path='OUTPUT/', verbose=False):
    # Output_folder_path
    save_filepath = output_folder_path(file_path, output_path, verbose=verbose)
    if verbose:
        print("save_path:", save_filepath)
    # exit()

    # Load the JSON data from the file
    with open(file_path, 'r') as file:
        data = json.load(file)

    # Extract the time series data
    general_kde = data['data']['General KDE']
    kde_sum = data['data']["KDE's sum"]
    kde_top = data['data']["KDE's top"]

    # Smooth the KDE's sum using a Gaussian filter
    smoothed_kde_sum = ndimage.gaussian_filter(kde_sum, sigma=sigma)

    # Find peaks in the smoothed data
    peaks, _ = find_peaks(smoothed_kde_sum, height=0)  # Adjust height as necessary

    # Create plots for each time series
    fig, axes = plt.subplots(3, 1, figsize=(10, 15))

    # Plot for General KDE
    axes[0].plot(general_kde, label='General KDE', color='blue')
    axes[0].set_title('General KDE')
    axes[0].set_xlabel('Index')
    axes[0].set_ylabel('Value')
    axes[0].legend()

    # Plot for KDE's sum with peaks on smoothed data
    axes[1].plot(kde_sum, label="KDE's sum", color='green', alpha=0.5)  # Original data
    axes[1].plot(smoothed_kde_sum, linestyle='--', color='red', label="Smoothed KDE's sum")  # Smoothed data
    axes[1].plot(peaks, smoothed_kde_sum[peaks], "x", label="Peaks")  # Mark peaks
    axes[1].set_title("KDE's sum with Peaks on Smoothed Data")
    axes[1].set_xlabel('Index')
    axes[1].set_ylabel('Value')
    axes[1].legend()

    # Plot for KDE's top
    axes[2].plot(kde_top, label="KDE's top", color='red')
    axes[2].set_title("KDE's top")
    axes[2].set_xlabel('Index')
    axes[2].set_ylabel('Value')
    axes[2].legend()

    # exit()
    plt.tight_layout()
    plt.savefig(save_filepath+'_graph.png')
    plt.show()

    # Return the positions of the peaks
    if verbose:
        print(peaks)
        print(type(peaks))

    # Specify the file path to save to
    # result_file_path = folder_path+'/result.csv'
    result_file_path = save_filepath+'_result.csv'

    # Save the array to a CSV file using numpy.savetxt
    np.savetxt(result_file_path, peaks, delimiter=',', fmt='%d')  # Use fmt='%d' for integers
    if verbose:
        print("Array has been saved to", result_file_path)
    
    return peaks, result_file_path

# Example usage
# file_path = 'path_to_your_file.json'  # Replace this with the path to your JSON file
# plot_time_series(file_path)


if __name__ == "__main__":
    # file_path = 'path_to_your_file.json'  # Replace this with the path to your JSON file
    file_path='INPUT/exp5b_audios/data.json'
    main(file_path)  # Specify your desired output filename here

