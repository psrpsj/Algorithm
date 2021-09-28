# Matching Anything But a Newline

regex_pattern = r"^.{3}\..{3}\..{3}\..{3}$"

# Matching Digits & Non-Digit Characters

Regex_Pattern = r"^.{2}\D.{2}\D.{4}"

# Matching Whitespace & Non-Whitespace Character

Regex_Pattern = r"\S{2}\s\S{2}\s\S{2}"  # Do not delete 'r'.

# Matching Word & Non-Word Character

Regex_Pattern = r"\w{3}\W\w{10}\W\w{3}"  # Do not delete 'r'.

# Matching Start & End

Regex_Pattern = r"^\d\w{4}\.$"  # Do not delete 'r'.
