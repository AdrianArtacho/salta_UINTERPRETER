import pandas as pd

def extract_and_check_range_x(summary_df, verbose=False):
    # Extract the 'range_x' values from the DataFrame
    range_x_values = summary_df['range_x'].tolist()
    
    # Check if all values in range_x_values are the same
    if all(x == range_x_values[0] for x in range_x_values):
        # If all values are the same, return the common value
        common_range_x = range_x_values[0]
        if verbose:
            print(f"The common value of 'range_x' across all rows is: {common_range_x}")
        return common_range_x
    else:
        # If values differ, raise a warning or handle the condition as needed
        print("Warning: The values in 'range_x' are not the same across all rows.")
        # Optionally, you can print the individual values for debugging
        print(f"Range_x values found: {range_x_values}")
        return None  # Or handle this case as per your requirement

def main(input_path, output_path='check.csv', verbose=False):
    # Load the CSV file
    df = pd.read_csv(input_path)

    # Prepare the DataFrame
    features = df['feature'].unique()
    data = []


    for feature in features:
        feature_df = df[df['feature'] == feature]
        instance_count = len(feature_df)
        min_x = feature_df['x_axis'].min()
        min_y = feature_df['y_axis'].min()
        range_x = feature_df['x_axis'].max() - min_x
        range_y = feature_df['y_axis'].max() - min_y
        data.append([feature, instance_count, min_x, min_y, range_x, range_y])

    # Create a new DataFrame with the required information
    summary_df = pd.DataFrame(data, columns=['feature', 'instance_count', 'min_x', 'min_y', 'range_x', 'range_y'])

    # Save the summary DataFrame to a CSV file
    summary_df.to_csv(output_path, index=False)

    if verbose:
        print(f"Summary saved to {output_path}")

    x_range_across_features = extract_and_check_range_x(summary_df)

    return x_range_across_features

if __name__ == "__main__":
    # Example usage
    input_file_path = 'OUTPUT/exp0b_SALTA/exp0b_SALTA.csv'
    main(input_file_path)
