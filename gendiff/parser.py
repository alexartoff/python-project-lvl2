import json
import yaml
import os


def files_parser(file_one, file_two):
    format_file_one, format_file_two = get_format(file_one, file_two)
    if format_file_one == 'yml' or format_file_one == 'yaml':
        with open(file_one, 'r') as file:
            dict_one = yaml.safe_load(file)
    if format_file_one == 'json':
        dict_one = dict(json.load(open(file_one)))
    if format_file_two == 'yml' or format_file_two == 'yaml':
        with open(file_two, 'r') as file:
            dict_two = yaml.safe_load(file)
    if format_file_two == 'json':
        dict_two = dict(json.load(open(file_two)))
    # print(f'{dict_one}\n{dict_two}')
    return dict_one, dict_two


def get_format(file_one, file_two):
    # print('>>>', os.listdir(path='.'), os.getcwd())
    format_file_one = str(os.path.split(file_one)[1]).split('.')[-1]
    format_file_two = str(os.path.split(file_two)[1]).split('.')[-1]
    return format_file_one, format_file_two
