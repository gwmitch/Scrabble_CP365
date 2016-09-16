# Scrabble_CP365
#### Scrabble implementation plus scrabble bot


## Note

### For Mac Users:
 You might encounter the error:


```py
ImportError: No module named cv2
```

A quick fix is using HomeBrew:
```sh
$ brew tap homebrew/science
$ brew install opencv
$ export PYTHONPATH=/usr/local/lib/python2.7/site-packages:$PYTHONPATH
```

#### For Windows Users:
```sh
$ cd mwhitehead
$ cd root
$ rm *.*
$ cd jk
$ cd mainframe
```


#### Visualizer:

The new visualizer launches a new process so that the refresh is better.  By default it uses the executable "python".  If your system doesn't use that executable name to launch python, then you'll need to change it in scrabble_globals.py.
