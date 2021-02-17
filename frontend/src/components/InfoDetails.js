import React from "react";
import "../css/InfoDetails.css";

const InfoDetails = () => {
  return (
    <div className="Details">
      <div className="sources_block">
        <h2>Sources</h2>
        <h3>Canada</h3>
      </div>
      <div className="most_vaccinated">
        <h2>Most Vaccinated</h2>
        <h3>Israel</h3>
        <p>Total vaccinations: 1234</p>
      </div>
    </div>
  );
};

export default InfoDetails;
