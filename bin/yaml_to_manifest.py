import argparse
import yaml
import pandas as pd

if __name__ == '__main__':
 
    parser = argparse.ArgumentParser("Converts yaml to manifest")
    parser.add_argument('--yaml_config_file', type = str)
    parser.add_argument('--output_file_string', 
                        type = str, 
                        default = 'manifest.tsv', 
                        required = False)
    args = parser.parse_args()
    
    with open(args.yaml_config_file, 'r') as stream:
    dict = (yaml.load(stream))   

    new_dict = {"path": args.output_files, 
                "parent": dict["parent"],
                "executed": dict["executed"],
                "used": dict["used"]}

    annotation_cols = [key for key in dict.keys() if key.startswith("annotation")]
    for col in annotation_cols:
        new_dict[col.replace("annotation_", "")] = dict[col]

    df = pd.DataFrame(data = new_dict)
    df.to_csv(args.output_file_string, sep = "\t")





