from schematic.models.metadata import MetadataModel
from schematic import CONFIG

config = CONFIG.load_config("./schematic/config.yml")

inputMModelLocation = CONFIG["model"]["input"]["location"]
inputMModelLocationType = CONFIG["model"]["input"]["file_type"]

manifest_title = CONFIG["manifest"]["title"]
manifest_data_type = CONFIG["manifest"]["data_type"]

metadata_model = MetadataModel(inputMModelLocation, inputMModelLocationType)
metadata_model.getModelManifest(title=manifest_title, 
                                rootNode=manifest_data_type)
