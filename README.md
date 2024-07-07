# README 

This repo takes the output of the UI in github and extrats the peaks (after some smoothing)

---

## USAGE

0. Type the path to the data file in the script...

1. Put the data file somewhere in `INPUT/``

2. Simply run the main script:

```shell
python INTERPRET.py
```

3. The result will be stored as `result.csv` in the folder where the data came from.

---

## INSTALL

Create a `venv`, install all dependencies...

## ISSUES

### The 500 limit

The keys 'data' as well as 'scaledData' both always present values between 0 and 500. This seems to be the range used for the width of the plots, and therefore for all operations in the app. At some point I should retrieve the actual length of the captured section and scale:

- plots
- cuts

into timecode values.

### The out-of-proportion width of the online plot

It seems that there is a minimum lower limit for frames in the onine APP...

- Try different sets, to see if the limit is always the same
- Check out the range of values in the sets I feed the APP
- Add a step in the process, where the values in the csv files are RESCALED to rebase the limit set in the online app and MAKE IT A READABLE PSEUDOTIMECODE AS WELL!

### (Repeated) Feature names

When combining two sets with same names, we encounter trouble!

- Devise a convention to name the features, that includes the subset they belong to, etc.
