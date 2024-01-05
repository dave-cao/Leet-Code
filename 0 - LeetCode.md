---
created: 2023-12-14T00:03
updated: 2024-01-05T12:59
---

# Code Problems Database

## List of all coding problems

```dataview

TABLE WITHOUT ID
	link(file.link, title) as Completed,
	time_elapsed as Time,
	difficulty as Difficulty,
	dateformat(created, "MMM dd, yyyy") as Date
FROM #code_problem 
WHERE !contains(file.path, "Templates")
SORT created DESC
```


## Steps to Solve

- What is data structures and variables do you need to use here?
- What is the brute force method or the easy to approach method?
- Optimize