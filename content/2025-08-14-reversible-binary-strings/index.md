+++
title = "Reversible binary strings"
+++

We want to send a binary string from a to b, but there's a chance that the string will be reversed during transmission, i.e. `101011` becomes `110101`.

We want a protocol such that we can figure out which orientation is correct.

Information theory suggests we should be able to do this with only one additional bit.

{{ code_block(path="content/2025-08-14-reversible-binary-strings/binary.py", code="python") }}

<!-- - <https://www.astralcodexten.com/p/open-thread-385/comment/124990517> -->
