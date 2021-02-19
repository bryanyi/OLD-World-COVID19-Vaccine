import React from "react";
import LoadingComponent from "./LoadingComponent";
import "../css/InfoDetails.css";

const InfoDetails = ({ filteredCountry }) => {
  return (
    <>
      {filteredCountry.length == 0 ? (
        <div className="Details">
          <div className="sources_block">
            <h2>Sources</h2>
          </div>
          <div className="most_vaccinated">
            <h2>Most Vaccinated</h2>
          </div>
        </div>
      ) : (
        filteredCountry.map((country, i) => {
          return (
            <div className="Details" key={i}>
              <div className="sources_block">
                <h2>Sources</h2>
                <h3>{country.country}</h3>
              </div>
              <div className="most_vaccinated">
                <h2>Most Vaccinated</h2>
                <h3>~Placeholder~</h3>
                <p>~Total vaccinations: 1234~</p>
              </div>
            </div>
          );
        })
      )}
    </>
  );
};

export default InfoDetails;
