 def countsubstring(s1, s2):
    # Base case: if s2 is shorter than s1, s1 can't be in s2
    if len(s2) < len(s1):
        return 0

    # If the substring at the beginning matches s1
    if s2[:len(s1)] == s1:
        # Count 1 and continue checking from the next character
        return 1 + countsubstring(s1, s2[1:])
    else:
        # Otherwise, just move one character ahead and continue
        return countsubstring(s1, s2[1:])
print(countsubstring('ab', 'cabalaba'))
