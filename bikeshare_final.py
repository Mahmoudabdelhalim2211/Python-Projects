import time
import pandas as pd
import numpy as np
import warnings
from scipy.stats import mode

CITY_DATA = { 'chicago': 'chicago.csv',
              'new york city': 'new_york_city.csv',
              'washington': 'washington.csv' }

# Print the number of NaN values in the dataframe 
def show_NaN_values(df): 
    start_time = time.time()
    
    # Total NaN Values "Before"
    x = df.isnull().sum().sum() 
    
    print("\nCalculating NaN values..\n") 
    print("Number of NaN values are: "+str(x)) 
    
    # Drop NaN Values
    df = df.dropna(axis=0) 
    # Total NaN Values "After"
    x = df.isnull().sum().sum()
    print("Number of NaN values after dropping the rows are: "+str(x)) 
    
    print("\nThis took %s seconds." % (time.time() - start_time)) 
    
    print('-'*40) 
    return df 

def get_filters():
    """
    Asks user to specify a city, month, and day to analyze.

    Returns:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    """
	
    print('Hello! Let\'s explore some US bikeshare data!')
    
    # TO DO: get user input for city (chicago, new york city, washington). HINT: Use a while loop to handle invalid inputs
    
    # Converting the input to lowercase
    city = input('\nPlease enter city: (chicago, new york city, washington)\n')
    city = city.lower()
    while (city.lower() not in  ["chicago","new york city","washington"]): 
        city = input('You entered invalid city !: (chicago, new york city, washington)\n') 
           

    # TO DO: get user input for month (all, january, february, ... , june)
    
    # Converting the input to lowercase
    month = input('\nPlease enter month: (all, january, february, march, april, may, june)\n')
    month = month.lower()
    while (month.lower() not in ['all','january', 'february', 'march', 'april', 'may', 'june']): 
        month = input('You entered invalid month !: (all, january, february, march, april, may, june)\n') 
          
        
    # TO DO: get user input for day of week (all, monday, tuesday, ... sunday)
    
    # Converting the input to lowercase
    day = input('\nPlease enter day of the week: (all, monday, tuesday, wednesday, thursday, friday, saturday, sunday)\n')
    day = day.lower()
    while (day.lower() not in ["all", "monday", "tuesday", "wednesday", "thursday", "friday", "saturday", "sunday"]): 
        day = input('Enter correct day of the week you would like to filter by !: (all, monday, tuesday, wednesday, thursday, friday, saturday, sunday)\n')
    
    print('-'*40)
    return city, month, day


def load_data(city, month, day):
    """
    Loads data for the specified city and filters by month and day if applicable.

    Args:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    Returns:
        df - Pandas DataFrame containing city data filtered by month and day
    """
    #Read the data
    df = pd.read_csv(CITY_DATA[city])
    print(df.head())
    
    # Convert the start time to date time
    df['Start Time'] = pd.to_datetime(df['Start Time'])
    
    # Extract month from Start Time to create new column 
    df['month'] = df['Start Time'].dt.month 
     
	# Extract day of the week from Start Time to create new column
    df['day_of_week'] = df['Start Time'].dt.weekday_name

    return df


def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    # TO DO: display the most common month
	
    df['Start Time'] = pd.to_datetime(df['Start Time']) 
    # Extract month from the Start Time column to create a month column 
    df['month'] = df['Start Time'].dt.month 
    # List of available months 
    months = ['january', 'february', 'march', 'april', 'may', 'june'] 
    # The most popular month 
    month = df['month'].mode()[0] 
    # The most popular month index in the list 
    popular_month = months[month-1] 
    print("The Most Popular Month:") 
    print(popular_month) 

    # TO DO: display the most common day of week

    df['Start Time'] = pd.to_datetime(df['Start Time']) 
    # extract day from the Start Time column to create a day column 
    df['day_of_week'] = df['Start Time'].dt.weekday_name 
    # The most popular day of the week 
    popular_day = df['day_of_week'].mode()[0] 
    print("\nThe Most Popular Day:") 
    print(popular_day) 


    # TO DO: display the most common start hour
	
    df['Start Time'] = pd.to_datetime(df['Start Time']) 
    # extract hour from the Start Time column to create an hour column 
    df['hour'] = df['Start Time'].dt.hour 
    # find the most popular hour 
    popular_hour = df['hour'].mode()[0] 
    print("\nThe Most Popular Hour:") 
    print(popular_hour) 

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()
    
    #To Remove "RuntimeWarning" from mode function: The input array could not be properly checked for nan values. nan values will be ignored. "values. nan values will be ignored.", RuntimeWarning)
    
    warnings.filterwarnings("ignore", category=RuntimeWarning)
    
    # TO DO: display most commonly used start station
    popular_start_station = mode(df['Start Station'],nan_policy='omit') 
    print("\nMost commonly start Station: {} \t {} times".format(popular_start_station[0],popular_start_station[1]))
    
    # TO DO: display most commonly used end station
    popular_end_station = mode(df['End Station'],nan_policy='omit') 
    print("\nMost commonly end Station: {} \t {} times".format(popular_end_station[0],popular_end_station[1])) 


    # TO DO: display most frequent combination of start station and end station trip, please note that it takes a long time
    popular_start_end_station = mode(df[['Start Station','End Station']],nan_policy='omit')
    print("\nMost commonly start & end Station:{} \nMost commonly combination of start station & end station trip{} times".format(str(popular_start_end_station[0]),str(popular_start_end_station[1])))
    
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()
    
    # change the start time to datetime
    df['Start Time'] = pd.to_datetime(df['Start Time']) 
    
    # change the end time  to datetime 
    df['End Time'] = pd.to_datetime(df['End Time']) 
	 
	 
    # Time Difference
    df['total_travel_time'] = df['End Time'] - df['Start Time'] 
    
    # TO DO: display total travel time, calculate the total (sum of the new column)
    
    total_travel_time = df['total_travel_time'].sum() 
    print("\nTotal travel time is: {} .".format(total_travel_time)) 
    
    # TO DO: display mean travel time, calculate mean 
    
    mean_travel_time = df['total_travel_time'].mean() 
    print("\nTotal mean time is: {} .".format(mean_travel_time)) 

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # TO DO: Display counts of user types
    unique_types = df['User Type'].unique() 
    i=0
    for type in unique_types: 
        unique_types,unique_types_count = np.unique(df['User Type'],return_counts = True) 
        print("User type '{}' was repeated {} times".format(unique_types[i],unique_types_count[i])) 
        i+=1 


    # TO DO: Display counts of gender
    if 'Gender' in df.columns: 
        gender_types = df['Gender'].unique()
    i=0 
    for type in gender_types:
        gender_types,gender_types_count = np.unique(df['Gender'],return_counts = True) 
        print("Gender '{}' was repeated {} times".format(gender_types[i],gender_types_count[i])) 
        i+=1 


    # TO DO: Display earliest, most recent, and most common year of birth
    if 'Birth Year' in df.columns: 
        min_year = int(df['Birth Year'].min()) 
        max_year = int(df['Birth Year'].max()) 
        print("\nThe earlieast year of birth : {}\nThe most recent year of birth: {}".format(min_year,max_year)) 
    # most common year of birth
    common_year_of_birth = mode(df['Birth Year'],nan_policy='omit')
    print("\nMost commonly year of birth: {} \nAnd repeated: {} times".format(int(common_year_of_birth[0]),common_year_of_birth[1])) 

        
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)
    
    # Implementing the ability to display raw data to the user
def display_raw_data(city): 
    print('\nDisplay raw data...\n') 
    start_time = time.time() 
    choice=input("Would you like to display raw data? (yes/no) :") 
    if choice=='yes': 
        with open(CITY_DATA[city]) as data_file: 
            repeat_rows='yes' 
            # displaying 5 rows to the user when asking for raw data
            # ask if user want to see more, and if y display the next 5 rows
            while repeat_rows.lower()=='yes': 
                sample = [next(data_file) for x in range(5)]
                dfsample = pd.DataFrame(sample)
                pd.set_option('display.max_columns', None)  
                pd.set_option('display.expand_frame_repr', False)
                pd.set_option('max_colwidth', -1)
                print (dfsample.iloc[:6])
                repeat_rows=input("Print more lines (yes/no):") 
                print("\nThis took %s seconds." % (time.time() - start_time)) 
                print('-'*40) 

def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day) 
        df= show_NaN_values(df)
        # raw data
        display_raw_data(city)
        #time_stats(df)
        time_stats(df) 
        #station_stats(df)
        station_stats(df) 
        #trip_duration_stats(df)
        trip_duration_stats(df) 
        #user_stats(df)
        user_stats(df) 

        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break

if __name__ == "__main__":
    main()
