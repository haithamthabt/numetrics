# Numetrics

Numetrics is a small package that has some functions regarding checking the performance of a model's predictions.

## Version

Relase `v0.0.1`

### Why did I create Numetrics?
1. The first reason is: I want to contribute to the Numerai community. I have learned a lot from Arbitrage, JRB, Wigglemuse, Michael Oliver, the team, and everybody in the community. 
2. The second reason is: I was tired of copying and pasting my code throughout my notebooks, so I decided to create a package to make it easier for me to just install it through pip

### How to install Numetrics?

You can install it with pip

```python
pip install numetrics
```

```python
import numetrics
```

### How to use Numetrics?
You have one function called ` diagnose ` this is the main function that does all the magic.
It takes a dataframe of your prediction. Prediction dataframe must have the following
- The id
- target column
- era
- predicton column

you can just pass only the predicton dataframe 
```python
 numetrics.diagnose(preds_df)
 ```

or you can spicify the target name and the predicton name 
```python
 numetrics.diagnose(preds_df,TARGET_NAME='target',PREDICTION_NAME='prediction_kazutsugi')
 ```


### See the example file to learn how to use this package.

#### This is the first version/draft/attempt of the package. The code does not look pretty and it still missing lots of functionalities. However, I promise I will do my best to make it better ASAP. 

#### Feel free to contribute to this package.
