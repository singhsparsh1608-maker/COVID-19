import os
import sqlite3
import pandas as pd
import streamlit as st

# ================================
# CONFIGURATION
# ================================

BASE_DIR = os.path.dirname(os.path.abspath(__file__))

DATA_FOLDER = os.path.join(BASE_DIR, "data")
ASSETS_FOLDER = os.path.join(BASE_DIR, "assets")

TABLEAU_IMAGE = os.path.join(
    ASSETS_FOLDER,
'dashboard.png'
)

st.set_page_config(
    page_title="COVID-19 Analysis",
    page_icon="📊",
    layout="wide"
)

# ================================
# LOAD CSS
# ================================

try:
    with open("style.css") as css:
        st.markdown(
            f"<style>{css.read()}</style>",
            unsafe_allow_html=True
        )
except:
    pass

# ================================
# SIDEBAR
# ================================

with st.sidebar:
    st.title("📊 COVID ANALYSIS")

    selected = st.radio(
        "Navigation",
        [
            "Home",
            "Load Data",
            "SQL Analysis",
            "Tableau Dashboard",
            "Insights",
            "About"
        ],
        index=0
    )

# ==========================================
# HOME PAGE
# ==========================================

if selected == "Home":

    st.title("COVID-19 GLOBAL DATA ANALYSIS")

    st.markdown(
        """
### Data Analytics Portfolio Project

Python • SQL • SQLite • Tableau • Streamlit
"""
    )

    st.divider()

    c1,c2,c3,c4=st.columns(4)

    c1.metric(
        "Countries",
        "230"
    )

    c2.metric(
        "Total Cases",
        "181.6 M"
    )

    c3.metric(
        "Total Deaths",
        "3.6 M"
    )

    c4.metric(
        "Vaccinations",
        "2.4 B"
    )

    st.divider()

    st.subheader("Tableau Dashboard Preview")

    st.image(
        TABLEAU_IMAGE,
        use_container_width=True
    )

    st.divider()

    st.header("Project Workflow")

    st.markdown("""

### Step 1
Load COVID Death Dataset

↓

### Step 2
Load COVID Vaccination Dataset

↓

### Step 3
Store Data in SQL Database

↓

### Step 4
Perform SQL Analysis

↓

### Step 5
Generate Insights

↓

### Step 6
Create Tableau Dashboard

↓

### Step 7
Develop Interactive Streamlit Application

""")

# ==========================================
# LOAD DATA PAGE
# ==========================================

elif selected=="Load Data":

    st.title("COVID Dataset")

    st.write(
        "The project uses two datasets collected from Our World in Data."
    )

    st.subheader("COVID Death Dataset")

    deaths_path=os.path.join(
        DATA_FOLDER,
        'DATA/CovidDeaths.xlsx'
    )

    if os.path.exists(deaths_path):

        deaths=pd.read_csv(deaths_path)

        st.success("COVID Death Dataset Loaded Successfully")

        st.write("Rows :",deaths.shape[0])
        st.write("Columns :",deaths.shape[1])

        st.dataframe(
            deaths.head(10),
            use_container_width=True
        )

    st.divider()

    st.subheader("COVID Vaccination Dataset")

    vaccine_path=os.path.join(
        DATA_FOLDER,
        'DATA/CovidVacinationSPLIT.csv'
    )

    if os.path.exists(vaccine_path):

        vaccine=pd.read_csv(vaccine_path)

        st.success("COVID Vaccination Dataset Loaded Successfully")

        st.write("Rows :",vaccine.shape[0])
        st.write("Columns :",vaccine.shape[1])

        st.dataframe(
            vaccine.head(10),
            use_container_width=True
        )

# ==========================================
# SQL ANALYSIS PAGE
# ==========================================

elif selected=="SQL Analysis":

    st.title("SQL Analysis")

    st.write(
        "The following SQL queries were executed to analyze the COVID-19 dataset."
    )

    st.divider()

    #part 2
    # ==========================================================
    # QUERY 1
    # ==========================================================

    st.header("Query 1 : Display Complete COVID Death Dataset")

    sql_query = """
    SELECT *
    FROM new_schema.`coviddeaths 4(coviddeaths)`
    ORDER BY 3,4;
    """

    st.code(sql_query, language="sql")

    st.subheader("Output")

    df = pd.read_csv(
        os.path.join(DATA_FOLDER, 'PROJECT 1/DATA/coviddeaths.csv')
    )

    st.dataframe(
        df,
        use_container_width=True
    )

    st.success("""
    Finding

    • Displayed the complete COVID Death dataset.

    • Used for initial exploration before performing analysis.

    • Helped understand all available variables.
    """)

    st.divider()

    # ==========================================================
    # QUERY 2
    # ==========================================================

    st.header("Query 2 : Display Complete Vaccination Dataset")

    sql_query = """
    SELECT *
    FROM new_schema.`coviddeaths vacination(coviddeaths)`
    ORDER BY 3,4;
    """

    st.code(sql_query, language="sql")

    st.subheader("Output")

    df = pd.read_csv(
        os.path.join(DATA_FOLDER, 'DATA/CovidVacinationSPLIT.csv')
    )

    st.dataframe(
        df,
        use_container_width=True
    )

    st.success("""
    Finding

    • Explored the vaccination dataset.

    • Verified all vaccination-related fields before joining tables.
    """)

    st.divider()

    # ==========================================================
    # QUERY 3
    # ==========================================================

    st.header("Query 3 : Required Columns for Analysis")

    sql_query = """
    SELECT
    location,
    STR_TO_DATE(date,'%d/%m/%Y'),
    total_cases,
    new_cases,
    total_deaths,
    population
    FROM `coviddeaths 4(coviddeaths)`
    ORDER BY 1,2;
    """

    st.code(sql_query, language="sql")

    st.subheader("Output")

    df = pd.read_csv(
        os.path.join(DATA_FOLDER, 'https://github.com/singhsparsh1608-maker/COVID-19/blob/main/DATA/CovidDeaths.xlsx%20PRO1.xlsx')
    )

    st.dataframe(
        df,
        use_container_width=True
    )

    st.success("""
    Finding

    • Selected only the important variables.

    • Reduced unnecessary columns.

    • Prepared the dataset for further analysis.
    """)

    st.divider()

    # ==========================================================
    # QUERY 4
    # ==========================================================

    st.header("Query 4 : Total Cases vs Total Deaths")

    sql_query = """
    SELECT
    location,
    STR_TO_DATE(date,'%d/%m/%Y'),
    total_cases,
    total_deaths,
    (total_deaths/total_cases)*100 AS DeathPercentage
    FROM `coviddeaths 4(coviddeaths)`
    ORDER BY 1,2;
    """

    st.code(sql_query, language="sql")

    st.subheader("Output")

    df = pd.read_csv(
        os.path.join(DATA_FOLDER, '/Users/sparshsingh/Desktop/JOB/PROJECTS/PROJECT 1/DATA/CovidVacination SPLIT.csv')
    )

    st.dataframe(
        df,
        use_container_width=True
    )

    st.success("""
    Finding

    • Calculated the death percentage.

    • Compared deaths with confirmed COVID cases.

    • Higher values indicate higher fatality rates.
    """)

    st.divider()

    # ==========================================================
    # QUERY 5
    # ==========================================================

    st.header("Query 5 : Chances of Death in Bosnia")

    sql_query = """
    SELECT
    location,
    STR_TO_DATE(date,'%d/%m/%Y'),
    total_cases,
    total_deaths,
    (total_deaths/total_cases)*100 AS DeathPercentage
    FROM `coviddeaths 4(coviddeaths)`
    WHERE location LIKE 'Bosnia%'
    ORDER BY 1,2;
    """

    st.code(sql_query, language="sql")

    st.subheader("Output")

    df = pd.read_csv(
        os.path.join(DATA_FOLDER, "https://github.com/singhsparsh1608-maker/COVID-19/blob/main/DATA/CovidDeaths.xlsx%20PRO1.xlsx")
    )

    st.dataframe(
        df,
        use_container_width=True
    )

    st.success("""
    Finding

    • Analysed Bosnia separately.

    • Observed changes in death percentage over time.

    • Country-specific analysis helps understand local trends.
    """)

    st.divider()

    # ==========================================================
    # QUERY 6
    # ==========================================================

    st.header("Query 6 : Total Cases vs Population")

    sql_query = """
    SELECT
    location,
    STR_TO_DATE(date,'%d/%m/%Y'),
    total_cases,
    population,
    (total_cases/population)*100 AS Chances_of_Covid
    FROM `coviddeaths 4(coviddeaths)`
    WHERE location LIKE 'Bosnia%'
    ORDER BY 1,2;
    """

    st.code(sql_query, language="sql")

    st.subheader("Output")

    df = pd.read_csv(
        os.path.join(DATA_FOLDER, "https://github.com/singhsparsh1608-maker/COVID-19/blob/main/DATA/CovidDeaths.xlsx%20PRO1.xlsx")
    )

    st.dataframe(
        df,
        use_container_width=True
    )

    st.success("""
    Finding

    • Calculated infection percentage.

    • Compared total cases with population.

    • Showed the spread of COVID among the population.
    """)

    st.divider()


    #part 3

    # ==========================================================
    # QUERY 7
    # ==========================================================

    st.header("Query 7 : Countries with Highest Infection Rate")

    sql_query = """
    SELECT
        location,
        MAX(population) AS Population,
        MAX(total_cases) AS TotalCases,
        MAX((total_cases/population))*100 AS InfectionRate
    FROM `coviddeaths 4(coviddeaths)`
    GROUP BY location
    ORDER BY InfectionRate DESC;
    """

    st.code(sql_query, language="sql")

    st.subheader("Output")

    df = pd.read_csv(
        os.path.join(DATA_FOLDER, "https://github.com/singhsparsh1608-maker/COVID-19/blob/main/DATA/CovidDeaths.xlsx%20PRO1.xlsx")
    )

    st.dataframe(
        df,
        use_container_width=True,
        height=450
    )

    st.success("""
    Findings

    • Compared every country by infection rate.

    • Countries were ranked according to the percentage of their population infected.

    • Helped identify nations most severely affected by COVID-19.
    """)

    st.divider()

    # ==========================================================
    # QUERY 8
    # ==========================================================

    st.header("Query 8 : Countries with Highest Death Count")

    sql_query = """
    SELECT
        location,
        MAX(population) AS Population,
        MAX(total_deaths) AS TotalDeaths,
        MAX((total_deaths/population))*100 AS DeathRate
    FROM `coviddeaths 4(coviddeaths)`
    GROUP BY location
    ORDER BY MAX(total_deaths);
    """

    st.code(sql_query, language="sql")

    st.subheader("Output")

    df = pd.read_csv(
        os.path.join(DATA_FOLDER, "https://github.com/singhsparsh1608-maker/COVID-19/blob/main/DATA/CovidDeaths.xlsx%20PRO1.xlsx")
    )

    st.dataframe(
        df,
        use_container_width=True,
        height=450
    )

    st.success("""
    Findings

    • Ranked countries based on total deaths.

    • Calculated death percentage relative to population.

    • Highlighted countries with the highest COVID mortality.
    """)

    st.divider()

    # ==========================================================
    # QUERY 9
    # ==========================================================

    st.header("Query 9 : Death Count by Continent")

    sql_query = """
    SELECT
        continent,
        MAX(population) AS Population,
        MAX(total_deaths) AS TotalDeaths,
        MAX((total_deaths/population))*100 AS DeathRate
    FROM `coviddeaths 4(coviddeaths)`
    GROUP BY continent
    ORDER BY MAX(total_deaths) DESC;
    """

    st.code(sql_query, language="sql")

    st.subheader("Output")

    df = pd.read_csv(
        os.path.join(DATA_FOLDER, 'https://github.com/singhsparsh1608-maker/COVID-19/blob/main/DATA/CovidDeaths.xlsx%20PRO1.xlsx')
    )

    st.dataframe(
        df,
        use_container_width=True
    )

    st.success("""
    Findings

    • Compared COVID deaths across continents.

    • Displayed the continents with the highest recorded deaths.

    • Useful for regional comparison and visualization.
    """)

    st.divider()

    #part 4
    # ==========================================================
    # QUERY 10
    # ==========================================================

    st.header("Query 10 : Global COVID Numbers")

    sql_query = """
    SELECT
        SUM(total_cases) AS TotalCases,
        SUM(total_deaths) AS TotalDeaths,
        SUM((total_deaths/total_cases))*100 AS DeathRate
    FROM `coviddeaths 4(coviddeaths)`;
    """

    st.code(sql_query, language="sql")

    st.subheader("Output")

    df = pd.read_csv(
        os.path.join(DATA_FOLDER, "https://github.com/singhsparsh1608-maker/COVID-19/blob/main/DATA/CovidDeaths.xlsx%20PRO1.xlsx")
    )

    st.dataframe(
        df,
        use_container_width=True
    )

    st.success("""
    Findings

    • Calculated worldwide COVID cases.

    • Calculated worldwide COVID deaths.

    • Determined the overall global death percentage.
    """)

    st.divider()

    # ==========================================================
    # QUERY 11
    # ==========================================================

    st.header("Query 11 : Joining Death and Vaccination Tables")

    sql_query = """
    SELECT *
    FROM `coviddeaths 4(coviddeaths)` dea
    JOIN `coviddeaths vacination(coviddeaths)` vac
    ON dea.date = vac.date
    AND dea.location = vac.location
    ORDER BY 4;
    """

    st.code(sql_query, language="sql")

    st.subheader("Output")

    df = pd.read_csv(
        os.path.join(DATA_FOLDER, "https://github.com/singhsparsh1608-maker/COVID-19/blob/main/DATA/CovidDeaths.xlsx%20PRO1.xlsx")
    )

    st.dataframe(
        df,
        use_container_width=True,
        height=450
    )

    st.success("""
    Findings

    • Combined COVID death data with vaccination data.

    • Created one integrated dataset.

    • Enabled vaccination analysis together with case statistics.
    """)

    st.divider()

    # ==========================================================
    # QUERY 12
    # ==========================================================

    st.header("Query 12 : Required Columns after Joining")

    sql_query = """
    SELECT
        dea.continent,
        dea.location,
        dea.date,
        dea.population,
        vac.new_vaccinations
    FROM `coviddeaths 4(coviddeaths)` dea
    JOIN `coviddeaths vacination(coviddeaths)` vac
    ON dea.location = vac.location
    AND dea.date = vac.date
    ORDER BY 1;
    """

    st.code(sql_query, language="sql")

    st.subheader("Output")

    df = pd.read_csv(
        os.path.join(DATA_FOLDER, "Shttps://github.com/singhsparsh1608-maker/COVID-19/blob/main/DATA/CovidDeaths.xlsx%20PRO1.xlsx")
    )

    st.dataframe(
        df,
        use_container_width=True,
        height=450
    )

    st.success("""
    Findings

    • Extracted only the required columns.

    • Simplified the joined dataset.

    • Prepared the data for rolling vaccination calculations.
    """)

    st.divider()

    # ==========================================================
    # QUERY 13
    # ==========================================================

    st.header("Query 13 : Rolling Total Vaccinations")

    sql_query = """
    SELECT
        dea.continent,
        dea.location,
        dea.date,
        dea.population,
        vac.new_vaccinations,

        SUM(vac.new_vaccinations)
        OVER(
            PARTITION BY dea.location
            ORDER BY dea.location, dea.date
        ) AS TOTAL_VACCINATION

    FROM `coviddeaths 4(coviddeaths)` dea

    JOIN `coviddeaths vacination(coviddeaths)` vac

    ON dea.location = vac.location
    AND dea.date = vac.date

    ORDER BY 1;
    """

    st.code(sql_query, language="sql")

    st.subheader("Output")

    df = pd.read_csv(
        os.path.join(DATA_FOLDER, "https://github.com/singhsparsh1608-maker/COVID-19/blob/main/DATA/CovidDeaths.xlsx%20PRO1.xlsx")
    )

    st.dataframe(
        df,
        use_container_width=True,
        height=500
    )

    st.success("""
    Findings

    • Used a SQL Window Function.

    • Calculated cumulative vaccinations for each country.

    • Shows vaccination progress over time instead of daily values.
    """)

    st.divider()


    #part 5
    # ==========================================================
    # QUERY 14
    # ==========================================================

    st.header("Query 14 : Population vs Vaccination using CTE")

    sql_query = """
    WITH popvsvac
    (
    continent,
    location,
    date,
    population,
    new_vaccinations,
    TOTAL_VACCINATION
    )

    AS
    (

    SELECT
    dea.continent,
    dea.location,
    dea.date,
    dea.population,
    vac.new_vaccinations,

    SUM(vac.new_vaccinations)
    OVER
    (
    PARTITION BY dea.location
    ORDER BY dea.location,dea.date
    )

    AS TOTAL_VACCINATION

    FROM `coviddeaths 4(coviddeaths)` dea

    JOIN `coviddeaths vacination(coviddeaths)` vac

    ON dea.location=vac.location
    AND dea.date=vac.date

    )

    SELECT *,
    (TOTAL_VACCINATION/population)*100
    AS PERCENTAGE_OF_VAC

    FROM popvsvac;
    """

    st.code(sql_query, language="sql")

    st.subheader("Output")

    df = pd.read_csv(
        os.path.join(DATA_FOLDER, "https://github.com/singhsparsh1608-maker/COVID-19/blob/main/DATA/CovidDeaths.xlsx%20PRO1.xlsx")
    )

    st.dataframe(
        df,
        use_container_width=True,
        height=500
    )

    st.success("""
    Findings

    • Used a Common Table Expression (CTE).

    • Calculated cumulative vaccinations.

    • Computed vaccination percentage.

    • Prepared data for Tableau visualization.
    """)

    st.divider()

    # ==========================================================
    # QUERY 15
    # ==========================================================

    st.header("Query 15 : Create View for Tableau")

    sql_query = """
    CREATE VIEW PERCENTAGEPOPULATION AS

    SELECT
    dea.continent,
    dea.location,
    dea.date,
    dea.population,
    vac.new_vaccinations,

    SUM(vac.new_vaccinations)
    OVER
    (
    PARTITION BY dea.location
    ORDER BY dea.location,dea.date
    )

    AS TOTAL_VACCINATION

    FROM `coviddeaths 4(coviddeaths)` dea

    JOIN `coviddeaths vacination(coviddeaths)` vac

    ON dea.location=vac.location
    AND dea.date=vac.date;
    """

    st.code(sql_query, language="sql")

    st.info("""
    This SQL View was created to store the processed vaccination data,
    making it easier to connect Tableau and build interactive dashboards.
    """)

# ==========================================================
# TABLEAU PAGE
# ==========================================================

elif selected == "Tableau Dashboard":

    st.title("Interactive Tableau Dashboard")

    st.write("""
    The dashboard summarizes the global impact of COVID-19 through interactive
    visualizations created in Tableau.
    """)

    st.image(
        TABLEAU_IMAGE,
        use_container_width=True
    )

    st.divider()

    st.subheader("Dashboard Highlights")

    st.markdown("""

    ✅ Global Cases

    ✅ Global Deaths

    ✅ Vaccination Progress

    ✅ Infection Rate

    ✅ Country Comparison

    ✅ Continent Comparison

    ✅ Time Series Analysis

    """)

# ==========================================================
# INSIGHTS PAGE
# ==========================================================

elif selected == "Insights":

    st.title("Project Insights")

    st.success("""
    Key Insights Obtained

    • Countries showed significant variation in infection rates.

    • Europe and North America recorded comparatively higher death counts.

    • Vaccination campaigns accelerated rapidly after their introduction.

    • Window Functions enabled cumulative vaccination analysis.

    • SQL Views simplified Tableau dashboard creation.

    • Combining SQL, Python and Tableau resulted in an end-to-end analytics workflow.
    """)

    st.divider()

    st.subheader("Skills Demonstrated")

    st.markdown("""

    - SQL

    - Window Functions

    - Common Table Expressions (CTE)

    - Data Cleaning

    - Data Analysis

    - Tableau Dashboarding

    - Streamlit Development

    - Python

    - Pandas

    """)

# ==========================================================
# ABOUT PAGE
# ==========================================================

else:

    st.title("About")

    st.markdown("""
    # COVID-19 Global Data Analysis Portfolio
    """)

    st.write("""
    This project demonstrates an end-to-end Data Analytics workflow,
    starting from raw COVID datasets and ending with interactive
    business dashboards.

    The project combines SQL, Python, Tableau and Streamlit to
    extract insights from global COVID-19 data.
    """)

    st.divider()

    col1, col2 = st.columns(2)

    with col1:

        st.subheader("Tools Used")

        st.markdown("""

    - Python

    - Pandas

    - SQL

    - MySQL

    - SQLite

    - Tableau

    - Streamlit

    - Plotly

    """)

    with col2:

        st.subheader("Project Features")

        st.markdown("""

    - Data Cleaning

    - SQL Analysis

    - Window Functions

    - CTE

    - SQL Views

    - Interactive Dashboard

    - Data Visualization

    - Portfolio Ready

    """)

    st.divider()

    st.markdown(
        """
## Developed By

### Sparsh Singh

Data Analytics Portfolio Project
"""
    )
