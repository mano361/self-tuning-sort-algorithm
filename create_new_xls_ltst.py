import pandas as pd
import os
import time
from statistics import mean

def generate_max_min_avg_file(input_file):
    """ """
    """
    1 second = 10^9 nanoseconds
    """
    if os.path.isfile(input_file):
        xls = pd.ExcelFile(input_file)
        random_df = pd.read_excel(xls, sheet_name='Random Data')
        increasing_df = pd.read_excel(xls, sheet_name='Increasing Data')
        decreasing_df = pd.read_excel(xls, sheet_name='Decreasing Data')
        print(increasing_df.shape)
        print(increasing_df.columns)
        print(increasing_df['Array Size'].unique())
        filter_columns = list(random_df.columns)[1:]
        print(filter_columns)

        modified_list = []
        for array_type in [random_df, increasing_df, decreasing_df]:
            min_val_list = []
            max_val_list = []
            avg_val_list = []
            for unique_array_size in array_type['Array Size'].unique():
                curr_df = array_type[array_type['Array Size'] == unique_array_size]
                min_val_list.append(unique_array_size)
                max_val_list.append(unique_array_size)
                avg_val_list.append(unique_array_size)
                for unique_column in filter_columns:
                    curr_col_list = curr_df[unique_column].values.tolist()
                    min_val_list.append(min(curr_col_list) * (10 ** 9))
                    max_val_list.append(max(curr_col_list) * (10 ** 9))
                    avg_val_list.append(mean(curr_col_list) * (10 ** 9))
            min_val_list = [min_val_list[i: i + 8] for i in range(0, len(min_val_list), 8)]
            max_val_list = [max_val_list[i: i + 8] for i in range(0, len(max_val_list), 8)]
            avg_val_list = [avg_val_list[i: i + 8] for i in range(0, len(avg_val_list), 8)]
            modified_list.append([min_val_list, max_val_list, avg_val_list])
        print(modified_list[0][0])
        # Random Data
        random_min_df = pd.DataFrame(modified_list[0][0], columns=list(increasing_df.columns))
        random_max_df = pd.DataFrame(modified_list[0][1], columns=list(increasing_df.columns))
        random_avg_df = pd.DataFrame(modified_list[0][2], columns=list(increasing_df.columns))

        with pd.ExcelWriter("Random_time_efficiency_10_to_10000.xlsx") as writer:
            random_min_df.to_excel(writer, sheet_name='Min Time Data', index=None)
            random_max_df.to_excel(writer, sheet_name='Max Time Data', index=None)
            random_avg_df.to_excel(writer, sheet_name='Avg Time Data', index=None)

        # Increasing Data
        increasing_min_df = pd.DataFrame(modified_list[1][0], columns=list(increasing_df.columns))
        increasing_max_df = pd.DataFrame(modified_list[1][1], columns=list(increasing_df.columns))
        increasing_avg_df = pd.DataFrame(modified_list[1][2], columns=list(increasing_df.columns))

        with pd.ExcelWriter("Increasing_time_efficiency_10_to_10000.xlsx") as writer:
            increasing_min_df.to_excel(writer, sheet_name='Min Time Data', index=None)
            increasing_max_df.to_excel(writer, sheet_name='Max Time Data', index=None)
            increasing_avg_df.to_excel(writer, sheet_name='Avg Time Data', index=None)


        # Decreasing Data
        decreasing_min_df = pd.DataFrame(modified_list[2][0], columns=list(increasing_df.columns))
        decreasing_max_df = pd.DataFrame(modified_list[2][1], columns=list(increasing_df.columns))
        decreasing_avg_df = pd.DataFrame(modified_list[2][2], columns=list(increasing_df.columns))

        with pd.ExcelWriter("Decreasing_time_efficiency_10_to_10000.xlsx") as writer:
            decreasing_min_df.to_excel(writer, sheet_name='Min Time Data', index=None)
            decreasing_max_df.to_excel(writer, sheet_name='Max Time Data', index=None)
            decreasing_avg_df.to_excel(writer, sheet_name='Avg Time Data', index=None)

    else:
        print("File not found in the given path")


if __name__=="__main__":
    generate_max_min_avg_file('D:\\270422\\time_efficiency_10_to_10000.xlsx')
