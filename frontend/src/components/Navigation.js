import React from "react";
import "../css/Navigation.css";

const Navigation = ({ handleSearch, searchBar }) => {
  const handleSearchResult = (e) => {
    handleSearch(e.target.value);
  };

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
            onChange={handleSearchResult}
            value={searchBar}
          />
        </form>
      </div>
    </div>
  );
};

export default Navigation;
