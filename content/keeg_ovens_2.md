Title: Ovens, Conveyers, and Queues, Pt. 2
Date: 2017-11-11
Tags: python, modelling
Category: python
Slug: ovens-conveyers-queues-2
Author: D. Vaillant
Summary: Simple modelling with Python.
Status: draft

We continue our discussion from [last time]({filename}keeg_ovens.md) with some implementations. Control your excitement, folks.

# Terminology Reference
- Object: Ovens, conveyers, queues, and the abstract objects (pits, voids, and the various sources)
- System: A connected collection of objects.
- Sources: Objects that create elements. Represent our system's initial point.
- Sinks: Objects that "destroy" elements. Represent our system's terminal point.
- Element: A thing which is passed into objects from a source.

# The Assumptions
We were rather vague on how our pieces might possibly work together. We do not have that luxury now. Instead of tackling the broadest possible implementations we'll start with a narrower one and hopefully work our way up.

## Elements Are Anonymous
This is a big one. We don't care about the identities or the properties of any of our elements: they're just blank units who only have properties in relation to whatever object they happen to occupy. As such, any collection of elements is representable by a natural number. There's "2 people", not "Timothy and Janet, a bickering old couple". 

If we jettison this assumption we would need to implement an "Element" class which holds pertient information. Our sources would need to be able to generate elements in a sensible way.

## Queues Are Infinite
Our first implementation is going to make the following assumptions: queues don't have a limit and they always exist next to a conveyer belt or an oven.

The infinite assumption is so we don't need to worry about "locking up" - no matter how many elements we feed into a system, if we stop feeding in elements and give it enough time it will process all of the objects we fed into it without any loss. We can imagine that supermarket line getting quite long, but as long as everyone stays in the line (and is patient) eventually everyone will get checked out and head home.

If we jettison this assumption we would need to add "capacities" to 


## Queues Don't Exist Alone

# What We're Left With
Queues are infinite, tied to ovens or conveyers, and have no limitations on
