import time

def Scroll():
    """A method for scrolling the page."""
      
    def run(driver):
      # Get scroll height.
      last_height = driver.execute_script("return document.body.scrollHeight")
  
      while True:
  
          # Scroll down to the bottom.
          driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
  
          # Wait to load the page.
          time.sleep(2)
  
          # Calculate new scroll height and compare with last scroll height.
          new_height = driver.execute_script("return document.body.scrollHeight")
  
          if new_height == last_height:
  
              break
  
          last_height = new_height