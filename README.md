# Sea ice prediction to go
___
## Can we beat complex climate models?
___

# Introduction
The Polar Regions are becoming more important for transportation and resources exploitation. But traveling to the Arctic or Antarctic requires information on the sea ice situation and planning becomes uncertain without having any idea about sea ice evolution in the desired period. Hence, in order to ease planning of any activity in near furture, an easy to handle short-term sea-ice extent forecast has been developed. Sea-ice prediction to go, so to speak.

![alt text](https://github.com/skrutzky/SeaIce_Prediction/blob/master/SeaIcePicture.JPG?raw=true)

**Project goals**
* identify major drivers for sea ice extent changes (in individual sectors)
* build model to predict near-future sea ice extent (SIE)

**Steakholders to be addressed**
* Shipping companies: having a model easy to use helping with ship route planning
* climate researchers/modellers: increased understanding on dependencies in the climate system


# Used modules
Python / Pandas / NumPy / Matplotlib / Seaborn / Basemap / Scikit-Learn / Logistic Regression / XGBoost / PCA  / Time series prediction / SARIMAx  / Google Cloud Platform / TensorFlow

# Conclusions
* SARIMA can beat the naive forecast for a prediction length of 6 months
* for longer predictions, a combination from SARIMA and the Naive model looks promising
* SARIMA predictions of ICA seem to be more appropriate in summer months than CMIP predictions. For SIE, CMIP shows higher variability but often still too low values (summer). However, comparing SIE from CMIP with its low resolution grids and satellite derived SIE with comparatively high spatial resolution is a bit difficult, therefore ICA is a better mean for comparisons.
* predicting sea ice in the Antarctic is more difficult and has higher inaccuracy than in the Arctic

# Outlook
___
* More data cleaning: proof whether abrupt jumps are due to inconsistencies in the data
* Prediction of sea ice using Neural Networks approach
* Consider exogen variables for more precise prediction
* Predict sea ice extent for subregions in the Arctic
* Increase regional investigation by predicting sea ice concentration 

