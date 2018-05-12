# FGOwikiGeter
Get the information of every servent in Fate/Grand Order

## introduction
    To check the data of each servent in Fate/Grand Order when my network crashed, i wrote this code to gather servent information.

## process
- 1 use the module of requests, and get the html file of servent introduction.
- 2 use the powerful module BeautifulSoup to get the content of target script ( because everything we need is in one script), and translate them into instant of class str (for the next match)
- 3 match each content of target script, with regular expression. I used the follow pattern to match
```python
    pattern=re.compile(u'var datadetail = (.*?);$')
``` 
- 4 after matching, I used json to store the result, and then store the result into the database.

## development

- 1, I didn't make the full use of the data, so, more information could be used to do something useful.
- 2, For future supplement