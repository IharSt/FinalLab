import argparse
import yaml
import xmltodict
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
    if os.path.splitext(input_file)[1] == ".xml":
        obj = loading_xml(input_file)
    if os.path.splitext(output_file)[1] == ".json":
        create_json_file(obj, output_file)
    if os.path.splitext(output_file)[1] == ".yaml" or os.path.splitext(output_file)[1] == ".yml":
        create_yml_or_yaml_file(obj, output_file)
    if os.path.splitext(output_file)[1] == ".xml":
        create_xml_file(obj, output_file)


# loading into an object from a .json file and verifying that the syntax of the file is correct
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

# loading into an object from an .yml file and verifying that the syntax of the file is correct
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

# loading into an object from an .xml file and verifying that the syntax of the file is correct
def loading_xml(input_file):
    for file in files:
        if file == input_file:
            with open(file, "r") as file_xml:
                file_content = file_xml.read()
                try:
                    xml_obj = xmltodict.parse(file_content)
                    return xml_obj
                except:
                    print("xml is not written correctly ")
                    sys.exit(1)
    print("No such file")
    sys.exit(1)

# writing data from the object to a file in the format and according to the syntax of .json
def create_json_file(obj, output_file):
    json_data = json.dumps(obj)
    with open(f"{os.path.splitext(output_file)[0]}.json", "w") as json_file:
        json_file.write(json_data)

# writing data from an object to a file in the format and according to the syntax of .yml
def create_yml_or_yaml_file(obj, output_file):
    yaml_data = yaml.dump(obj)
    with open(f"{os.path.splitext(output_file)[0]}{os.path.splitext(output_file)[1]}", "w") as yaml_file:
        yaml_file.write(yaml_data)

#writing data from the object to a file in the format and according to the syntax .xml
def create_xml_file(obj, output_file):
    xml_data = {'root': obj}
    xml_data = xmltodict.unparse(xml_data)
    with open(f"{os.path.splitext(output_file)[0]}.xml", "w") as xml_file:
        xml_file.write(xml_data)

if __name__ == "__main__":
    main()


