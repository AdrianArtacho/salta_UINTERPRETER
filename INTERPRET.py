import gui.gui_browse as gui_browse
import plot_time_series
import analyze_json

json_path = gui_browse.main(params_title='Browse files', 
         params_initbrowser='INPUT',
         params_extensions='.json',               # E.g. '.csv'
         size=(40,20),
         verbose=False)

print("json_path:", json_path)


# exit()
peaks = plot_time_series.main(json_path)
print(peaks)

analyze_json.main(json_path)

