#! /usr/bin/env python

# A rule must : 
#               ditinguish which kind of block it applies
#               apply on the block

# so rule object should have 2 method : condition , aciton


"""
Rule list:
    heading : block that is only a sigle line. at most 70 char. if end with : , not title
    
    title : first block of the text, must be a title
    
    listitem : block begins with (-)
           it begins between the first non-list block and list 
           it ends between the last list item and non-list block.
"""


class Rule:
    """
    General class that def some general rule. 
    sub class take responsiblity to condition()
    """
    def action(self, block, handler):
        handler.start(self.type)
        handler.feed(block)
        handler.end(self.type)
        return True


class HeadingRule(Rule):
    """
    line at most 70 char and not end with :
    """
    type = 'heading'
    def condition(self,block):
        return not '\n' in block and len(block)<=70 and not block[-1] == ':'
        
        

class TitleRule(HeadingRule):
    """
    first block of the text and is a heading 
    """
    type = 'title'
    first = True
    def condtion(self,block):
        if not self.first:return False
        self.first = False
        return headingRule.condition(self,block)
        
class ListItemRule(Rule):
    """
    listitem begins with '-'. it will be deleted when applying the rules
    """ 
    type = 'listitem'
    def condition(self,block):
        return block[0]=='-'
    def action(self,block,handler):
        handler.start(self.type)
        handler.feed(block[1:].strip())
        handler.end(self.type)
        return True
        
class ListRule(ListItemRule):
    """
    list starts between non-list block and first listitem
    list ends between the last list item and non-list block.
    """
    type = 'list'
    inside = False
    def condition(self,block):
        return True
    def action(self,block,handler):
        if not self.inside and ListItemRule.condition(self,block):
            handler.start(self.type)
            self.inside = True
        elif self.inside and not ListItemRule.condition(self,block):
            handler.end(self.type)
            self.inside = True
        return False
        
class ParagraphRule(Rule):
    """
    all rest block not defined 
    """
    type = 'paragraph'
    def condition(self,block):
        return True

        
        
        

