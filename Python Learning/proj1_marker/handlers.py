#! /usr/bin/env python


class Handler:
    """
    process objects from parser
    
    in every block . call start() at the beginning and call end at the end.
    chosing correct block name as args. 
    
    sub() is to chose a correct replace function for re.sub()
    """

    def callback(self,prefix,name,*args):
        """
        given a prefix or name, search for a right method. None as default.
        If callable, the object will be called by extra args
        """
        method = getattr(self,prefix+name,None)
        if callable(method): return method(*args)
    def start(self,name):
        "prefix = start_ "
        self.callback('start_',name)
    def end(self,name):
        "prefix = end_ "
        self.callback('end_',name)
    def sub(self,name):
        """
        return a function that: this function will be the replace function in re.sub()
        """
        def substitution(match):
            result = self.callback('sub_',name,match)
            if result is None: match.group(0)# group(0) : original group
            return result
        return substitution
        
        
class HTMLRender(Handler):
    """
    generate basic tags for HTML
    """
    def star_document(self):
        print '<html><head><title>...</titl></head></body>'
    def end_document(self):
        print '</body></html>'
    def start_pargraph(self):
        print '<p>'
    def end_paragraph(self):
        print '</p>'
    def start_heading(self):
        print '<h2>'
    def end_heading(self):
        print '</h2>'
    def start_list(self):
        print '<ul>'
    def end_list(self):
        print '</ul>'
    def start_listitem(self):
        print '<li>'
    def end_listitem(self):
        print '</li>'
    def start_title(self):
        print '<h1>'
    def end_title(self):
        print '</h1>'
    def sub_emphasis(self,match):
        return '<em>%s</em>'%match.group(1)
    def sub_url(self,match):
        return '<a href="%s">%s</a>'% (match.group(1),match.group(1))
    def sub_mail(self,match):
        return '<a href="mailto:%s">%s</a>'%(match.group(1),match.group(1))
    def feed(self,data):
        print data
        
