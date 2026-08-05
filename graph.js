const records = JSON.parse(localStorage.getItem("denkoRecords")) || [];
console.log(records);

// No.1～No.13
const labels = [];
const times = [];

for (let i = 1; i <= 13; i++) {
  labels.push(`No.${i}`);

  // その問題の記録だけ取り出す
  const noRecords = records.filter((r) => Number(r.no) === i);

  if (noRecords.length === 0) {
    times.push(null); // 記録なし
  } else {
    // 最新の記録を使う
    const latest = noRecords[noRecords.length - 1];
    times.push(latest.seconds / 60);
  }
}

const ctx = document.getElementById("timeChart");

new Chart(ctx, {
  type: "line",
  data: {
    labels: labels,
    datasets: [
      {
        label: "最新タイム（分）",
        data: times,
        borderWidth: 3,
        tension: 0.3,
        spanGaps: true,
      },
    ],
  },
  options: {
    responsive: true,
    scales: {
      y: {
        reverse: true,
        min: 0,
        max: 40,
        title: {
          display: true,
          text: "時間（分）",
        },
      },
      x: {
        title: {
          display: true,
          text: "候補問題",
        },
      },
    },
  },
});
