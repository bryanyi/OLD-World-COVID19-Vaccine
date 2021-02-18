import React from "react";
import { Bar } from "react-chartjs-2";

const Chart = () => {
  return (
    <div className="Chart">
      <div className="bar__graph">
        <Bar
          data={{
            labels: ["Total Vaccinated", "Daily Vaccinations"],
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
      </div>
    </div>
  );
};

export default Chart;
