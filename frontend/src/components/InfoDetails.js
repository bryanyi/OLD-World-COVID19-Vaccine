import React, { useEffect, useState } from "react";
import axios from "axios";
import "../css/InfoDetails.css";

const InfoDetails = ({ filteredCountry, fetchMostVaccinated }) => {
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
                <div className="source_links">
                  <p>{country.source_name}</p>
                  <a href={country.source_website}>
                    Source Website for {country.country}
                  </a>
                </div>
              </div>
              <div className="most_vaccinated">
                <h2>Most Vaccinated</h2>
                <h3>
                  {fetchMostVaccinated.map((country, i) => {
                    return (
                      <div key={i}>
                        <div>{country.country}</div>
                        <div>{country.total_vaccinations}</div>
                      </div>
                    );
                  })}
                </h3>
              </div>
            </div>
          );
        })
      )}
    </>
  );
};

export default InfoDetails;
