## You must always have at least one element in the history stack
## which is the page that you are currently at.
## For the forward stack, this condition is not necessary.

## Two Stacks
## Time Complexity: O(N) - need to traverse the list for back & forward
## Space Complexity: O(N)
class BrowserHistory:
    def __init__(self, homepage):
        '''
        Initializes the object with the homepage of the browser.
        :type homepage: str
        '''
        # start on the homepage
        self.history = [homepage]
        self.forward_pages = []


    def visit(self, url):
        '''
        Visits url from the current page.
        It clears up all the forward history.
        :type url: str
        :rtype: None
        '''
        self.history.append(url)
        # forward history clears up
        self.forward_pages = []


    def back(self, steps):
        '''
        Move steps back in history.
        :type steps: int
        :rtype: str
        '''
        while steps > 0 and len(self.history) > 1:
            self.forward_pages.append(self.history.pop())
            steps -= 1
        return self.history[-1]


    def forward(self, steps):
        '''
        Move steps future in history.
        :type steps: int
        :rtype: str
        '''
        while steps > 0 and self.forward_pages:
            self.history.append(self.forward_pages.pop())
            steps -= 1
        return self.history[-1]


## List
## Time Complexity: O(1)
## Space Complexity: O(N)
class BrowserHistory:
    def __init__(self, homepage):
        '''
        Initializes the object with the homepage of the browser.
        :type homepage: str
        '''
        # start on the homepage
        self.history = [homepage]
        # maintain the current position
        self.curr = 0
        # mark the end of the list (dynamically resizing)
        self.end = 0


    def visit(self, url):
        '''
        Visits url from the current page.
        It clears up all the forward history.
        :type url: str
        :rtype: None
        '''
        self.curr += 1
        if self.curr < len(self.history):
            self.history[self.curr] = url
        else:
            self.history.append(url)
        # clears up the forward history
        self.end = self.curr


    def back(self, steps):
        '''
        Move steps back in history.
        :type steps: int
        :rtype: str
        '''
        self.curr = max(0, self.curr - steps)
        return self.history[self.curr]


    def forward(self, steps):
        '''
        Move steps future in history.
        :type steps: int
        :rtype: str
        '''
        self.curr = min(self.end, self.curr + steps)
        return self.history[self.curr]
