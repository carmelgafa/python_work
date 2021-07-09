# Bet: A supervised task can be simplified by dividing the dataset in clusters according to features and then generating different supervised models for each cluster

## Abstract

Idea is to:

- Select the two most important features using PCA
- Use the features to divide the dataset into clusters (max 3)
- Generate supervised models (Regression) for each cluster
- Compare result with un-clustered dataset
- Compare result with better supervised learning algorithms

## Datasets Used
- [Concrete Compressive Strength Data Set](https://archive.ics.uci.edu/ml/datasets/concrete+compressive+strength)

## Reading

- [A STEP-BY-STEP EXPLANATION OF PRINCIPAL COMPONENT ANALYSIS (PCA)](https://builtin.com/data-science/step-step-explanation-principal-component-analysis)
- [Cluster-then-predict for classification tasks](https://towardsdatascience.com/cluster-then-predict-for-classification-tasks-142fdfdc87d6)
