---
created: 2023-12-14T00:03
updated: 2023-12-14T01:22
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
SORT file.ctime DESC
```

