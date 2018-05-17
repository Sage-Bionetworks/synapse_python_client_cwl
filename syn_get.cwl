#!/usr/bin/env cwl-runner
cwlVersion: v1.0
class: CommandLineTool

hints:
  DockerRequirement:
    dockerPull: quay.io/andrewelamb/synapse_python_client
    
baseCommand: [ python, /usr/local/bin/syn_get.py ]

inputs:
 
  synapse_id:
    type: string
    inputBinding:
      prefix: "--synapse_id"
      
  config_file:
    type: File
    inputBinding:
      prefix: "--config_file"

outputs:

  output:
    type: File
    outputBinding:
      glob: ./*