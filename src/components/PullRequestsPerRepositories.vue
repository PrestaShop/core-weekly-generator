<template>
  <div :id="identifier" />
</template>

<script>
  import Plotly from 'plotly.js-dist';

  export default {
    name: 'PullRequestsPerRepositories',
    props: {
      identifier: {
        type: String,
        default: '',
      },
      pullRequests: {
        type: Object,
        default: () => {},
      },
      type: {
        type: String,
        default: 'opened',
      },
    },
    mounted() {
      const weeks = Object.keys(this.pullRequests);

      const prs = [];
      weeks.forEach((week) => {
        prs.push(this.pullRequests[week][this.type].total_count);
      });

      const data = [
        {
          x: weeks,
          y: prs,
          name: 'Opened',
          type: 'bar',
        },
      ];
      const layout = {
        barmode: 'group',
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
