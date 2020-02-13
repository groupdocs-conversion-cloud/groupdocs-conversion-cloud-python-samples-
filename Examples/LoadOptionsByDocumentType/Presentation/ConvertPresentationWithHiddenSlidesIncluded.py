# Import modules
import groupdocs_conversion_cloud
from Common import Common

# This example demonstrates how to convert presentation document into pdf document
class ConvertPresentationWithHiddenSlidesIncluded:
    @classmethod  
    def Run(cls):
        # Create necessary API instances
        apiInstance = groupdocs_conversion_cloud.ConvertApi.from_keys(Common.app_sid, Common.app_key)
        
        # Prepare convert settings
        settings = groupdocs_conversion_cloud.ConvertSettings()
        settings.file_path = "Presentation/with_hidden_page.pptx"
        settings.format = "pdf"

        loadOptions = groupdocs_conversion_cloud.PresentationLoadOptions()
        loadOptions.show_hidden_slides = True

        settings.load_options = loadOptions
        settings.output_path = "converted"

        # Convert
        result = apiInstance.convert_document(groupdocs_conversion_cloud.ConvertDocumentRequest(settings))

        print("Document converted: " + result[0].url)
        