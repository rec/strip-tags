#!/usr/bin/env python

from BeautifulSoup import BeautifulSoup
 
def strip_all_tags(html):
  return html and ''.join(BeautifulSoup(html).findAll(text=True)) 

def join_inputs():
  results = []
  while True:
    try:
      results.append(raw_input())
    except EOFError:
      return ''.join(results)

print(strip_all_tags(html))
