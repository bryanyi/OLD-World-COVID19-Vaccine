import React, { useState, useEffect } from "react";
import "../css/Navigation.css";

const Navigation = ({ setSearchBar }) => {
  const [searchValue, setSearchValue] = useState("");

  useEffect(() => {
    searchValue.target == undefined
      ? setSearchBar("United States")
      : setSearchBar(searchValue.target.value);
  }, [searchValue]);

  return (
    <div className="NavigationComponent">
      <div className="main__title">
        <h1>COVID-19</h1>
        <h1>World Vaccinations</h1>
      </div>
      <div className="navbar__search">
        <form>
          <input
            type="text"
            placeholder="Search Country"
            onChange={setSearchValue}
          />
        </form>
      </div>
    </div>
  );
};

export default Navigation;
