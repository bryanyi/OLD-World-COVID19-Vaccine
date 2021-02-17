import React from "react";
import "../css/CountryStats.css";

const CountryStats = () => {
  return (
    <div className="Stats">
      <div className="total_vaccinations">
        <h3>Total Vaccinations</h3>
        <p>Canada</p>
        <p>February 6th, 2021</p>
        <h2>1234</h2>
      </div>
      <div className="daily_vaccinations">
        <h3>Daily Vaccinations</h3>
        <p>Canada</p>
        <p>February 6th, 2021</p>
        <h2>1234</h2>
      </div>
      <div className="vaccines">
        <h3>Vaccine</h3>
        <p>Canada</p>
        <p>February 6th, 2021</p>
        <h2>1234</h2>
      </div>
    </div>
  );
};

export default CountryStats;
