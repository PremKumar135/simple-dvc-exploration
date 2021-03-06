#split the raw data
#save it into the processed data
import os
import pandas as pd
import argparse
from get_data import load_configurations
from sklearn.model_selection import train_test_split

def split_and_save_data(config_path):
    config = load_configurations(config_path)
    raw_data_path = config['raw_data']['raw_dataset_csv']
    train_data_path = config['split_data']['train_path']
    test_data_path = config['split_data']['test_path']
    split_ratio = config['split_data']['test_size']
    random_state = config['base']['random_state']

    df = pd.read_csv(raw_data_path)
    train, test = train_test_split(df, test_size = split_ratio, random_state=random_state)

    #save files
    train.to_csv(train_data_path, index=False, encoding='utf-8')
    test.to_csv(test_data_path, index=False, encoding='utf-8')

if __name__ == '__main__':
    args = argparse.ArgumentParser()
    args.add_argument('--config', default='params.yaml')
    parsed_args = args.parse_args()
    split_and_save_data(parsed_args.config)