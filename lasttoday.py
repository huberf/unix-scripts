import webbrowser
import datetime

todayDate = datetime.date.today()
yesterday = todayDate - datetime.timedelta(days=1)
todayLink = "https://www.last.fm/user/nhuberfeely/library?from=" + str(todayDate.year) + "-" + str(todayDate.month) + "-" + str(todayDate.day) + "&page=1&to=" + str(todayDate.year) + "-" + str(todayDate.month) + "-" + str(todayDate.day)
webbrowser.open(todayLink)
