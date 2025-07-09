# Design and Methodology

## Approach
- I used defaultdict(list) to group words by their sorted key.
- The key for each word is its sorted version (e.g., "race" → "acer").
- This way, all words that consist of the same letters are grouped together.


## Scalability
- For 10 million words:
  - The code performs efficiently in memory as long as the file size is reasonable.
  - We can use generators and stream the file line by line if it gets too large.

- For 100 billion words::
  - The input must be processed in batches..
  - Intermediate results can be stored on disk (e.g., using databases or MapReduce frameworks).
  - Sorting and grouping can be distributed across multiple machines.


## External Libraries
No external libraries were used.
