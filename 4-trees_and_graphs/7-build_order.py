'''
You are given a list of projects and a list of dependencies (which is a list of pairs of projects, where the second project is independent of the first project). All of a project's dependencies must be built before the project is. Find a build order that will allow the projects to be built. If there is no valid build order, return an error.

EXAMPLE:
INPUT:
  projects: a, b, c, d, e, f
  dependencies: (a, d), (f, b), (b, d), (f, a), (d, c)
OUTPUT: f, e, a, b, d, c

APPROACH 1 - topological sort algorithm
APPROACH 2
- DFS to find the build path
- when we get to the end of the path and can't go any further, we know those terminating nodes can be the last projects to be built
- think about cycles -- don't want to get stuck in an infinite route

'''
