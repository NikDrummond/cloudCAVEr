# CloudCAVEr

This is just a simple toolbox wrapping some *cloud* volume and *CAVE* client funcitons for programatically getting data from flywire. There are no doubt some (probably better) alternatives, which I will link to below. The idea here is for quick and dirty work with flywire, to handle some functions which may previously have taken multiple steps.

## Requierments

`cloudvolume` is required for pulling EM data from flywire - the segmentation, meshes, skeletons, and image layer. See [here](https://github.com/seung-lab/cloud-volume)
to install:

```
pip install cloud-volume
```
NOTE: although the data from cloud-volume can be freely accessed, if you write a bunch of code and repeatedly access the data automatically, in large quantities, or are in need of a large amount of data, you will spoil it for everyone. It is advised to reach out to the seung lab directly in the case you wish to do this.

`CAVEclient` is required for accessing annotation and status information for flywire reconstructions - proofread status, neuron annotations, connectivity. See [here](https://caveclient.readthedocs.io/en/latest/guide/intro.html) 

to install:

```
pip install caveclient
```

## Client setup

In order to access data from the CAVE client, you need to have a CAVE account. From the [CAVEclient tutorial](https://github.com/seung-lab/FlyConnectome/blob/main/CAVE%20tutorial.ipynb), you can do this like so. It just requires a google account:

<div class="warning" style='padding:0.1em; background-color:#d3d3d3; color:#000000'>
<span>
<p style='margin-top:1em; text-align:center'>
<b>CAVE account setup
</b></p>
<p style='margin-left:1em;'>

Each and every user needs to create a CAVE account and download a user token to access CAVE's services programmatically. FlyWire's data is publicly available which means that no extra permissions need to be given to a new user account to access the data.

A Google account (or Google-enabled account) is required to create a CAVE account.
Start here if you do not have a CAVE account or are not sure

Login to CAVE to setup a new account. To do this go to this [website](https://prod.flywire-daf.com/materialize/views/datastack/flywire_fafb_public).

</p>
<p style='margin-bottom:1em; margin-right:1em; text-align:right; font-family:Georgia'> 
</p></span>
</div>

## Set and save your token

As we are wrapping things together for simplicity, once you have the above things set up, cloud volume and CAVE client are used in the background. However, to access flywire data you need to set up and save a token