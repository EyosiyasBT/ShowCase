# Accountability Module: Increasing Trust in Reinforcement Learning Agents

**MSc Thesis - University of Oslo, 2023**

## Abstract

Artificial Intelligence requires trust to be fully utilised by users and for them to feel safe while using them. Trust, and indirectly a sense of safety, has been overlooked in the pursuit of more accurate or better-performing black box models. The field of Explainable Artificial Intelligence and the current recommendations and regulations around Artificial Intelligence require more transparency and accountability from governmental and private institutes.

Creating a self-explainable AI that can be used to solve a problem while explaining its reasoning is challenging to develop. Still, it would be unable to explain all the other AIs without self-explainable abilities. It would likely not function for different problem domains and tasks without extensive knowledge about the model.

The solution proposed in this thesis is the **Accountability Module** - an external explanatory module designed to function with different AI models in different problem domains. The prototype was inspired by accident investigations regarding autonomous vehicles but was created and implemented for a simplified simulation of vehicles driving on a highway. The prototype's goal was to attempt to assist an investigator in understanding why the vehicle crashed.

The Accountability Module found the main factors in the decision that resulted in an accident. It was also able to facilitate the answering of whether the outcome was avoidable and if there were inconsistencies with the agent's logic by examining different cases against each other. The prototype managed to provide useful explanations and assist investigators in understanding and troubleshooting agents.

The thesis and the Accountability Module indicate that a similar explanatory module is a robust direction to explore further.

## Research Questions

| Symbol | Research Objective | Method |
|---|---|---|
| α | What were the main factors in the decision? | Saliency Maps |
| β | Would changing a factor lead to a different decision? | Evolutionary Algorithm |
| γ | Why did two similar cases get different decisions? | UMAP + Counterfactuals |

## Tech Stack

Python, PyTorch, stable-baselines3, DQN, highway-env, UMAP, Ray, CUDA

## Thesis

[Eyosiyas_Master.pdf](./Eyosiyas_Master.pdf) (130 pages)
