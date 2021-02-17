import React, { useEffect, useState } from "react";
import axios from "axios";

// COMPONENTS
import Navigation from "./components/Navigation";
import CountryStats from "./components/CountryStats";
import InfoDetails from "./components/InfoDetails";
import Chart from "./components/Chart";

const App = () => {
  const [countries, setCountries] = useState([]);

  useEffect(async () => {
    const { data } = await axios.get("http://127.0.0.1:8000");
    setCountries(data);
  }, [setCountries]);

  return (
    <div className="App">
      <h1>This is the covid vaccine app!</h1>
      <Navigation />
      <CountryStats />
      <InfoDetails />
      <Chart />
    </div>
  );
};

export default App;
