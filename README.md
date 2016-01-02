# Import from `github_com` (Please don't use it)

Experimental Python module finder/loader from github, like in golang.

So, in golang we can import like:

```go
import "github.com/parnurzeal/gorequest"
```

But in python we should install package by our hands:

```bash
pip install requests
```

And import it like:

```python
import requests
```

But with this magic package and power of [PEP-0302](https://www.python.org/dev/peps/pep-0302/) we can
do it automatically:

```python
from github_com.kennethreitz import requests

assert requests.get('https://github.com/nvbn/import_from_github_com').status_code == 200
```

## Installation

You should have git, Python 3.2+ and pip:

```bash
pip install import_from_github_com
```

## License MIT
Project License can be found [here](LICENSE.md).
