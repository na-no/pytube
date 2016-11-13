#!/usr/bin/env/python
import re
import webbrowser

#sandusky

#removes things that prevent viewing
print "Input YouTube URL: "
youtubeURL = raw_input()


#replaces '=' with '/'
#removes 'watch?'
#loop?
#re.sub(r'watch\?', '', youtubeURL)

print "\n"
edit_URL1 = re.sub(r'=', '/', youtubeURL)
print "Tweaking...", edit_URL1
edit_URL2 = re.sub(r'watch\?', '', edit_URL1)
print "Tweaked:", edit_URL2

if edit_URL2 == "v=":
    edit_URL3 = re.sub(r'v=', 'v/', edit_URL2)
    print "Tweaked:", edit_URL3
    print edit_URL3

#Link to specific playback point
"""
add #t = at end of video URL followed by minute you want with (#m#s)
ex. #t=01m18s, or #t =78s
print ("Set link to specific playback point? y/n")
userreply = raw_input()
if userreply == 'y':
    print "OK"
    playbackminute = input("Set playback minute in ##m: ")
    playbacksecond = input("Set playback second in ##s: ")
    playbacksyntax = "#t=" + str(playbackminute) + str(playbacksecond)
    def playbackset(edit_URL3, playbacksyntax):
        playbackset = edit_URL3 + playbacksyntax
        webbrowser.open(playbackset)
elif userreply == 'n':
    print "ACTION TERMINATED"
else:
    print "INVALID"
    """


print "\n"
proceed_message = "Open URL with web browser? (y/n)"
print proceed_message

user_response = raw_input()
if user_response == 'y':
    webbrowser.open(edit_URL2)
elif user_response == 'n':
    print ("Action terminated.")
else:
    print proceed_message

print "\n"
playback_message = "Set link to specific playback point?"
userreply = raw_input()
if userreply == 'y':
    print "OK"
    playbackminute = input("Set playback minute in ##m: ")
    playbacksecond = input("Set playback second in ##s: ")
    playbacksyntax = "#t=" + str(playbackminute) + str(playbacksecond)
    def playbackset(edit_URL3, playbacksyntax):
        playbackset = edit_URL3 + playbacksyntax
        webbrowser.open(playbackset)
elif userreply == 'n':
    print "ACTION TERMINATED"
else:
    print "INVALID"
