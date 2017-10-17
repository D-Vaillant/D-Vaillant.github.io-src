Title: Ovens, Conveyers, and Queues, Pt. 1
Date: 2017-10-16
Tags: python, modelling
Category: python
Slug: ovens-conveyers-queues
Author: D. Vaillant
Summary: Simple modelling with Python.

A dear friend of mine pointed me towards the simple model that is the namesake of this post: ovens, conveyers, and queues. We define some terms first:

- Object: Ovens, conveyers, queues, and the other sorts of "machines" that we use.
- System: Any number of connected objects.
- Elements: The individual "things" that we feed into our system.

# The Model
All objects of our model have a central idea: they take in elements from one end (the input), do something with those elements, and then put the elements in whatever object they have on the other end (the output). A physical analogue of this is an assembly line - we have a big stockpile of raw materials, we place them on a moving conveyer belt, and we feed them into a machine that takes a certain amount of time to process them before placing them somewhere else.

To faciliate this model we add on several abstract objects which can be easily replaced with other systems. 

## Queues 
A queue is just the CS 101 concept: it has a `enqueue` and `dequeue` methods which take in elements and then releases elements in the same order as they were taken in. The physical analogue is, well, a queue (or "line").

## Conveyers
The physical analogue here is a conveyer belt. Elements are placed on the conveyer belt and take a certain number of steps, ticks, seconds, units-of-time to get to the next element. After a certain number of steps on the conveyer belt, an element is moved to the output object.

Conveyers have no limit to the amount of elements that can be placed on them, although we can choose to implement a *piecewise capacity* - that is, each "space" in a conveyer belt can have up to **n** objects on it at any given time.

## Ovens
The physical analogue here is, well, an oven. Ovens are just conveyers with a *global capacity* - they can take in some number of elements in any order but can have up to **n** elements, where **n** is the global capacity of the oven.

## The Abstract Objects
These aren't part of the model, strictly speaking, but we include them because they make our life easier. They fall into two groups: sources and sinks.

Sources create a stream of elements according to whatever logic we desire. They cannot act as outputs. 

Sinks take in a stream of elements and do nothing else with them. We can log them, if we want, and use them as "data collection" objects to track how the system as a whole is performing.

## Anonymous Elements?
We have not yet touched on an important question about our implementation: are our elements anonymous or do they have identities? That is - is it important that we keep track of which element is which or are they just interchangable units? Our eventual choice here will lead to a difference in implementations - we will begin with anonymous elements and then adapt our implementation to allow for non-anonymity.

# Some Physical Analogues
Okay, so this is all well and good. Let's actually get some intuition as to how these pieces fit together.

## Grocery Store
You have finished shopping at a store and walk towards the express aisle. It takes you 5 minutes to get to the aisle, 5 minutes to checkout, and another minute to exit the store. The checkout line only holds 3 people at a time.

So: We have a conveyer belt with time 5, a queue before the checkout, an oven with time 5 and capacity 3, and a conveyer belt of time 1.

## Grocery Store, Redux
Instead of using only the express aisle we instead have multiple lines open. As it turns out, this is a minor change: it still takes 5 minutes to get to the aisles and one minute to exit the store from the lines. However: we model all of the lines as *one* Oven, with a larger capacity (of 25) but with the same time.

So: We have a conveyer belt with time 5, a queue before the checkout lines, an oven with time 5 and capcity 25, and a conveyer belt of time 1. This is an example of how our objects can abstract away from some physical details and instead treat them as a single coherent thing.

# Closing Comments
Next time: we look into implementing some of these objects in Python! 
