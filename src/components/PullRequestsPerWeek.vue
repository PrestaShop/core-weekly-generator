<template>
  <div :id="identifier" />
</template>

<script>
  import Plotly from 'plotly.js-dist';

  export default {
    name: 'PullRequestsPerWeek',
    props: {
      identifier: {
        type: String,
        default: '',
      },
      pullRequests: {
        type: Object,
        default: () => {},
      },
    },
    mounted() {
      const weeks = Object.keys(this.pullRequests);

      const opened = [];
      const closed = [];
      const merged = [];
      weeks.forEach((week) => {
        opened.push(this.pullRequests[week].opened.total_count);
        closed.push(this.pullRequests[week].closed.total_count);
        merged.push(this.pullRequests[week].merged.total_count);
      });

      const data = [
        {
          x: weeks,
          y: opened,
          name: 'Opened',
          type: 'scatter',
        },
        {
          x: weeks,
          y: closed,
          name: 'Closed',
          type: 'scatter',
        },
        {
          x: weeks,
          y: merged,
          name: 'Merged',
          type: 'scatter',
        },
      ];
      const layout = {
        barmode: 'stack',
        title: 'Pull requests per week',
        autosize: true,
        autoscale: true,
      };

      Plotly.newPlot(
        this.identifier,
        data,
        layout,
        {},
        {showSendToCloud: true, responsive: true},
      );
    },
  };
</script>
