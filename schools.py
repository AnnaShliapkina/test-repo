#Every year, American high school students take SATs, which are standardized tests intended to measure literacy, numeracy, and writing skills.print
#There are three sections - reading, math, and writing, each with a maximum score of 800 points. These tests are extremely important for students 
#and colleges, as they play a pivotal role in the admissions process.

#Analyzing the performance of schools is important for a variety of stakeholders, including policy and education professionals,
#researchers, government, and even parents considering which school their children should attend.

#You have been provided with a dataset called schools.csv, which is previewed below.

#You have been tasked with answering three key questions about New York City (NYC) public school SAT performance.



#Create a pandas DataFrame called best_math_schools containing the "school_name" and "average_math" score 
#for all schools where the results are at least 80% of the maximum possible score, sorted by "average_math" in descending order.


# Re-run this cell 
import pandas as pd

# Read in the data
schools = pd.read_csv("schools.csv")

# Preview the data
schools.head()

# Filter schools where the average math score is at least 80% of the maximum
best_math_schools_80 = schools[schools['average_math'] >= 0.8 * 800]

best_math_schools_2 = best_math_schools_80[['school_name', 'average_math']]

# Sort the DataFrame by 'average_math' in descending order
best_math_schools = best_math_schools_2.sort_values(by='average_math', ascending=False)
best_math_schools.head()




#Identify the top 10 performing schools based on scores across the three SAT sections, 
#storing as a pandas DataFrame called top_10_schools containing the school name and a column named "total_SAT",
#with results sorted by total_SAT in descending order.



# The code correctly creates a new column 'total_SAT' by summing the values of 'average_math', 'average_reading', and 'average_writing' columns.
schools['total_SAT'] = schools['average_math'] + schools['average_reading'] + schools['average_writing']

# The code then sorts the DataFrame by the 'total_SAT' column in descending order and selects the top 10 rows.
top_10_schools = schools[['school_name', 'total_SAT']].sort_values('total_SAT', ascending=False).head(10)
top_10_schools.head()


#Locate the NYC borough with the largest standard deviation for "total_SAT", storing as a DataFrame called largest_std_dev with "borough" 
#as the index and three columns: "num_schools" for the number of schools in the borough, "average_SAT" for the mean of "total_SAT", 
#and "std_SAT" for the standard deviation of "total_SAT". Round all numeric values to two decimal places.


# Calculate the required statistics per borough
borough_stats = schools.groupby('borough')['total_SAT'].agg(['count', 'mean', 'std']).round(2)
# Identify the borough with the largest standard deviation
largest_std_dev = borough_stats[borough_stats['std'] == borough_stats['std'].max()]

# Rename columns for better clarity
largest_std_dev = largest_std_dev.rename(columns={'count': 'num_schools', 'mean': 'average_SAT', 'std': 'std_SAT'})


# Print the resulting DataFrame
print(largest_std_dev)
print("Murtaza 2" , largest_std_dev)