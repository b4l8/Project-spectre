#! /usr/bin/env python

quit = False
while quit == False :
    review = raw_input("my input:")
    assert review != 'bye', "Quit by user"
    reviewed=review.replace('fuck','****')
    print reviewed

