#!/usr/bin/env/python

import webbrowser

print("Input YouTube URL: ")
youtubeURL = raw_input()


playback_message = "Set link to specific playback point? (y/n)"
print playback_message
userreply = raw_input()
if userreply == 'y':
    print "OK"
    playbackminute = input("Set playback minute in ##m: ")
    playbacksecond = input("Set playback second in ##s: ")
    playbacksyntax = "#t=" + str(playbackminute) + str(playbacksecond)
    playbackset = youtubeURL + playbacksyntax
    webbrowser.open(playbackset)
elif userreply == 'n':
    print "ACTION TERMINATED"
else:
    print "INVALID"
