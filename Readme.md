# Upgrade your print statements

<p align="centre">
<img src="./docs/morpheus.jpg" alt="print statement meme" width="700">
</p>


## Loggers are like print() statements
except they also include [loads of other metadata](https://docs.python.org/3/library/logging.html#logrecord-attributes):

&ensp;&ensp; - timestamp<br />
&ensp;&ensp; - args (values or variables put into functions)<br />
&ensp;&ensp; - Function name<br />
&ensp;&ensp; - level (e.g. DEBUG)<br />
&ensp;&ensp; - line number (e.g line 42)<br />
&ensp;&ensp; - msg (same as print!)<br />
&ensp;&ensp; - module (which python script it came from)<br />
&ensp;&ensp; - processes (getting fancy)<br />
&ensp;&ensp; - threads (getting very fancy)<br /><br />

## Where do I start?

There are loads of online articles but very few clearly explain how to configure complex loggers with filters and yaml files. This repo comes bundled with tidy logging configuration files saved in `src/logconfig/`.<br />
There is also a timing decorator in `src/utils/` so you can optimize your code by simply decorating your function with `@timing` above it.
<br />
To see loggers in action, setup a virtual environment and then run `main.py`

## Requirements

 * Python 3.7+

<sup>(I haven't tried any earlier version as of 21st November 2021)</sup>

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

The output reflects the yaml file format settings:

```bash
2021-11-21 15:43:47,689 DEBUG - [module01.py: line 17] - funccalc - something executed
```


### loggers
@TODO describe root loggers and their inheritance
```json
root:
  level: DEBUG
  handlers: [console, debug_file_handler, info_file_handler, warn_file_handler, error_file_handler, critical_file_handler, root_file_handler]
```

<p align="center">
  <img src="./docs/rootlogger.png" alt="root logger yaml" width="800">
</p>

### handlers
@TODO describe handlers and how they redirect bytes

### filters
@TODO describe how filters only allow bytes to handlers if a condition is true. reference filter classes in logconfig.py


</details>

## References
Docs: https://docs.python.org/3/library/logging.html#module-logging
lots of logging examples: https://zetcode.com/python/logging/
timeit vs decorator: https://stackoverflow.com/questions/1622943/timeit-versus-timing-decorator
real python uses perf_counter: https://realpython.com/lessons/timing-functions-decorators/
What are decorators: https://gist.github.com/Zearin/2f40b7b9cfc51132851a
Decorators can be reinforced to accept args: https://stackoverflow.com/questions/653368/how-to-create-a-python-decorator-that-can-be-used-either-with-or-without-paramet

