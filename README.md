# Test task

Test task has three units:

* Data downloading unit (will download data according to the spec)
* Data rendering unit   (will render downloaded data according to the spec)
* Live rendering unit   (will render downloaded data and maintain search on it)

Test task uses the following OSS libraries:

* Pytest
* Requests
* PureCSS/WireframeCSS
* Pystache
* Flask
* Fire

This task uses DI and tests are done via mocking 
downloader (in order to not to hit Google too much)

## How to install

### Set up virtualenv and install requirements

```shell

git clone https://github.com/MichaelLeachim/____testTaskMagetic; 
virtualenv venv;
source venv/bin/activate; 
pip install -r reqs.txt;

```

## How to run 

### First task

Will download data according to spec.
Parameter `--save_to` is optional

```shell

python main.py downloadData --save_to='workdata/data.txt'

```


#### Sub unit (format according to spec)

In order to format downloaded data according to 
the spec, use the following command
Parameters `--path` and `--input_data` are optional

```shell

python main.py formatAccordingToSpec --path=workdata/data.output.txt  --input_data=workdata/data.txt

tail workdata/data.output.txt;
# GAME_WORD/com.zynga.words
# GAME_WORD/com.zynga.wwf2.free
# GAME_WORD/com.zytoona.wordscrush
# GAME_WORD/de.lotum.whatsinthefoto.us
# GAME_WORD/es.socialpoint.wordlife
# GAME_WORD/mindware.wordgames
# GAME_WORD/se.maginteractive.rumble
# GAME_WORD/se.maginteractive.rumble.free
# GAME_WORD/se.maginteractive.wordbrain
# GAME_WORD/ws.letras

```


### Second task

Will translate downloaded data into a HTML template
Parameters `--path` and `--input_data` are optional

```shell

python main.py showInTemplate --path=workdata/output.html  --input_data=workdata/data.txt

```

### Third task

Will run a flaks app that allows filtering by the
search parameter.


Parameter `--port` is optional

```shell

python main.py runHTTPServer --port=8000
# For example

wget 127.0.0.1:8000/?search=racing

```

# How to test

```shell

pytest . 


```



# Questions [DEPRECATED]

* General questions.  When I finish. Do I upload to github? 

* Should I get it live, or can I download data and use it 
  * What if it starts showing captcha for requests?
* Find game by name:
  * Is (the search) cased? 
  * Is (keyword search) cased?
* Second one: 
  * Print as HTML table, right? 
  
  
