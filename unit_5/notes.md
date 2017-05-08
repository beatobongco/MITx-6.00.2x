# Machine Learning notes

All ML methods require:

* representation of features
* distance metric for feature vectors
* objective functions and constraints
* optimization method for learning the model
* evaluation method

## Supervised learning

Start with set of feature vector/value pairs

Goal is to find a model that predicts a value for a previously unseen feature vector

Regression model predicts a real number (infinite)

Classification models predicts a label (chosen from finite set of labels)

## Unsupervised learning

Start with feature vector, no labels

Goal: uncover latent structure in set of feature vectors

Clustering
 - define metric that captures how similar one feature vector is to another
 - group examples based on this metric

Different structures emerge depending on which features you choose.

## Choosing features

Features never fully describe the situation

Feature engineering
  - represent examples by feature vectors that will facilitate generalization.
  - don't overfit

We want to maximize the signal to noise ratio.
