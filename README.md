# Tashkent Cafe Market Analysis

This project analyzes café competition in Tashkent to support a real
business decision: **where to open a new café**.

## Business Question
If we plan to open a new café in Tashkent:
- Which districts have the highest café competition?
- Where are potential market opportunities?
- Does price level influence customer satisfaction?

## Data
The dataset was collected manually from Google Maps and includes:
- Café name
- District
- Rating
- Review count
- Price level
- Geographic coordinates (latitude, longitude)

The original data was collected in Excel and cleaned and processed using Python.

## Analysis Steps
- Loaded and inspected raw data
- Cleaned and standardized column names
- Converted numeric fields to correct data types
- Explored rating distributions and review counts
- Compared café density, ratings, and demand across districts
- Visualized key patterns using Python

## Key Insights
- Café ratings in Tashkent are generally high across all price levels, indicating that higher prices do not guarantee higher customer satisfaction.
- Customer demand, measured by review count, varies significantly by district.
- **Mirzo Ulugbek** and **Yunusobod** show the highest average review counts, indicating strong market activity.
- **Shayxontohur** has the highest number of cafés, suggesting higher competition.
- **Olmazor** shows significantly lower customer engagement despite comparable ratings.

## Final Recommendation
Based on the analysis, the most attractive districts to open a café are **Mirzo Ulugbek** and **Yunusobod**, where customer demand and satisfaction are both high. Pricing strategy appears less important than location, suggesting that a moderately priced café in a high-demand district is more likely to succeed.

## Tools Used
- Python (pandas, matplotlib, seaborn)
- Visual Studio Code
- Git & GitHub

## Status
Completed exploratory analysis.  
This project demonstrates an end-to-end data analysis workflow using real-world data.