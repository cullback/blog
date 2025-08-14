+++
title = "Watsky words"
+++

Between 2019 and 2023, rapper George Watsky released three albums called Complaint, Placement, and Intention. When arranged next to each other, the titles form a 3x3 word puzzle that can be read across and down:

```
com pla int
pla cem ent
int ent ion
```

In an [interview with Philip DeFranco](https://www.youtube.com/watch?v=6pDUCAgsnKU&t=2562s), Watsky said the following:

> when I worked with this linguist, we plugged the rules of this word puzzle into the english dictionary and it only spit out one possibility of 9-letter words that interlocked in the way we wanted it to...there was only one solution

Let's double check their work.

We start by assembling a list of nine-letter english words:

```bash
$ curl https://raw.githubusercontent.com/cullback/english-wordlist/refs/heads/main/words.csv | rg '^[a-z]{9}$' > words.csv
$ wc -l words.csv
    18841 words.csv
```

Checking all three-word combinations of that list would take a long time ($18841^3=6,688,239,997,321$). We can explore the search space more efficiently by using binary search to find the words with the prefix we want:

```python
import fileinput
from bisect import bisect_left
from collections.abc import Iterator
from itertools import takewhile


def starts_with(words: list[str], prefix: str) -> Iterator[str]:
    left = bisect_left(words, prefix)
    return takewhile(lambda word: word.startswith(prefix), words[left:])


words = sorted(w.rstrip() for w in fileinput.input())
for first in words:
    for third in starts_with(words, first[6:]):
        for second in starts_with(words, first[3:6]):
            if second.endswith(third[3:6]):
                print(f"{first},{second},{third}")
```

Running this gives us 1480 solutions:

```bash
python3 watsky.py words.csv | wc -l
    1480
```

Some of the other album titles Watsky could have chosen include:

```
worshiped
shittiest
pedestals

castrates
traumatic
testicles

prostates
statistic
testicles
```

I think these would have been equally interesting.
