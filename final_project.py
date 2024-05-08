import argparse
import yaml
import os
import sys

files = os.listdir()

def parse_arguments():
    parser = argparse.ArgumentParser()
    parser.add_argument("input_file")
    parser.add_argument("output_file")
    return parser.parse_args()

def main():
    args = parse_arguments()
    input_file = args.input_file
    output_file = args.output_file
    if os.path.splitext(input_file)[1] == ".json":
        obj = loading_json(input_file)
    if os.path.splitext(input_file)[1] == ".yml" or os.path.splitext(input_file)[1] == ".yaml":
        obj = loading_yml_or_yaml(input_file)
        
def loading_json(input_file):
    for file in files:
        if file == input_file:
            with open(file, "r") as file_js:
                file_content = file_js.read()
                try:
                    json_obj = json.loads(file_content)
                    return json_obj
                except:
                    print("json is not written correctly ")
                    sys.exit(1)
    print("No such file")
    sys.exit(1)

def loading_yml_or_yaml(input_file):
    for file in files:
        if file == input_file:
            with open(file, "r") as file_yaml:
                file_content = file_yaml.read()
                try:
                    yaml_obj = yaml.safe_load(file_content)
                    return yaml_obj
                except:
                    print("yaml or yml is not written correctly ")
    print("No such file")
    sys.exit(1)
     

if __name__ == "__main__":
    main()


