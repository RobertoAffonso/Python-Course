import webbrowser

webbrowser.open("https://www.python.org", new=2)
webbrowser.open_new("https://www.python.org")
webbrowser.open_new_tab("https://www.python.org")

help(webbrowser)

explorer = webbrowser.get(webbrowser.iexplore)

explorer.open_new("https://www.python.org")
