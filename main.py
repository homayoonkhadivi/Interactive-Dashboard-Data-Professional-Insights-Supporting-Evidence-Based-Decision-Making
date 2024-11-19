import streamlit as st

# Streamlit App Title
st.title("Data Professional Survey Dashboard")
st.subheader("Visualizing Insights from the Data Professional Survey")

# Introduction
st.write("""
This dashboard offers a comprehensive exploration of the survey conducted among data professionals. 
It delves into key trends such as demographics, job satisfaction, preferred programming languages, 
average salaries by roles and gender, and work-life balance. The visualizations are interactive, 
providing you with insights into the landscape of data professionals across different roles and countries.
""")

# Embedding Power BI Dashboard
st.components.v1.iframe(
    src="https://app.powerbi.com/reportEmbed?reportId=6b360218-e4b9-4661-9e5e-f6a3c7060f19&autoAuth=true&ctid=05a7ba18-6bbe-4b81-b56a-ab6809c437eb",
    width=1140,
    height=600
)

# Detailed Explanation of Dashboard Sections
st.write("## Dashboard Highlights and Insights")
st.write("""
1. **Demographics - Age and Gender Distribution**:
    - The dashboard provides an age slider (18 to 92 years) for filtering respondents by age groups.
    - Gender distribution is visually represented, allowing us to analyze survey results by male and female respondents.

2. **Total Survey Takers and Average Age**:
    - The survey had a total of **630 respondents**, with an average age of **29.87 years**. This highlights the relatively young age distribution of professionals in the data industry.

3. **Average Salary by Job Title**:
    - This visualization outlines the average salaries across different job titles:
        - **Data Scientist**: $94K (highest average salary).
        - **Data Engineer**: $65K.
        - **Data Analyst**: $55K.
        - **Student/Looking for a job**: $27K (lowest average salary).
    - These insights can guide professionals in identifying lucrative roles within the industry.

4. **Favorite Programming Languages**:
    - **Python** is the most popular language, with 255 respondents favoring it.
    - Other commonly used languages include **R (61 respondents)** and **JavaScript**.
    - This highlights the dominance of Python in the data domain while also acknowledging the diversity in language preferences.

5. **Work-Life Balance and Job Satisfaction**:
    - Respondents rated their happiness with salary and work-life balance:
        - **Happiness with Salary**: Average rating of **4.27 out of 10**.
        - **Happiness with Work-Life Balance**: Higher satisfaction with an average rating of **5.74 out of 10**.
    - These insights are crucial for organizations to address areas that impact employee well-being and retention.

6. **Career Switching Preferences**:
    - A significant **372 respondents (59%)** expressed a desire to switch careers, while **258 respondents (41%)** preferred to remain in their current roles.
    - This metric can help identify dissatisfaction levels and areas for improvement within data-related roles.

7. **Geographical Representation - Country of Respondents**:
    - The dashboard maps respondents across various countries, allowing organizations to identify geographic patterns in data professionals’ preferences and career opportunities.
    - Countries like **India, the United States, and Canada** are prominently represented, reflecting global trends in data-related careers.

8. **Difficulty Level Perception**:
    - The pie chart captures how respondents perceive the difficulty level of their roles:
        - Around **23% find their roles "Very Difficult"**.
        - A smaller group finds their roles “Very Easy”.
        - This visualization helps organizations better understand workforce challenges.
""")

# Additional Notes
st.write("## Important Notes")
st.write("""
- **Dashboard Access**: This embedded Power BI dashboard is interactive and allows for real-time exploration. 
  Access is determined by Power BI's sharing settings:
  - If this dashboard is public, anyone with the link can view it.
  - For private dashboards, proper permissions are required.
- **Actionable Insights**: Organizations can leverage these insights to improve work satisfaction, salary standards, and overall employee well-being.
""")

st.write("""
**Explore the interactive visualizations above to dive deeper into these insights and uncover trends shaping the data professional community!**
""")
