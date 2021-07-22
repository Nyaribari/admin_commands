import  delorean
datetime_strings = ["July 25th 2008","October 6th 2012","September 19th 2013","August 11th, 1992", "April 28th, 2052"]
    
for date in datetime_strings:
    delorean_object = delorean.parse(date)
    human_date = delorean_object.humanize()
    print(human_date)