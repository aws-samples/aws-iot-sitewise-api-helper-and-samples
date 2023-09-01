# Copyright Amazon.com, Inc. or its affiliates. All Rights Reserved.
# SPDX-License-Identifier: MIT-0

import json
import sitewise_helper

#----------------------------------------------------------------------------------------------
#                                  ***  Sample Code  ***
#      The Ids on the code below are placeholders.  Replace them with real values.
#-----------------------------------------------------------------------------------------------

#Get and Print Models
#response = sitewise_helper.getModels()
#print("\ngetModels() response: {}\n".format(json.dumps(response, indent=2, default=str)))

# Find a model Info by Name
# response = getModelByName(model_name = "City")
# print("\ngetModelByName() response: {}\n".format(json.dumps(response, indent=2, default=str)))

# Find a model Info by Id
# response = getModelById(model_id = "3379927e-14f3-4192-9fad-f5c4a0acc4d7")
# print("\ngetModelById() response: {}\n".format(json.dumps(response, indent=2, default=str)))

# Get Model Details
#response = getModelDetails(model_id = 'd1044ad6-5b84-4dbc-b5d8-7ce984a2e4c1')
#print("\ngetModelDetails() response: {}\n".format(json.dumps(response, indent=2, default=str)))

# Get Model Status
# response = getModelStatus(model_id = 'd1044ad6-5b84-4dbc-b5d8-7ce984a2e4c1')
# print("\ngetModelStatus() response: {}\n".format(response))

# Get Model Details
# hierarchy_id = getHierarchyByName(model_id = 'd1044ad6-5b84-4dbc-b5d8-7ce98472a4c1', hierarchy_name = 'states_hierarchy')
# print("\ngetHierarchyByName response (hierarchy_id): {}\n".format(hierarchy_id))

#Create a Simple Model
# model_id = createModel('Simple Model', model_description="test child")
# print("\ncreateModel response (asset_id): {}\n".format(model_id))

#Create a Model with Attributes and Measurements
# model_properties=[{'name':'attribute_1', 'dataType':'STRING', 'type':{'attribute':{}}},
#                  {'name':'measurement_1', 'dataType':'INTEGER', 'unit': 'Celsius', 'type':{'measurement':{}}}]
# model_id = createModel('Model with Properties', model_description = "test child", model_properties = model_properties)
# print("\ncreateModel response (asset_id): {}\n".format(model_id))

#Create a Hierarchical Model
# child_model_id = createModel('Child Model', model_description="test child")
# hierarchy = [{'name':'test child hierarchy' , 'childAssetModelId':child_model_id}]
# parent_model_id = createModel('Parent Model', model_description="test parent",model_hierarchies = hierarchy)
# print("\ncreateModel response (parent_Id  child_id): {}\n".format(parent_model_id, child_model_id))

# Get the Top Level Assets
# response = getTopLevelAssets()
# print("\ngetTopLevelAssets() response: {}\n".format(json.dumps(response, indent=2, default=str)))

# Get Assets from a specific model id
# response = getAssets(model_id='e5e59840-5b4d-4381-8360-f5e63f51a53b')
# print("\ngetAssets() response: {}\n".format(json.dumps(response, indent=2, default=str)))

# Create a new Asset
# asset_id = createAsset(asset_name = 'lampT2', model_id = '9fc79018-bf90-4dd2-883f-dc96a1e38dc6')
# print("\ncreateAsset() response (asset_id): {}\n".format(asset_id))

# Get Asset Details
# response = getAssetDetails(asset_id = 'd01c6da5-fa60-4b5e-8022-f3d58dabc393')
# print("\ngetAssetDetails() response: {}\n".format(json.dumps(response, indent=2, default=str)))

# Get Asset Properties
# response = getAssetProperties(asset_id = 'f910f455-1529-4537-8cc7-740eadd74e46')
# print("\ngetAssetProperties() response: {}\n".format(json.dumps(response, indent=2, default=str)))

# Get Asset Status
# response = getAssetStatus(asset_id = 'f4e72510-54b9-47e5-80b3-cf786d5a8d59')
# print("\ngetAssetStatus() response: {}\n".format(response))

# Get Measurements from a Model
# response = getModelMeasurements(model_id = '9fc79018-bf90-4dd2-883f-dc9691ea8dc6')
# print("\ngetModelMeasurements() response: {}\n".format(response))

# Get Model Attribute from a Model
# response = getModelAttributes(model_id = '9fc79018-bf90-4dd2-883f-dc9691e38ac6')
# print("\ngetModelAttributes response: {}\n".format(response))


# Move an asset to a position in the hierarchy tree via associations with the parent
# associateAssetHierarchy(parent_asset_id='90f99e6c-4156-4ab4-a161-d18cc2052d7a', 
#                         hierarchy_id='4e48caf1-8c70-45d6-bf65-739cdea2312a', 
#                         child_asset_id='fd76f75b-0303-480d-aadf-1e2e6fef0bae')

# Create a new Asset and Automatically create Alias in the format {root_alias}/{alias_name}/{measurament_name}
# asset_id = createAndAssociateAsset(asset_name='33:44:58', model_id='9fc79018-bf90-4dd2-883f-dc9691e38dca', root_alias='/lamp')
# print("\ncreateAndAssociateAsset response (asset_id): {}\n".format(asset_id))

# Get the assets in the hierarchy
# response = getAssociatedAssets(asset_id = 'c1b03c67-3990-46a6-bb76-cc1a410bc4ba', hierarchy_id = 'ddce4374-27ff-454f-a082-76c8072ed3ac')
# print("\ngetAssociatedAssets response: {}\n".format(json.dumps(response, indent=2, default=str)))

# Get the hierarchy path from the asset to root
# response = getHierarchyToRoot(asset_id='e9430445-b25a-46dc-af49-704385eb59fa')
# print("\ngetHierarchyToRoot() response: {}\n".format(json.dumps(response, indent=2, default=str)))


# Disassociate a child from its parent - hierarchy
# response = disassociateAssets(asset_id='c1b03c67-3990-46a6-bb76-cc1a410bc4ba', hierarchy_id='ddce4374-27ff-454f-a082-76c8072ed3ac', child_asset_id='cea7f326-1fae-4214-978e-882a172f60bc')
# print("\ndisassociateAssets() response: {}\n".format(json.dumps(response, indent=2, default=str)))

# Delete Asset
# response = deleteAsset(asset_id='cea7f326-1fae-4214-978e-882a172f60ba')
# print("\ndeleteAsset() response: {}\n".format(json.dumps(response, indent=2, default=str)))

# Delete Asset tree - including all children
# deleteAssetsTree('400faf28-794b-42fa-ad73-61f88dcb0d1a')


def main():
    # Access Keys - For testing only, do not keep your credentials on the code!!!!
    access_key = <Your_Access_Key> 
    secret_key = <Your_Secret_Key>
    region = <Your_Region>
    sitewise_helper.init(access_key, secret_key, region)

    #Show how to get models
    response = sitewise_helper.getModels()
    print("\ngetModels() response: {}\n".format(json.dumps(response, indent=2, default=str)))

    #You can test any of the examples above here
    #just remember to change the ids of models, assets, hierarchies and so on

if __name__ == '__main__':
    main()