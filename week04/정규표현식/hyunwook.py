# Positive Lookahead
Regex_Pattern = r'o(?=oo)'

# Negative Lookahead
Regex_Pattern = r"(.)(?!\1)"

# Positive Lookahead
Regex_Pattern = r"(?<=[13579])\d"

# Negative Lookahead
Regex_Pattern = r"(?<![aeiouAEIOU])."

# Backreferences To Failed Groups
Regex_Pattern = r"^\d\d(-?)\d\d\1\d\d\1\d\d$"

# Matching Same Text Again & Again
Regex_Pattern = r'([a-z])(\w)(\s)(\W)(\d)(\D)([A-Z])([a-zA-Z])([aeiouAEIOU])(\S)\1\2\3\4\5\6\7\8\9\10'