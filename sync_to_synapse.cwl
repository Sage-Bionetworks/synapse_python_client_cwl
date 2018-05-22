#!/usr/bin/env cwl-runner
cwlVersion: v1.0
class: CommandLineTool

hints:
  DockerRequirement:
    dockerPull: quay.io/andrewelamb/synapse_python_client
    
baseCommand: [ python, /usr/local/bin/sync_to_synapse.py ]

stdout: out.txt

inputs:
 
  manifest_file:
    type: File
    inputBinding:
      prefix: "--manifest_file"
      
  synapse_config_file:
    type: File
    inputBinding:
      prefix: "--synapse_config_file"
      
outputs:

  output:
    type: File
    outputBinding:
      glob: out.txt