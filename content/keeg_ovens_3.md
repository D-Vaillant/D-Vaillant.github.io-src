Title: Ovens and Conveyors, Pt. 3
Date: 2018-12-03
Tags: python, modeling
Category: python
Slug: ovens-conveyors-3
Author: D. Vaillant
Summary: Python implementations of the oven/conveyor models.
Status: draft

If you have no idea what's going on here, a look at [the introduction to the topic]({filename}keeg_ovens.md) and [more discussion on it]({filename}keeg_ovens_2.md) may help clarify.

# The Machine Class
This is just for conceptual clarity. All machines:
* Do something each tick.
* May or may not take inputs or outputs.
* May have an incoming machine and/or an outgoing machine.

```python
class Machine:
    def __init__(self, *args, inc_machine=None, out_machine=None, **kwargs):
        self.incoming_machine = inc_machine
        self.outgoing_machine = out_machine

    def tick(self):
        raise NotImplementedError

    def intake(self, input):
		pass

	def output(self):
		pass

```

# Implementing Conveyors
We need to specify the following properties: The time, the piecewise capacities, and then incoming and outgoing machines. We'll represent the internal state as just a list.

```python
class Conveyor(Machine):
    def __init__(self, structure, outgoing_machine=Sink()):
        """ Structure is a list of non-negative integers that specifies
        piecewise capacity. 
        If 0 is given, that space has infinite capacity. """
        super().__init()
        self.structure = structure
        self.line = list()*len(structure)
```

On each tick we want to do the following:
* Pass elements from the terminal stage into the outgoing machine
* Advanced each element one stage, if possible

I'm not going to lie: there was a lot of trial and error here.
