import time
import pandas as pd
import numpy as np

CITY_DATA = { 'chicago': 'chicago.csv',
              'new york city': 'new_york_city.csv',
              'washington': 'washington.csv' }

def check_data_entry(prompt, valid_entries): 
    """
    Asks user to type some input and verify if the entry typed is valid.
    Since we have 3 inputs to ask the user in get_filters(), it is easier to write a function.
    Args:
        (str) prompt - message to display to the user
        (list) valid_entries - list of string that should be accepted 
    Returns:
        (str) user_input - the user's valid input
    """
    try:
        user_input = str(input(prompt)).lower()

        while user_input not in valid_entries : 
            print('Sorry... it seems like you\'re not typing a correct entry.')
            print('Let\'s try again!')
            user_input = str(input(prompt)).lower()

        print('Great! the chosen entry is: {}\n'.format(user_input))
        return user_input

    except:
        print('Seems like there is an issue with your input')

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
    valid_cities = CITY_DATA.keys()
    prompt_city = 'Would you like to see data for chicago, new york city, or washington?: '
    city = check_data_entry(prompt_city, valid_cities)

            


    # TO DO: get user input for month (all, january, february, ... , june)
    valid_months = ['all', 'january', 'february', 'march', 'april', 'june', 'july', 'august', 'september', 'october', 'november', 'december']
    prompt_month = 'Do you want to filter by a particular month? \n if no type "all" \n if yes What month? (please, specify in small letters only ):   '
    month = check_data_entry(prompt_month,valid_months)
     


    # TO DO: get user input for day of week (all, monday, tuesday, ... sunday)
    valid_days = ['all', 'monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'saturday', 'sunday']
    prompt_day = 'Wow!!! \n What day do you want to filter with? \n If none, type "all":  '
    day = check_data_entry(prompt_day, valid_days)

      




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
    df = pd.read_csv(CITY_DATA[city])
    df['Start Time'] = pd.to_datetime(df['Start Time'])
    df['month'] = df['Start Time'].dt.month
    df['Week Day'] = df['Start Time'].dt.day_of_week
    df['Hour'] = df['Start Time'].dt.hour
    mon_index = {'january':1, 'february':2, 'march':3,'april':4, 'may':5,'june':6,'july':7,'august':8,'september':9,'october':10,'november':11,'december':12}
    if month != 'all':
        df = df.iloc[df['month'] == mon_index[month]]
    day_index = {'sunday':6, 'monday':0, 'tuesday':1, 'wednesday':2, 'thursday':3, 'friday':4, 'saturday':5}
    if day != 'all':
        df = df.iloc[df['Week Day'] == day_index[day]]
        
    return df


def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    # TO DO: display the most common month
    most_common_month = df['month'].mode()[0]
    print('The most common month is {}'.format(most_common_month))

    # TO DO: display the most common day of week
    mcd = df['Week Day'].mode()[0]
    print('The most common day of the week is{}'.format(mcd))

    # TO DO: display the most common start hour
    m_ch = df['Hour'].mode()[0]
    print('The most common start hour is {}'.format(m_ch))

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # TO DO: display most commonly used start station
    mcss = df['Start Station'].mode()[0]
    print('The most commonly used start station is {}'.format(mcss))

    # TO DO: display most commonly used end station
    mces = df['End Station'].mode()[0]
    print('The most commonly used end station is {}'.format(mces))

    # TO DO: display most frequent combination of start station and end station trip
    df['Start-End'] = df['Start Station'] + "-" + df['End Station']
    MFC = df['Start-End'].mode()
    print('The most frequent combination of start station and end station trip is {}'.format(MFC))

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # TO DO: display total travel time
    total_tt = df['Trip Duration'].sum()
    print('The total tavel time is {} seconds'.format(total_tt))

    # TO DO: display mean travel time
    mean_tt = df['Trip Duration'].mean()
    print('The mean travel time is {}'.format(mean_tt))

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # TO DO: Display counts of user types
    user_type = df['User Type'].value_counts()
    print('The count of the various user types are: \n {}'.format(user_type))
    # TO DO: Display counts of gender
    if 'Gender' in df.columns:
      gender_count = df['Gender'].value_counts
      print(gender_count)
    else:
      print('No available data for gender')

    # TO DO: Display earliest, most recent, and most common year of birth
    if 'Birth Year' in df.columns:
      earliestYOB = df['Birth Year'].max()
      mrYOB = df['Birth Year'].min
      mcYOB = df['Birth Year'].mode()[0]
      print('The earliest year of birth is {}'.format(earliestYOB))
      print('The most recent year of birth is {}'.format(mrYOB))
      print('The most comonn year of birth is {}'.format(mcYOB))
    else:
      print('No available data for Year of birth')

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)

def see_five_rows(df):
    view_data = input("Do you want to view the first 5 rows?").lower()
    if view_data == 'yes':
        i = 0
        while 0 < 1: 
            print(df.iloc[i:i + 5])
            i+=5
            see_again = input("Do you want to view the next 5 rows?").lower()
            if see_again != 'yes':
                break



def main():
    while True:
        city, month,day = get_filters()
        df = load_data(city,month,day)
        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df)
        see_five_rows(df)
        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break


if __name__ == "__main__":
	main()
