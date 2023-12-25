import pandas as pd
import numpy as np

def calculate_transition_probabilities(data, states):
    # Initialize a matrix to hold the transition counts
    transition_counts = {state: {next_state: 0 for next_state in states} for state in states}

    # Count transitions for each consecutive state pair
    for idx in range(len(data) - 1):
        for state, next_state in zip(states, states[1:]):
            if data.at[idx, state] == 'Yes' and data.at[idx, next_state] == 'Yes':
                transition_counts[state][next_state] += 1

    # Convert counts to probabilities
    transition_matrix = pd.DataFrame(index=states, columns=states)
    for state in states:
        total_transitions = sum(transition_counts[state].values())
        for next_state in states:
            transition_matrix.at[state, next_state] = (transition_counts[state][next_state] / total_transitions) if total_transitions > 0 else 0

    return transition_matrix

# Generate a random dataset for demonstration
np.random.seed(0)  # For reproducibility
data = pd.DataFrame(np.random.choice(['Yes', 'No'], size=(10000, 5)), columns=["Visited Website", "Signed Up for Newsletter", "Made First Purchase", "Became Repeat Customer", "Churned"])

# Calculate transition probabilities
states = ["Visited Website", "Signed Up for Newsletter", "Made First Purchase", "Became Repeat Customer", "Churned"]
transition_matrix = calculate_transition_probabilities(data, states)

print(transition_matrix)
