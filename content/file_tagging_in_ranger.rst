File Tagging: Wallpapers
#########################
:tags: ranger, tagging, file.organization
:date: 2018-06-13 00:00
:category: file.management
:slug: ranger-file-tagging
:author: DVaillant
:summary: Using file tagging in Ranger.
:status: draft

A project that I've kept coming back to was the idea of `virtual tagging` within a file system. The idea was simple: you use a database, you crawl through some "root directory", you populate a table with rows for each file and you have a many-to-many relationship between Files and Tags (i.e. strings). Some irritations:

- An interface for adding and removing tags without having to just dig around with the database.
- An interface for actually sorting by these tags in some sort of file manager.

Now, this sort of thing isn't novel (luckily) - there are lots of differnet projects that aim at the same thing. I started looking into this with a particular usecase in mind: adding tags through Ranger.

Ranger comes out of the box with "metadata" which are key-value pairs stored in a `.metadata.json` file in a directory. There's a few limitations here: 

- If you move the file, all of the metadata is lost and you need to manually move the entry in the json file to the `.metadata.json` of the new directory.
- There's no non-Ranger interface for dealing with metadata; it's fairly easy to make one (or even just do it manually).
- There isn't a way to actually use this metadata out-of-the-box to do things like "move all files with tag X". It's implementable using Ranger's API.

The first issue is resolved by adding a wrapper around the standard move functions in Ranger. The seocnd issue is just a matter of representing "a function that 
