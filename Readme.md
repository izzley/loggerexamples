# Upgrade your print statements
<p>
<img src="./docs/morpheus.jpg" alt="print statement meme" width="400" align="centre" style="padding-right: 30px; padding left: 20px;">
<p>



Logging does exactly what print statements do except better. They include [loads of other metadata](https://docs.python.org/3/library/logging.html#logrecord-attributes) like:

* timestamp
* args (values or variables put into functions)
* Function name
* level (e.g. DEBUG)
* line number (e.g line 42)
* msg (same as print!)
* module (which python script it came from)
* processes (getting fancy)
* threads (getting very fancy)

## Where do I start?

There are loads of online articles but not many address how to configure complex loggers with filters and yaml files. This repo comes bundled with tidy logging configuration files - look at the `logconfig/` folder.<br />
There is also a timing decorator in `utils/` so you can optimize your code just by putting `@timing` above your function.
<br />
To see loggers in action, setup a virtual environment and then run `main.py`

## Requirements

 * Python 3.7+

<sup>(I haven't tried any earlier version)</sup>

## Quickstart - Git clone and virtual env setup

<details>
<summary>Quickstart Instructions</summary>

--- 
<br>

## Windows using powershell or CMD

cd to clone directory. Create virtual env with pip + venv:

```powershell
git clone https://github.com/izzley/loggerexamples
cd loggerexamples\
py -0p # Optional: check your version and python path
py -m venv .venv
.venv\Scripts\activate
pip install --upgrade pip
pip install -r requirements.txt

# run main script
.\src\main.py
```

## Linux/Mac

```sh
cd /to/clone/location
git clone https://github.com/izzley/loggerexamples
cd loggerexamples/
python3 -m venv .venv
source .venv/bin/activate
pip install --upgrade pip
pip install -r requirements.txt
```

If your relative imports aren't working, create `.pth' and add the 
parent folder/s to the file:

```
$ echo $(pwd) >> .venv/lib/python3.8/site-packages/my_p_ext.pth
```

</details>
<br>

## Whats in the YAML file??

<details>
<summary>YAML parts</summary>

--- 
<br>

In short, the `conf.YAML` file contains all of the instructions for how the logger should behave. Below breaks down the conf yaml file into its parts:
### formatters


```json
formatters:
    standard:
        format: "%(asctime)s %(levelname)s - [%(filename)s: line %(lineno)s] - %(funcName)s - %(message)s"
```

Take this logger for example:
```{python}
def funccalc(n):
    logger.debug("something executed")
    for _ in range(n):
        i = 0
    return
```
The output reflects the yaml file formatting: formatters > standard > format

```bash
2021-11-21 15:43:47,689 DEBUG - [module01.py: line 17] - funccalc - something executed
```


### loggers

```json
root:
  level: DEBUG
  handlers: [console, debug_file_handler, info_file_handler, warn_file_handler, error_file_handler, critical_file_handler, root_file_handler]
```

<p align="center">
  <img src="./docs/rootlogger.png" alt="root logger yaml" width="800">
</p>

### handlers

### filters


</details>

## References

- https://zetcode.com/python/logging/