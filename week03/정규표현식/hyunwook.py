# Capturing & Non-Capturing Groups
Regex_Pattern = r'(ok){3,}'

# Alternative Matching
Regex_Pattern = r'^(Mr\.|Mrs\.|Ms\.|Dr\.|Er\.)[a-zA-Z]+$'

# Matching Word Boundaries
Regex_Pattern = r'\b[aeiouAEIOU][a-zA-Z]*\b'

# Matching Character Ranges
Regex_Pattern = r'^[a-z][1-9][^a-z][^A-Z][A-Z]'

# Matching Specific Characters
Regex_Pattern = r'^[123][120][xs0][30Aa][xsu][.,]$'

# Excluding Specific Characters
Regex_Pattern = r'^[^0-9][^aeiou][^bcDF]\S[^AEIOU][^.,]$'