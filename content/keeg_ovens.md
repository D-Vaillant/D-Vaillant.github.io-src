Title: Ovens and Conveyors, Pt. 1
Date: 2018-10-16
Tags: python, modelling
Category: python
Slug: ovens-conveyors
Author: D. Vaillant
Summary: Simple modelling, prior to Python.

A dear friend of mine pointed me towards the simple model that is the namesake of this post: ovens and conveyors. We define some terms first:

- Machine: Ovens, conveyors, and the other sorts of "machines" that we use.
- Elements: The individual "things" that we feed into our system.
- System: Any number of connected machines.

# The Model
All machines of our model have a central idea: they take in elements from one end (the input), do something with those elements, and then put the elements in whatever machine they have on the other end (the output). A physical analogue of this is an assembly line - we have a big stockpile of raw materials, we place them on a moving conveyor belt, and we feed them into a machine that takes a certain amount of time to process them before placing them somewhere else.

To facilitate this model we use several abstract machines.

## Elements
The things we input and output from machine to machine. They can be anonymous or not - that is, we might keep track of each element and its properties or we might just use interchangeable units.

## Conveyors
The physical analogue here is a conveyor belt. Elements are placed on the conveyor belt and take a certain number of steps, ticks, seconds, units-of-time to get to the next machine. After a certain number of steps on the conveyor belt, an element is moved to the output machine. We refer to each step as a *stage*, with the first stage being *initial* and the last one being *terminal*.

Conveyors might have no limit to the amount of elements that can be placed on them or we can choose to implement a *piecewise capacity* - that is, each stage in a conveyor belt can have up to **n** elements on it at any given time. We'll explicitly note if a conveyor has piecewise capacities but otherwise assume that they're infinite.

## Ovens
The physical analogue here is, well, an oven. Ovens are just conveyors with a *global capacity* - they can take in some number of elements in any order but can have up to **n** elements, where **n** is the global capacity of the oven. This is just some overhead over a conveyor. 

This allows the possibility of empty stages!

## Sinks and Sources
Sources create a stream of elements according to whatever logic we desire. They cannot intake elements. 

Sinks take in a stream of elements and do nothing else with them. We can log them, if we want, and use them as "data collection" machines to track how the system as a whole is performing. They cannot output elements.

# Some Physical Analogues
Okay, so this is all well and good. Let's actually get some intuition as to how these pieces fit together.

## Grocery Store
You have finished shopping at a store and walk towards the express aisle. It takes you 5 minutes to get to the aisle, 5 minutes to checkout, and another minute to exit the store. If someone is already at the checkout you'll have to wait.

So: We have an conveyor belt with time 5, an oven with time 5 and capacity 1, and an conveyor belt of time 1.

## Grocery Store, Redux
Instead of using only the express aisle we instead have 3 lines open. In this case we have a capacity of 3: the oven can process three people at once in parallel. These people have infinite patience - we'll consider finite patience next time.

So: We have an conveyor belt with time 5, an oven with time 5 and capacity 3, and an conveyor belt of time 1.

# Closing Comments
Next time: we look into implementing some of these machines in Python! 
