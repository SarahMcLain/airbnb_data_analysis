# airbnb_data_analysis

# This repository contains two notebooks:

    ## 1. hawaii_airbnb_clean_data.ipynb
    
        This first notebook takes raw data from airbnb and cleans it into a more useable form.. Initially the data on how many bedrooms/beds/bath for each property is not accessible as it is tucked away in the name column with a lot of other information.

        The notebook splits this column to identify the aspects of the airbnb rental.  

        It then drops unnecessary columns and then fills in any NaN values with 1 as every property is guarenteed to have at least 1 place to sleep and 1 bathroom to use.

        Cleaned data is then saved to a new csv file. 

        Data was sourced from: http://insideairbnb.com/get-the-data/

    ## 2. hawaii_data_analysis.ipynb

        This notebook looks at the cleaned Hawaii airbnb data. 
        
        Part 1: 

        First it looks at how many unique neighborhoods are in the data set. 

        Then it identifes the top 20 airbnb hosts (the people who have to highest count of proeperties listed on the site).  It looks at where the properties are located (in which neighbourhood) to identify the most frequently used sites by the top owners. 

        The next section calculates the average price per night for each of the top 20 hosts

        Then it is all put together into a new dataframe containing the host name, average price pre night, the average number of beds, and the property count for each host.

        Part 2:

        Average Price per Neighborhood is calculated.

        Results:
            Bar chart showing that Lahaina is the most expensive neighborhood to stay in per night and Molokai is the cheapest. 
        
        Counts of porperties in each neighborhood are calculated.

        Results:
            Chart shows us that Lahaina is the second most listed area and Lanai is the least.


        Summary statistics of the data are calculated. 
        
        Results:
            It shows us the data set has a lot of potential outliers with a standard deviation of 1400. 
            It also identifes that the mode is 0, indicating that there are several properties listed for $0.00 a night that will need to be removed. 
        
        Create a dataframe with the outlier information and then consolidate it based on the host names.

        Show the average price by hosts in the outlier group.

        Then create a new dataframe for hosts in the outlier group the same way we did for the top 20 hosts. 

        Check and see if there are any hosts in the top 20 hosts that are also in the outlier group. 

         

