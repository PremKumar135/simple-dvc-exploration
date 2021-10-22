#load the given data
#store it in data/raw for further process
import os
import pandas as pd
import argparse
from get_data import get_params, get_data

def load_and_save(config_path):
    config = get_params(config_path)
    df = get_data(config_path)
    new_cols = [col.replace(' ', '_') for col in df.columns]
    raw_data_path = config['load_raw_data']['raw_dataset_csv']
    df.to_csv(raw_data_path, sep=',', index=False, header=new_cols)

if __name__=='__main__':
    args = argparse.ArgumentParser()
    args.add_argument('--config', default='params.yaml')
    parsed_args = args.parse_args()
    load_and_save(parsed_args.config)
