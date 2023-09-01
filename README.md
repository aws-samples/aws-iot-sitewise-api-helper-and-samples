# Authors
* **Leo Simberg**: Lead IoT Partner Solutions Architect

# About this respository
This repository offers comprehensive code samples demonstrating the interaction with AWS IoT SiteWise APIs. These samples illustrate the creation and manipulation of Models, Assets, and Hierarchies within the IoT SiteWise framework. Developers can utilize this repository as a valuable reference for constructing production-ready code in their applications. Additionally, it serves as a valuable development aid, enabling the streamlined creation and removal of multiple models and assets during various development stages, including testing and quality assurance processes.

**Note:** These utility functions are intended for development purposes and examples. They are not considered production-ready.


# How does it work?
The file **sitewise_helper.py** comprises illustrative examples of AWS IoT SiteWise API calls. Meanwhile, the **sitewise_helper_samples.py** file contains diverse usage instances demonstrating how to effectively leverage the helper functions within an external application context.


### Prerequisites

To use the AWS IoT SiteWise utility functions, you need to have Python installed on your system. Additionally, you should have the Boto3 library installed. You'll also need valid AWS access and secret keys with appropriate permissions to interact with AWS IoT SiteWise.

- Python 3.x
- Boto3 library installed (`pip install boto3`)

### Functions Overview
1. **`init(access_key, secret_key, region)`**

   Initialize the IoT SiteWise client using provided access keys and region.

2. **`createModel(model_name, model_description="", model_properties=[], model_hierarchies=[])`**

   Create a new asset model with specified properties and hierarchies. Returns the asset model ID.

3. **`getModels()`**

   Retrieve a list of all asset models.

4. **`getModelByName(model_name)`**

   Find an asset model by its name.

5. **`getModelById(model_id)`**

   Find an asset model by its ID.

6. **`getModelDetails(model_id)`**

   Retrieve detailed information about an asset model.

7. **`getTopLevelAssets()`**

   Retrieve the top-level assets in the system.

8. **`getAssets(model_id)`**

   Retrieve a list of assets originated from a specific model.

9. **`getAssetDetails(asset_id)`**

   Retrieve detailed information about an asset.

10. **`getAssociatedAssets(asset_id, hierarchy_id)`**

    Retrieve associated assets for a given asset and hierarchy.

11. **`getHierarchyToRoot(asset_id)`**

    Retrieve the hierarchy path from the asset to the root.

12. **`createAsset(asset_name, model_id)`**

    Create a new asset based on a specified model. Returns the asset ID.

13. **`associateAssetHierarchy(parent_asset_id, hierarchy_id, child_asset_id)`**

    Associate a child asset to a parent asset based on a hierarchy.

14. **`associateAssetAlias(asset_id, measurement_id, alias, notification_state='DISABLED')`**

    Associate an alias to an asset property (attribute or measurement).

15. **`createAndAssociateAsset(asset_name, model_id, root_alias="/")`**

    Create an asset and automatically associate its measurements with aliases.

16. **`disassociateAssets(asset_id, hierarchy_id, child_asset_id)`**

    Disassociate a child asset from its parent based on a hierarchy.

17. **`deleteAsset(asset_id)`**

    Delete an asset that is not associated with any other asset.

18. **`deleteAssetsTree(asset_id)`**

    Delete an asset and its entire hierarchy tree.

19. **`deleteTopAssets()`**

    Delete all top-level assets that are not associated with any other assets.

20. **`deleteAllTopAssetsTree()`**

    Delete all top-level assets along with their hierarchy trees. (Use with caution!)

Please ensure that you review the specific use cases and documentation provided for each function in the code for better understanding and proper usage.

### Important Notes
- Ensure that you thoroughly test these utility functions in a controlled environment before using them in a production context.
- It's recommended to follow best practices for error handling, logging, and security when using these utility functions in any project.
- Always stay informed about AWS services' updates and changes that might affect the behavior of these functions.

### License
This library is licensed under the MIT-0 License. See the LICENSE file.

### 
# Special Thanks
* Bin Qiu: Partner Solutions Architect 
* Keith Hodo: Partner Solutions Architect
