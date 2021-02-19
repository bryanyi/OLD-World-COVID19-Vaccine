import React, { useEffect, useState } from "react";
import axios from "axios";
import "./css/App.css";

// COMPONENTS
import Navigation from "./components/Navigation";
import CountryStats from "./components/CountryStats";
import InfoDetails from "./components/InfoDetails";
import Chart from "./components/Chart";

const App = () => {
  // FETCH COUNTRIES FROM DJANGO API
  useEffect(async () => {
    const { data } = await axios.get("http://127.0.0.1:8000");
    setCountries(data);
    setSearchBar("United States");
  }, []);

  const [countries, setCountries] = useState([]); // Array of objects
  const [searchBar, setSearchBar] = useState("");

  // Filter the searched country from Navigation.js component
  const filteredCountry = countries.filter((country) => {
    if (country.country.toLowerCase() === searchBar.toLowerCase()) {
      return country;
    }
  });

  const handleSearch = (val) => {
    setSearchBar(val);
  };

  return (
    <div className="App">
      <div className="left__screen">
        <Navigation
          countries={countries}
          handleSearch={handleSearch}
          searchBar={searchBar}
          filteredCountry={filteredCountry}
        />
        <CountryStats filteredCountry={filteredCountry} />
        <Chart />
      </div>

      <div className="right__screen">
        <InfoDetails filteredCountry={filteredCountry} />
      </div>
    </div>
  );
};

export default App;
