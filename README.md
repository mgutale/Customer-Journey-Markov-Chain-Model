# Markov Chain Transition Probability Calculator

## Overview

This Python script calculates the transition probabilities between various states in a Markov chain model. It's useful for modeling customer journeys or similar sequential processes, determining the likelihood of transitioning from one state to another within a dataset.

## Markov Chain and Transition Probability Formula

In a Markov chain, the probability of transitioning from one state to another depends solely on the current state, not on the sequence of events that preceded it. The formula for the transition probability from state `i` to state `j` is:

P(i, j) = Number of transitions from state i to state j / Total number of transitions from state i


## Prerequisites

- Python environment (Python 3.x)
- Pandas and NumPy libraries installed

## Script Functionality

1. **Data Processing**: Iterates through each record to observe state transitions.
2. **Transition Counting**: Counts transitions from each state to every other state.
3. **Probability Calculation**: Applies the Markov chain formula to calculate transition probabilities.
4. **Matrix Construction**: Creates a transition matrix with probabilities of moving from one state to another.

## Using the Script

1. **Dataset Preparation**: Use a Pandas DataFrame with each column representing a state and rows indicating records. Each record should have 'Yes' or 'No' values for each state.
2. **Execution**: Run the script in your Python environment to obtain the transition matrix.
3. **Output**: The script outputs a transition matrix in a Pandas DataFrame format.

## Sample Dataset

A sample dataset is generated in the script for demonstration purposes. Replace it with actual data for practical use.

## Customisation

- Adjust the `states` list to align with your dataset's states.
- Modify the transition counting logic to fit your specific application requirements.

## Important Note

- The script uses a randomly generated dataset for demonstration. Implement it with real data for actual applications.
- The script is set up for sequential transitions. Modify as needed for different transition behaviors.

This README provides guidance on using the script to calculate Markov chain transition probabilities. For specific customizations or additional information, refer to the script's comments or consult Python programming resources.
