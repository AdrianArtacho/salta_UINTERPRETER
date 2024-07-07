import json
import pandas as pd
import matplotlib.pyplot as plt
import sys
import os
import pyt.paths.parse_path as parse_path
import pyt.paths.create_folder as create_folder

def output_folder_path(file_path, output_folder='OUTPUT/',verbose=False):
    # Extract the directory part of the path
    folder_path = os.path.dirname(file_path)
    if verbose:
        print('folder_path:', folder_path)

    # exit()
    name_string, ext_string = parse_path.main(file_path, verbose=False)

    if verbose:
        print("name_string:",name_string, "ext_string:", ext_string)
    
    create_folder.main(name_string, local_folder = 'OUTPUT')
    output_path = output_folder+name_string+'/'+name_string
    if verbose:
        print("output_path:", output_path)
    return output_path 

def main(json_path, scaledValues=False):
    # Output folder path
    output_path = output_folder_path(json_path)

    # Load the JSON file
    with open(json_path, 'r') as f:
        data = json.load(f)
    
    # Create a dataframe to hold the analysis results
    analysis = {'key': [], 'subkey': [], 'num_values': [], 'min_value': [], 'max_value': []}
    
    # Extract data from the 'data' and 'scaledData' keys
    # for key in ['data', 'scaledData']:
    for key in ['data']:
        for subkey, values in data[key].items():
            if isinstance(values, list):
                num_values = len(values)
                min_value = min(values)
                max_value = max(values)
                
                analysis['key'].append('data')
                analysis['subkey'].append(subkey)
                analysis['num_values'].append(num_values)
                analysis['min_value'].append(min_value)
                analysis['max_value'].append(max_value)
            else:
                print(f"Skipping subkey '{subkey}' as it is not a list")

    if scaledValues:
        for key in ['scaledData']:
            for subkey, values in data[key].items():
                if isinstance(values, list):
                    num_values = len(values)
                    min_value = min(values)
                    max_value = max(values)
                    
                    analysis['key'].append('scaledData')
                    analysis['subkey'].append(subkey)
                    analysis['num_values'].append(num_values)
                    analysis['min_value'].append(min_value)
                    analysis['max_value'].append(max_value)
                else:
                    print(f"Skipping subkey '{subkey}' as it is not a list")
    
    # Convert analysis dictionary to a dataframe
    df = pd.DataFrame(analysis)
    
    # Save dataframe to a CSV file
    df.to_csv(output_path+'_analysis.csv', index=False)
    
    # Plot all subkeys
    fig, axs = plt.subplots(len(analysis['subkey']), 1, figsize=(10, len(analysis['subkey']) * 5))
    
    if len(analysis['subkey']) == 1:
        axs = [axs]  # Make sure axs is iterable
    
    for i, subkey in enumerate(analysis['subkey']):
        values = data['data'].get(subkey, data['scaledData'].get(subkey, []))
        axs[i].plot(values)
        axs[i].set_title(subkey)
        axs[i].set_xlabel('Index')
        axs[i].set_ylabel('Value')
    
    plt.tight_layout()
    plt.savefig(output_path+'_subplots.png')

if __name__ == '__main__':
    # if len(sys.argv) != 2:
    #     print("Usage: python analyze_json.py <path_to_json>")
    #     sys.exit(1)
    
    # json_path = sys.argv[1]
    json_path = 'INPUT/test_o1.json'
    main(json_path)
