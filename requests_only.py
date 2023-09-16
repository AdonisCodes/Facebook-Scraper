
# Make The initial request to the page based on the cookies
# Get the first end cursor ( Easy to do )
# Now create a while loop
    # Make a request to the api with the new cursor
    # If the next cursor is none, or has_next_page is false
        # Return
    # If There are posts ( Play around with insomnia to see how much I can exclude )
    # Convert them to post objects
    # Append them to a list
    # Save the newest request to a file ( If we need to start from a specific cursor because of crash
    # Go through each post & append to a csv file ( Build a custom method for that
    # Go through each post & append to a json file
    # Upon network errors retry for at least 10 times.