# Stroke Data Analysis
Selected topic - Our group chose to analyze stroke data from a national database. We selected this topic because of our shared interest in healthcare. We realized that some of the tools acquired in this course would allow us to investigate this data in unique and informative ways. 
Description of their source of data - This data was pulled from Kaggle and is a private data source. It includes information such as age, gender, marital status, smoking history, avg blood sugar readings, known heart disease and whether or not the patient had a stroke. It lists data for about 5000 patients.
Questions we hope to answer with the data include identifying clusters of patients at risk for stroke and better understanding to what extent certain risk factors are predictive of stroke risk.

## Outline
Our aim was to predict stroke outcomes based off of common risk factors. 
We determined to analyze our stroke data in the following steps:

1.  Find data - we chose stroke data because of our shared interest in healthcare, we used Kaggle to find datasets
2.  Seek out comparable data for comparison (Framingham study data)
3.  Merge data per requirement guidelines
4.  Save to database on PostgreSQL (Amazon's document DB external access was outside of VCS and was prohibitive)
5.  Investigate descriptive stats using Tableau, Pandas, R, apply findings to presentation slides
6.  Discuss findings and justification for subsequent methods
7.  Scale model for machine learning
8.  Run Neural Network, compare to other machine learning tools
9.  Build/host web app using Heroku
10.  Present findings for final project
11.  Discuss with instructors and participants

## Link to Google Slides
https://docs.google.com/presentation/d/17cFCFnLW4qrUeIxmmtPW_RbE7PYHm5CGyeRSKDeG2SQ/edit#slide=id.gdabe68cc73_0_15


## Links to Dashboard
https://prod-useast-b.online.tableau.com/t/jessiestableau/authoring/Draft/Sheet1/Sheet%203#1 
https://prod-useast-b.online.tableau.com/t/jessiestableau/authoring/Seanadds62/BMIStroke?#1


## Database
Saving the merged data and encoded data to a Amazon's RDS service using PostgreSQL.

The design:

![](resources/images/db_ERD.png)

## Meeting time.
Tuesday and Thursdays after class, otherwise as needed. We will use Slack to discuss our plan as often as daily in order to meet deadlines. 

## Communication
Chat through slack and use zoom to video chat. Use Trello to keep track of tasks. Meet as needed to finalize project. 
