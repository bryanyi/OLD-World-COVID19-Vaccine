import React from "react";
import { Bar } from "react-chartjs-2";

const Chart = ({ filteredCountry }) => {
  return (
    <div className="Chart">
      <div className="bar__graph">
        {filteredCountry.map((country, i) => {
          return (
            <Bar
              key={i}
              data={{
                labels: ["Total Vaccinated", "Daily Vaccinations"],
                datasets: [
                  {
                    data: [
                      country.total_vaccinations,
                      country.daily_vaccinations,
                    ],
                    label: "Vaccinations",
                    backgroundColor: ["#2a9d8f", "#f4a261"],
                    borderColor: "#171717",
                    fill: true,
                  },
                ],
                options: {
                  scales: {
                    yAxes: [
                      {
                        ticks: {
                          beginAtZero: true,
                        },
                      },
                    ],
                  },
                },
              }}
              height={105}
              width={300}
            />
          );
        })}
      </div>
    </div>
  );
};

export default Chart;
