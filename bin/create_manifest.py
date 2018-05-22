import argparse
import yaml
import pandas as pd

if __name__ == '__main__':
 
    parser = argparse.ArgumentParser("Creates manifest file for synctosynapse")
    
    parser.add_argument('--paths', type = str, nargs = '+')
    parser.add_argument('--parent', type = str)
    parser.add_argument('--used', 
                        type = str,
                        nargs = '+',
                        default = None, 
                        required = False)
    parser.add_argument('--executed', 
                        type = str,
                        nargs = '+',
                        default = None, 
                        required = False)
    parser.add_argument('--activity_name', 
                        type = str,
                        default = None, 
                        required = False)
    parser.add_argument('--activity_description', 
                        type = str,
                        default = None, 
                        required = False)
    parser.add_argument('--yaml_config_file', 
                        type = str, 
                        default = None, 
                        required = False)
    parser.add_argument('--output_file_string', 
                        type = str, 
                        default = 'manifest.tsv', 
                        required = False)
    args = parser.parse_args()
    
    manifest_dict = {"path": args.paths, 
                     "parent": args.parent}
    
    if args.used is not None:
        manifest_dict["used"] = ";".join(args.used)
    
    if args.executed is not None:
        manifest_dict["executed"] = ";".join(args.executed)
    
    if args.activity_name is not None:
        manifest_dict["activityName"] = args.activity_name
    
    if args.activity_description is not None:
        manifest_dict["activityDescription"] = args.activity_description
    
     
    if args.yaml_config_file is not None:
        with open(args.yaml_config_file, 'r') as stream:
            dict = (yaml.load(stream))
            annotation_cols = [key for key in dict.keys() if key.startswith("annotation")]
            for col in annotation_cols:
                 manifest_dict[col.replace("annotation_", "")] = dict[col]
    
    df = pd.DataFrame(data = manifest_dict)
    df.to_csv(args.output_file_string, sep = "\t")
