import csv

def domain_builder(search, section): 
    """
    Return 0: Array of domains
    Return 1: Array of cities
    
    Builds the Craigslist URL's for each city in 'city.csv'

    Some options for sorting your craigslist are found below,
    more options can be found in readme.txt and the rest can
    be found simply by going on craigslist.

    Section: 'sss' = all
             'cta' = cars all
             'cto' = cars owner
             'syp' = computer parts
             'sya' = computers
             'ela' = electronics
             'zip' = free stuff
    """

    domains = []
    cities_list = []

    domain_protocol = 'https://'
    domain_name = '.craigslist.org/search/'
    domain_section = section
    domain_search = '?query={}'.format(search)
    domain_parameters = '&sort=rel&postedToday=1'
    
#    posted_today = ''
#    title_status = ''
#    car_type = ''
#    transmission = ''
    

    with open("cities_compile.csv") as csv_file:
        cities = csv.reader(csv_file)

        for city in cities:
            domains.append(domain_protocol + str(city[0]) + domain_name + domain_section + 
                           domain_search + domain_parameters) 

            cities_list.append(city)
       
    return domains, cities_list





