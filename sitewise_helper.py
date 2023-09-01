# Copyright Amazon.com, Inc. or its affiliates. All Rights Reserved.
# SPDX-License-Identifier: MIT-0

# ************************************************************************************************************************
# This tool is not considered production-ready, and it doesn't have error handling implemented!
# Its intended use is to aid in development and/or provide examples for
# developers to create their own production code.
#
# SiteWise Documentation: https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/iotsitewise.html
# ************************************************************************************************************************

import boto3
import time

client_sw = None

#Init the helper
def init(access_key, secret_key, region):
    global client_sw
    client_sw = boto3.client('iotsitewise', aws_access_key_id=access_key,
    aws_secret_access_key=secret_key, region_name=region)


#Create Model
#For reference on modelProperties and Hierarchies: 
#https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/iotsitewise.html#IoTSiteWise.Client.create_asset_model
def createModel(model_name, model_description="", model_properties=[], model_hierarchies=[]):
    response = client_sw.create_asset_model(assetModelName = model_name, 
                                            assetModelDescription = model_description,
                                            assetModelProperties = model_properties,
                                            assetModelHierarchies = model_hierarchies)
    assetModelId = response['assetModelId']
    for i in range(30):
            time.sleep(1)
            status = getModelStatus(assetModelId)
            print(status)
            if status == "ACTIVE": break
    return assetModelId

#Retrive all Models
def getModels():
    response = client_sw.list_asset_models()
    responseMetadata = response['ResponseMetadata']  
    return response['assetModelSummaries']

#Find a Model by Name
def getModelByName(model_name):
    models = getModels()
    for model in models:
        if model_name == model['name']: return model
    return None

#Find a Model by ID
def getModelById(model_id):
    models = getModels()
    for model in models:
        if model_id == model['id']: return model
    return None

#Get Model Details
def getModelDetails(model_id):
    response = client_sw.describe_asset_model(assetModelId=model_id)
    responseMetadata = response['ResponseMetadata']
    del response['ResponseMetadata']
    return response

#Find the Hierarchy id by name of the model
def getHierarchyByName(model_id, hierarchy_name):
    model_details = getModelDetails(model_id = model_id)
    for hierarchy in model_details['assetModelHierarchies']:
        if hierarchy['name'] ==  hierarchy_name:
            return hierarchy['id']

#Get all Measurements from a model
def getModelMeasurements(model_id):
    response = client_sw.describe_asset_model(assetModelId=model_id)
    responseMetadata = response['ResponseMetadata'] 
    assetModelProperties = response['assetModelProperties']
    keys = []
    for property in assetModelProperties:
        type = property['type']
        if type.get('measurement') !=None:
            keys.append(property['name'])
    return keys

#Get all Attributes from a model
def getModelAttributes(model_id):
    response = client_sw.describe_asset_model(assetModelId=model_id)
    responseMetadata = response['ResponseMetadata']
    assetModelProperties = response['assetModelProperties']
    keys = []
    for property in assetModelProperties:
        type = property['type']
        if type.get('attribute') !=None:
            keys.append(property['name'])
    return keys

#Retrieve Model Status - 'CREATING'|'ACTIVE'|'UPDATING'|'DELETING'|'FAILED'
def getModelStatus(model_id):
    return getModelDetails(model_id)['assetModelStatus']['state']

#Retrieve the Top Level Assets
def getTopLevelAssets():
    response = client_sw.list_assets(filter='TOP_LEVEL')
    responseMetadata = response['ResponseMetadata']
    del response['ResponseMetadata']
    return response

#Find all assets originated from a Model
def getAssets(model_id):
    response = client_sw.list_assets(assetModelId=model_id)
    responseMetadata = response['ResponseMetadata']
    del response['ResponseMetadata']
    return response

#Retrieve Asset Details
def getAssetDetails(asset_id):
    response = client_sw.describe_asset(assetId=asset_id)
    responseMetadata = response['ResponseMetadata']
    del response['ResponseMetadata']
    return response

#Retrieve Asset Status -  'CREATING'|'ACTIVE'|'UPDATING'|'DELETING'|'FAILED'
def getAssetStatus(asset_id):
    return getAssetDetails(asset_id)['assetStatus']['state']

#Retrieve Asset Proprieties
def getAssetProperties(asset_id):
    properties={}
    assetDetails = getAssetDetails(asset_id)
    for property in assetDetails["assetProperties"]:
        properties[property["name"]] = property["id"]
    return properties

#Create a new Asset based in a model
def createAsset(asset_name, model_id):
    response = client_sw.create_asset(assetName = asset_name, assetModelId = model_id)
    responseMetadata = response['ResponseMetadata']
    asset_id = response["assetId"]
    for i in range(30):
        time.sleep(1)
        status = getAssetStatus(asset_id)
        print(status)
        if status == "ACTIVE": break
    return asset_id
    
#Associate a Alias to a Asset Propriety (Attribute or Measurement)
def associateAssetAlias(asset_id, measurement_id, alias, notification_state='DISABLED'):
    response = client_sw.update_asset_property(
        assetId=asset_id,
        propertyId=measurement_id,
        propertyAlias=alias,
        propertyNotificationState=notification_state
    )
    responseMetadata = response['ResponseMetadata']
    return response

#Associate a Asset to a Parent based on the hierarchy 
def associateAssetHierarchy(parent_asset_id, hierarchy_id, child_asset_id):
    response = client_sw.associate_assets(assetId = parent_asset_id, hierarchyId = hierarchy_id, childAssetId = child_asset_id)
    responseMetadata = response['ResponseMetadata']

#Create a new Asset with automatic association of its measurements
#Alias format is: {root_alias}/{asset_name}/{measumement_name}
def createAndAssociateAsset(asset_name, model_id, root_alias="/"):
    asset_id = createAsset(asset_name, model_id)
    for i in range(30):
        time.sleep(1)
        status = getAssetStatus(asset_id)
        print(status)
        if status == "ACTIVE": break
    properties = getAssetProperties(asset_id)
    listParams = getModelMeasurements(model_id)
    for propName in listParams:
        associateAssetAlias(asset_id, properties[propName], "{}/{}/{}".format(root_alias, asset_name, propName))
    return asset_id

# Get the asset Associations
def getAssociatedAssets(asset_id, hierarchy_id):
    response = client_sw.list_associated_assets(assetId=asset_id, hierarchyId=hierarchy_id)
    del response['ResponseMetadata']
    return response

# Get the hierarchy path from the asset to root
def getHierarchyToRoot(asset_id):
    response = client_sw.list_asset_relationships(assetId=asset_id, traversalType='PATH_TO_ROOT')
    responseMetadata = response['ResponseMetadata']
    del response['ResponseMetadata']
    return response

# Disassociate a child from its parent - hierarchy
def disassociateAssets(asset_id, hierarchy_id, child_asset_id):
    response = client_sw.disassociate_assets( assetId = asset_id, hierarchyId = hierarchy_id, childAssetId = child_asset_id)
    
# Delete a Asset - the asset cannot be assotiates with any other asset
def deleteAsset(asset_id):
    response = client_sw.delete_asset(assetId = asset_id)
    responseMetadata = response['ResponseMetadata']
    return response

# Delete all assets in a hierarchy (Tree)
def deleteAssetsTree(asset_id):
    deleteAssetsTreeHelper(asset_id=asset_id)
    time.sleep(5)
    deleteAsset(asset_id=asset_id)

# Helper for the delete all assets
def deleteAssetsTreeHelper(asset_id):
    assetDetails = getAssetDetails(asset_id = asset_id)
    list_hierarchies = assetDetails['assetHierarchies']
    for hierarchy in list_hierarchies:
        hierarchy_id = hierarchy['id']
        associated_assets = getAssociatedAssets(asset_id = asset_id, hierarchy_id = hierarchy_id)['assetSummaries']
        #print("\ response: {}\n".format(json.dumps(associated_assets, indent=2, default=str)))
        for asset in associated_assets:
             child_id = asset['id']
             deleteAssetsTreeHelper(asset_id=child_id)
             print('disassociate asset: ', asset['name'], child_id)
             disassociateAssets(asset_id=asset_id, hierarchy_id=hierarchy_id, child_asset_id=child_id)
             time.sleep(5)
             deleteAsset(asset_id=child_id)

# Delete all Top Assets - the assets cannot have associations
def deleteTopAssets():
    list_top_assets = getTopLevelAssets()
    for asset in list_top_assets['assetSummaries']:
        deleteAsset(asset_id=asset['id'])

# Delete all assets in the region - BE CAREFUL!!!!!!!
def deleteAllTopAssetsTree(): 
    list_top_assets = getTopLevelAssets()
    for asset in list_top_assets['assetSummaries']:
        deleteAssetsTree(asset_id=asset['id'])
