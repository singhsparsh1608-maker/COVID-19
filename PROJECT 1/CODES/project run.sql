SELECT * FROM new_schema.`coviddeaths 4(coviddeaths)`
order by 3,4;

SELECT * FROM new_schema.`coviddeaths vacination(coviddeaths)`
order by 3,4;

-- TAKING OUT THINGS THAT WE ARE GOING TO USE
select location,
STR_TO_DATE(date, '%d/%m/%Y'),
total_cases,new_cases,total_deaths,population
from`coviddeaths 4(coviddeaths)`
order by 1,2;

-- FINDING TOTAL CASES VS TOTAL DEATHS

select location,
STR_TO_DATE(date, '%d/%m/%Y'),location,
total_cases,total_deaths,(total_deaths/total_cases)*100 as DeathPercentage
from `coviddeaths 4(coviddeaths)`
order by 1,2;

-- CHANCES OF DEATH IN YOUR COUNTRY
select location,
STR_TO_DATE(date, '%d/%m/%Y'),location,
total_cases,total_deaths,(total_deaths/total_cases)*100 as DeathPercentage
from `coviddeaths 4(coviddeaths)`
where location like 'Bosnia%'
order by 1,2;

-- FINDING TOTAL CASES VS POPULATION

select location,
STR_TO_DATE(date, '%d/%m/%Y'),
total_cases,population,(total_cases/population)*100 as CHANCES_OF_COVID
from`coviddeaths 4(coviddeaths)`
where location like 'Bosnia%'
order by 1,2;

-- COMPARING COUNTRIES ACC TO INFECTION RATE
Select  location,max(population) as population,
MAX(total_cases) as total_cases,MAX((total_cases/population))*100 as INFECTION_RATE
from`coviddeaths 4(coviddeaths)`
Group by location
order by INFECTION_RATE desc;

-- SHOWING COUNTRIES WITH HIGHEST DEAD COUNT PER POPULATION
select location,max(population),
max(total_deaths),max((total_deaths/population))*100 as DEATH_RATE
from`coviddeaths 4(coviddeaths)`
group by location
order by max(total_deaths);

-- 	SAME BY CONTINENT
select continent,max(population),
max(total_deaths),max((total_deaths/population))*100 as DEATH_RATE
from`coviddeaths 4(coviddeaths)`
group by continent
order by max(total_deaths) desc;


-- GLOBAL NUMBER 
select  sum(total_cases),sum(total_deaths),sum((total_deaths/total_cases))*100 as DEATH_RATE
from`coviddeaths 4(coviddeaths)`;

-- JOINING THE TABLES AND GETTING A PROJECT OR DATA
select *
from `coviddeaths 4(coviddeaths)` dea
join `coviddeaths vacination(coviddeaths)` vac
on dea.date=vac.date
  and dea.location=dea.location
order by 4;

-- SHOWING SPECIFIC THINGS
select dea.continent,dea.location,dea.date,dea.population,vac.new_vaccinations
from `coviddeaths 4(coviddeaths)` dea
join `coviddeaths vacination(coviddeaths)` vac
on dea.location=vac.location
  and dea.date=vac.date
  order by 1;
  
  -- LOOKING AT TOTAL POPULATION VS VACCINATION
  
  select dea.continent,dea.location,dea.date,dea.population,vac.new_vaccinations,sum(vac.new_vaccinations) 
  over (partition by dea.location order by dea.location,dea.date ) as TOTAL_VACCINATION
from `coviddeaths 4(coviddeaths)` dea
join `coviddeaths vacination(coviddeaths)` vac
on dea.location=vac.location
  and dea.date=vac.date
  order by 1;
  
  select dea.continent,dea.location,dea.date,dea.population,vac.new_vaccinations,sum(vac.new_vaccinations) 
  over (partition by dea.location order by dea.location,dea.date ) as TOTAL_VACCINATION,
  (TOTAL_VACCINATION/population)*100 -- [THIS CANNOT BE DONE SO WE DO CTE]
from `coviddeaths 4(coviddeaths)` dea
join `coviddeaths vacination(coviddeaths)` vac
on dea.location=vac.location
  and dea.date=vac.date
  order by 1;
  
  -- CTE 
  with popvsvac (continent,location,date,population,new_vaccinations,TOTAL_VACCINATION)
  as
  ( 
  select dea.continent,dea.location,dea.date,dea.population,vac.new_vaccinations,sum(vac.new_vaccinations) 
  over (partition by dea.location order by dea.location,dea.date ) as TOTAL_VACCINATION
from `coviddeaths 4(coviddeaths)` dea
join `coviddeaths vacination(coviddeaths)` vac
on dea.location=vac.location
  and dea.date=vac.date
  order by 1 )
  select *,( TOTAL_VACCINATION/population)*100  as PERCENTAGE_OF_VAC
  from popvsvac;
  
  -- TEMPT TABLE IS JUST AN ALTERNATIVE OF THIS
  
  
  -- CREATING VIEW TO STORE DATA FOR LATER VISUALISATION
  create view PERCENTAGEPOPULATION as 
    select dea.continent,dea.location,dea.date,dea.population,vac.new_vaccinations,sum(vac.new_vaccinations) 
  over (partition by dea.location order by dea.location,dea.date ) as TOTAL_VACCINATION
from `coviddeaths 4(coviddeaths)` dea
join `coviddeaths vacination(coviddeaths)` vac
on dea.location=vac.location
  and dea.date=vac.date
  -- order by 1 
  
  
  
  



