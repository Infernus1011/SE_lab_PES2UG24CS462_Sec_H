# Reflection

This assignment showed me how static analysis tools can identify problems that may not be obvious during a quick read or a normal run of a program. Pylint highlighted code quality and maintainability concerns, Flake8 caught formatting issues, and Bandit drew attention to potentially unsafe patterns.

The most important changes were replacing SQL string formatting with parameterized queries, removing the unnecessary pickle round trip and unused hard-coded password, and improving exception and state handling. I also updated names, documentation, and formatting. These changes made the program clearer and safer while preserving its tower-tracking demonstration.

I learned that analyzer findings need to be read in context. For example, Bandit warns about pickle because deserializing untrusted data can be dangerous; in the original script, the data was serialized and deserialized locally. Removing that unnecessary operation both simplified the code and eliminated the warning.

After updating the code, I ran the demonstration and checked it with all three tools. The fixed version ran successfully, Pylint reported 10.00/10, Bandit reported no issues, and Flake8 passed. In future projects, I would run these tools regularly so that security, style, and maintainability problems are caught early.
