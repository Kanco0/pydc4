<p align="center"><b>2026-01-18</b></p>
<h1 align="center">📊 Dataset:Telecom Customer Churn</h1>
<h2 align="center">📌 Project Summary:<br>
  Telecom Customer Churn Data Merge & Cleanup</h2>

The Problem: The telecom churn dataset was split across multiple CSV files, with customer data and population data stored separately. The raw data also contained many missing values, especially in service-related columns like Churn Reason and Internet Type, making analysis unreliable.

The Fix: I merged the datasets using a left join on Zip Code to ensure customer records remained the priority while enriching them with population data. I audited the merged dataset using structured validation tools (info(), isnull().sum()) and handled missing values through logical imputation rather than deletion. Categorical fields were filled with meaningful labels such as None or No Internet Service to preserve analytical integrity.

The Result: A single, fully merged, and clean dataset with zero missing values, consistent categories, and validated joins. The final dataset is analysis-ready and suitable for customer behavior analysis, churn insights, and reporting.

📁 Repository contains:

raw_data/ → Original CSV files

cleaned_data/ → Final merged and cleaned dataset

scripts/ → Python scripts for merging and cleaning

Validation steps and checks

<hr>
<h3>🗂️ Loading & Merging the Data</h3>
After unzipping the code, I found 3 CSV files in it.
Weird, ha? This honestly never happened to me before, but it’s fine — I can just merge the 2 main ones using <code>pd.merge()</code>.

I first checked the columns of both files using <code>df_churn.columns.tolist()</code> and <code>df_pop.columns.tolist()</code>.
Turns out they both share a common column called <code>Zip Code</code>, so I used it as a bridge between <code>df_churn</code> and <code>df_pop</code>.

This step is important to make sure the data doesn’t mix up and lines up perfectly.

By using <code>how='left'</code>, I’m telling Python that customers are the priority.
So if there are like 100 customers living in the same zip code, all of them will correctly get the same population data.

If this step wasn’t done properly, customers could end up with random zip codes, which would completely break the dataset.
And if a zip code doesn’t exist in the population table, it simply stays empty — which is totally fine and honest data-wise.
<hr>
<h3>🕵️ discovery</h3>
first tool is <code>df_final.info()</code>, this gives me the structure of the columns.
the number of rows is 7043 and there are different types of data types.

I’ve seen that some columns don’t have the full 7043 rows, which means that the dataset has a sinking hole.

the second tool is <code>df_final.isnull().sum()</code>, it’s like the scanner for this job. it goes through every column and scans how many NaN cells are there, and I saw that there are 5174 empty cells in <code>Churn Reason</code>. this number was a key to understand that these customers didn’t even leave.

the third one is <code>missing_cols.dtypes</code>, this is like a healing doctor. it tells me what data type every column has, so I can decide the next info to fix or enter.
<hr>
<h3>𓀧 specialized Cleaning</h3>
by using the scanning tools results, I used imputation instead of deleting.

categorical columns: in columns such as <code>Churn Reason</code>, <code>Internet Type</code>, and others, the empty cells mean the customer got no service. so I replaced <code>NaN</code> with understood words such as <code>None</code> or <code>No Internet Service</code>. this keeps them for future analytics instead of them just disappearing.
<hr>
<h3>🔍Final Validation</h3>
as the final checking step, the goal is to make sure that there is no NaN and all of em are gone.
the command was <code>df_final.isnull().sum().sum()</code>.

what it does is collect all nulls and all missing values in every line and every column in the whole dataset at once.
the result was 0.

I also did a double check on spelling mistakes and printed unique words in every column using a loop. the result was good again.
<hr>
<h3>saving</h3>
saving it in the same folder that iam working in, I started with 2 datasets and ended up with 1 merged dataset.
