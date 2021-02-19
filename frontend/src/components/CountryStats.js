import React from "react";
import LoadingComponent from "./LoadingComponent";
import "../css/CountryStats.css";

const CountryStats = ({ filteredCountry }) => {
  return (
    <>
      {filteredCountry.length == 0 ? (
        <LoadingComponent />
      ) : (
        filteredCountry.map((country, i) => {
          return (
            <div className="Stats" key={i}>
              <div className="total_vaccinations">
                <h3>Total Vaccinations</h3>
                <p>{country.country}</p>
                <p>{new Date(country.date).toDateString()}</p>
                <h2>{country.total_vaccinations}</h2>
              </div>
              <div className="daily_vaccinations">
                <h3>Daily Vaccinations</h3>
                <p>{country.country}</p>
                <p>{new Date(country.date).toDateString()}</p>
                <h2>{country.daily_vaccinations}</h2>
              </div>
              <div className="vaccines">
                <h3>Vaccine</h3>
                <p>{country.country}</p>
                <p>{new Date(country.date).toDateString()}</p>
                <h2>{country.vaccines}</h2>
              </div>
            </div>
          );
        })
      )}
    </>
  );
};

export default CountryStats;
