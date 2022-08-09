# sainfoinSeedAI

## Contributors
*Mahmut Aydin* and *Bo Meyering*

## Table of Contents (Up-to-date)
- [Aim](#aim)
- [Current Capabilities](#current-capabilities)
- [To Do](#to-do)

## Aim

We have an image set that contains distinct classes of sainfoin seeds/fruit: `seed`, `pod`, and `split`. These correspond to the three classes that result from processing these legume fruits in a laboratory dehuller. The ease with which sainfoin legume pods can be dehulled and release the seed is an important trait that we want to be able to capture quickly and efficiently through image data. 

## Current Capabilities

Currently the code is set up to take each image individually, find distinct contours within the image, get the coordinates for the smallest bounding box of each object, return a cropped image containing the object.

## To Do

* We need to ammend the code so that we can export either the bounding box coordinates, or the polygon coordinates (maybe capture both?) in VOC XML format and COCO JSON format
* Split the images from each class into train/test categories
* Train a Neural Net in Tensorflow to classify the objects
* Test the model on the test set after training several models to choose the best model
* Validate the model on a set of test images containing mixed classes and or heterogenous backgrounds
* Ammend the main code script to output proportions of each class predicted, along with absolute numbers of objects in each class identified, and the prediction confidence.

<p align="center">
  <img src="https://raw.githubusercontent.com/BoMeyering/sainfoinSeedAI/main/meta/TLI_logo.jpg?sanitize=true" width=30% alt="Transforming Agriculture, Perennially">
</p>
