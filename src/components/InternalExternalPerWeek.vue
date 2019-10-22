<template>
  <div :id="identifier" />
</template>

<script>
  import Plotly from 'plotly.js-dist';

  export default {
    name: 'InternalExternalPerWeek',
    props: {
      identifier: {
        type: String,
        default: '',
      },
      pullRequests: {
        type: Object,
        default: () => {},
      },
      issues: {
        type: Object,
        default: () => {},
      },
    },
    mounted() {
      const weeks = Object.keys(this.pullRequests);

      const pullRequestsOpenedInternal = [];
      const pullRequestsOpenedExternal = [];
      const issuesOpenedInternal = [];
      const issuesOpenedExternal = [];

      weeks.forEach((week) => {
        let pullRequestsCoreInternal = this.pullRequests[week].opened.core.internal;
        let pullRequestsCoreExternal = this.pullRequests[week].opened.core.external;
        Object.values(this.pullRequests[week].opened.repositories).forEach((value) => {
          pullRequestsCoreInternal += value.internal;
          pullRequestsCoreExternal += value.external;
        });

        pullRequestsOpenedInternal.push(pullRequestsCoreInternal);
        pullRequestsOpenedExternal.push(pullRequestsCoreExternal);

        let issuesCoreInternal = 0;
        let issuesCoreExternal = 0;
        Object.values(this.issues[week].opened.repositories).forEach((value) => {
          issuesCoreInternal += value.internal;
          issuesCoreExternal += value.external;
        });

        issuesOpenedInternal.push(issuesCoreInternal);
        issuesOpenedExternal.push(issuesCoreExternal);
      });

      const data = [
        {
          x: weeks,
          y: pullRequestsOpenedInternal,
          name: 'Pull requests opened internal',
          type: 'scatter',
        },
        {
          x: weeks,
          y: pullRequestsOpenedExternal,
          name: 'Pull requests opened external',
          type: 'scatter',
        },
        {
          x: weeks,
          y: issuesOpenedInternal,
          name: 'Issues opened internal',
          type: 'scatter',
        },
        {
          x: weeks,
          y: issuesOpenedExternal,
          name: 'Issues opened external',
          type: 'scatter',
        },
      ];

      const layout = {
        barmode: 'stack',
        title: 'Pull requests and issues opened by PrestaShop and the community',
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
