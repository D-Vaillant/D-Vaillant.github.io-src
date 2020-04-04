Title: Ovens and Conveyors, Pt. 2
Date: 2018-12-02
Tags: python, modeling
Category: python, data structures
Slug: ovens-conveyers-2
Author: D. Vaillant
Summary: More discussion of models. Still prior to Python.
Status: draft

We continue our discussion from [last time]({filename}keeg_ovens.md) with some implementation details. Control your excitement, folks. 

# Terminology Reference
- Machine: Ovens, conveyors, and the abstract machines (pits, voids, and the various sources)
- System: A connected collection of machines.
* Stage: A "step" within a machine. Each element moves up one stage per tick.
* Tick: A discrete unit of time.
- Sources: Machines that create elements. Represent our system's initial point.
- Sinks: Machines that "destroy" elements. Represent our system's terminal point.
- Element: A thing which is passed into machines from a source.
- Global capacity: The total amount of elements that can be processed by an machine (at the same time)
- Piecewise capacity: The amount of elements that can be processed at each stage by an machine (at the same time)

# Implementation Considerations
We were rather vague on how our pieces might possibly work together. We do not have that luxury now. 

## The Anonymity of Elements
This is a big one. We care about the identities and the properties of our elements: they're individuals and should be tracked separately. We can implement an `Element` class and subclass it for whatever kind of element we want to represent (whether they be golf clubs or golfers).

If we jettison this assumption we would have blank units who only have properties in relation to whatever machine they happen to occupy. As such, any collection of elements is representable by a natural number. There's "2 people", not "Timothy and Janet, a bickering old couple". This could be a property of whatever machine they're a part of. The advantage here would just be less overhead since instead of tracking 100 different Element instances you just have "100".

And then, a hybrid solution: we can have `MultipleElements` where each instance corresponds to multiple elements. Each instance is a "wrapper" around a number of elements which all have identical properties. All of our golf clubs in a particular batch, for example. The `Element` class then becomes a subclass since it's just the case where the number of elements is 1. But we run into annoyances when it comes to the consolidation and breaking up: if we want to take 3 elements from a `MultipleElement` then we need to make another one and mutate the previous one.

We're going to just use Elements here, for the sake of simplicity.

## The Capacity of Conveyors
Conveyors might be infinite and hold elements for an infinite length of time. This is accomplished by having the initial stage, where elements go right after the previous machine, have an infinite piecewise capacity.  We can imagine a supermarket line getting quite long, but as long as everyone stays in the line (and is patient) eventually everyone will get checked out and head home. If the initial stage is finite then we might end up with some locking up if too many elements are introduced at once but as long as at least one stage is infinite then eventually we can solve that locking.

There's a lot of minutia possible here with piecewise capacities. We'll deal with that later.

Another consideration is "dropping" elements. People are going to go home instead of waiting in line. This will be done by the Conveyor modifying element properties to track how long they've been in each particular stage. Maybe they're dropped after a cumulative amount of time or maybe they're dropped after spending too long in one particular stage. A

Another drop possibility is dropping as soon as we lock up. This can either be throughout or at the terminal or initial stages or wherever. If it doesn't fit, it falls off.

These considerations apply to ovens as well.

## Sinks and Sources
If our sink isn't infinite, we put a conveyor in front of it. We need an infinite sink at the end of our system. I leave this as an exercise for the reader.

Sources can generate elements by any rule they want. They cannot output into a conveyor that locks up unless we want to specify dropping and/or infinite buffer capacity for the source (which is a possibility). But I'd rather have sources simply output elements and nothing more - the oncoming conveyor must figure out what to do with elements if it fills up or have an infinite initial stage and never fill up.

## Parallel Tracks
First: Does this even make sense? As shown in the grocery redux example from last time we can model parallel lines by having a conveyor with a piecewise capacity above 1. 

But what about the case where these parallel lines go off to different machines? We'd need a *junction* here - a machine which takes elements and outputs them to different systems based on some criteria. They would be a type of conveyor with an additional rule that outputs them to one of many systems.

If we think about junctions using element properties as criteria we find that they act as *sorting machines* as well - a junction that outputs defective products into a sink, for example.

# Next Time
We'll actually program this in Python.
