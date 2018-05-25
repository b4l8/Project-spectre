#! /usr/bin/env python

"""
Global Variable

apilevel        || Python DB API version        || String const 
threadsafety    || module thread safety level   || 0-3 int 
paramstyle      || SQL parameters style         || ref doc

"""

# threadsafety : 0 : totally non shared module
#                1 : thread share module, but connectiong non shared
#                3 : totally thread safe 

"""
Exception               Superclass
                        
StandardError       ||                  || base class
Warning             || StandardError    || Non fatal error
Error               || StandardError    || base class
InterfaceError      || Error            || interface error not database
DatabaseError       || Error            || base class of database errors
DataError           || DatabaseError    || data error ie. out of range
OperationalError    || DatabaseError    || 
IntergrityError     || DatabaseError    || 
IntarnalError       || DatabaseError    || 
ProgrammingError    || DatabaseError    || 
NotSupportedError   || DatabaseError    || 
"""


