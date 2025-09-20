+++
title = "Reversible binary strings"
draft = true
+++

Barcodes carry encode 12 decimal digits of information, with one extra checksum digit. That's 1 trillion different values, or just under 40 bits of information.

A barcode uses 84 bits to encode this instead. Part of this is so the scanner knows if it's reading the barcode upside down or not.

Given a binary string, we want to design an encoding such that we can tell whether it has been flipped upside down or not.

For example, if we have `101011`, we want to transform it

The naive solution would be to always prepend a `0` to the front and `1` to the end. Then if our message starts with a `1`, we know it's been reversed.

Information theory suggests we should be able to do this using only 1 additional bit of information.

We'll split the problem up into cases of even and odd length messages.

## Even case

I find the even case easier than the odd case. For starters, we can insert a bit into the middle of the string, and the receiver can extract it unambiguously.

What should we store there to encode an orientation?

We walk the message from both ends and find the index first bits that differ, e.g.

```
110001
^    ^ - same at index 0
 ^  ^  - different at index 1
```

so the index is `i`. Now we store the bit at index i in the message, so the "encoded" message becomes

```
1101001
   ^- insert msg[i]
```

When the reveiver receives the message, they walk the pairs outside in again. When they encounter bits that differ, they just check the middle bit to see which orientation is correct.

If no pairs differ, our message is a palindrome and we can store any bit in the middle as the message will be the same in either orientation.

## Odd case

The odd case is trickier because when we insert a bit, the middle is two bits and it's unclear which one we should read.

We do the same thing and find the index where pairs differ.

```
01100
```

i=1
msg[i] = 1
insert to left of middle

```
01_100
010100
```

what to insert?
if msg[i]=0 then msg[n] else !msg[n]

on receive
head=recv[:n-1]=01
mid1=recv[n-1]=0
mid2=recv[n]=1
tail=recv[n+1:]=00
mid1 == mid2 => msg[i]=0
mid1 != mid2 => msg[i]=1

if msg[i] == expected
head+mid2+tail=01100

{{ code_block(path="content/2025-08-14-reversible-binary-strings/binary.py", code="python") }}

<!-- - <https://www.astralcodexten.com/p/open-thread-385/comment/124990517> -->
<!-- https://medium.com/datascience-semantics3/why-the-u-in-upc-doesnt-mean-universal-a1a675eea0ea -->
