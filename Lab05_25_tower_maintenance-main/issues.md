| Issue | Type | Line(s) | Description | Fix Approach |
|:--|:--|:--:|:--|:--|
| SQL query uses string formatting | Security - Medium<br>Bandit B608 | 11 | `site` is interpolated into SQL, which may allow SQL injection. | Use `?` placeholders and pass values separately. |
| Pickle serialization/deserialization | Security - Medium<br>Bandit B301, B403 | 1, 43 | Bandit warns that loading untrusted pickle data can execute code. This code only deserializes data it just serialized locally. | Remove the unnecessary pickle round trip; return the fetched rows directly. |
| Hard-coded password | Security - Low<br>Bandit B105 | 6 | A password is written directly in source code; it is currently unused. | Remove it, or load credentials securely if they are required. |
| Broad exception handler | Code quality<br>Pylint W0718 | 20 | Catching all exceptions can hide unexpected errors. | Catch the expected database exception or let unexpected errors surface. |
| Missing docstrings / non-standard names | Code quality<br>Pylint C0114, C0116, C0103 | 1, 10, 15, 25, 34, 42, 46 | Module/function docstrings are missing, and some function names are not `snake_case`. | Add concise docstrings; rename functions and update their call sites. |
| Long lines / formatting | Style<br>Pylint C0301; Flake8 E501, E303, E225 | 5, 11, 18, 25, 35, 43, 50 | Reports flag long lines, excess blank lines, and missing operator spacing. | Wrap long statements and correct spacing and blank lines. |
| Global state / unnecessary `else` | Code quality<br>Pylint W0603, R1705 | 16, 36 | `service_count` is modified globally; an `else` follows a `return`. | Avoid the global update where practical; remove the redundant `else`. |
