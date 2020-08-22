# **About the Bank Spyders project**

## I created this as a basis for creating a more specialized **_sub-spyder_** for projects-to-come

## Each of these projects aim to do the following

- to **_scrape_** the daily exchange rates of a certain bank and save the results (to a database to-be defined in the future)
- to **_graph_** the scraping results in an informative way towards the [end-goal](https://addendgoalheaderhere) of the project.
- to **_email_** results that satisfy a certain criteria, defined by the [end-goal](https://addendgoalheaderhere) of the project.

## The End-goal(s) of all of these projects

- To find a connection between the results and current real-world events.

  - current real-world events is an ambiguous definition that needs to be better explained later, once enough data has been collected.

- To find a connection / link between the banks.

  - this can be found be overlaying the graphs of multiple banks over eachother, for example.

- To find a way to predict the fall or rise of prices given certain data (e.g Stock prices of some company, Tension between two major powers, etc..)
  - Using my currently non-existent machine-learning / deep-learning skills, I will attempt to predict prices according to the criteria of the previous two conditions.

---

## **Details about each file:**

- ### **_[BankSpyder.py](https://github.com/aziznal/bank_spyders/blob/master/BankSpyder.py)_**

  Main Class that subspyders will inherit from. has all the basic bells and whistles to make programming a subspyder more straight-forward

    Note: ResultGrapher will need results formatted in the pre-defined structure found [here](https://add_result_example.json_here).

- ### **_[ResultGrapher.py](https://github.com/aziznal/bank_spyders/blob/master/ResultGrapher.py)_**

  Graphs the results collected by the subspyder

- ### **_[functions.py](https://github.com/aziznal/bank_spyders/blob/master/functions.py)_**

  Includes general helper functions for spyders.

  - **_get_current_time():_**

    Returns a dict object with keys 'hour' and 'minutes'

  - **_set_new_interval_( starting_hour, ending_hour, required_frequency ):**

    returns the proper interval to wait between each iteration of data collecting such that the
    required frequency of data points will be reached.

  - **_save_scraped_data( spyder, results ):_**

    Saves results to a file named by the spyder according to the current session's date.

    This function creates the destination folder if it does not exist.

  - **_numth(number):_**

    Takes in 'n', returns 'n _th_'

    e.g:

        1  -> "1st"
        2  -> "2nd"
        45 -> "45th"

- ### **_[init_script.py](https://github.com/aziznal/bank_spyders/blob/master/init_script.py)_**

  Creates project settings, exec.bat, and makes sure all the essential directories are present.

  Run this script to initialize project_settings.json, and create the exec.bat file to assign to an automatic process later.

  This script is made to be customized for every different spyder as needed.
