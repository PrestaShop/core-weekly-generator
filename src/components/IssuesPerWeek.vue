<template>
  <div :id="identifier"></div>
</template>

<script>
  import Plotly from 'plotly.js-dist';

  export default {
    name: 'IssuesPerWeek',
    props: {
      identifier: {
        type: String,
        default: '',
      },
      issues: {
        type: Object,
        default: () => {
          return {};
        },
      },
    },
    mounted() {
      const weeks = Object.keys(this.issues);

      const opened = [];
      const closed = [];
      const fixed = [];
      weeks.forEach((week) => {
        opened.push(this.issues[week].opened.total_count);
        closed.push(this.issues[week].closed.total_count);
        fixed.push(this.issues[week].fixed.total_count);
      });

      const data = [
        {
          x: weeks,
          y: opened,
          name: 'Opened',
          type: 'bar',
        },
        {
          x: weeks,
          y: closed,
          name: 'Closed',
          type: 'bar',
        },
        {
          x: weeks,
          y: fixed,
          name: 'Fixed',
          type: 'bar',
        },
      ];
      const layout = {
        barmode: 'group',
        title: 'Issues per week',
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
