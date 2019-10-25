<template>
  <div>
    <div
      class="tabs"
    >
      <div
        class="tab"
        :class="{'is-tab-selected': currentYear === year}"
        v-for="year in Object.keys(stats)"
        :key="`header-${year}`"
        @click.stop="currentYear = year"
      >
        <span>{{ year }}</span>
      </div>
    </div>

    <section
      v-for="year in Object.keys(stats)"
      :key="year"
    >
      <template v-if="isVisible(year)">
        <pull-requests-per-week
          :pull-requests="stats[year].pull_requests"
          :identifier="`pull-requests-per-week-${year}`"
        />
        <issues-per-week
          :issues="stats[year].issues"
          :identifier="`issues-per-week-${year}`"
        />
        <internal-external-per-week
          :issues="stats[year].issues"
          :pull-requests="stats[year].pull_requests"
          :identifier="`internal-external-per-week-${year}`"
        />
      </template>
    </section>
  </div>
</template>

<script>
  import stats from '../public/computed.json';
  import PullRequestsPerWeek from './components/PullRequestsPerWeek';
  import IssuesPerWeek from './components/IssuesPerWeek';
  import InternalExternalPerWeek from './components/InternalExternalPerWeek';

  export default {
    name: 'App',
    data() {
      return {
        currentYear: null,
        stats,
      };
    },
    components: {
      InternalExternalPerWeek,
      IssuesPerWeek,
      PullRequestsPerWeek,
    },
    mounted() {
      const years = Object.keys(this.stats);
      this.currentYear = years[years.length - 1];
    },

    methods: {
      isVisible(year) {
        return this.currentYear === year;
      },
    },
  };
</script>

<style lang="scss">
  .tabs {
    display: flex;

    border-bottom: 1px solid #D7DBDD;

    .tab {
      cursor: pointer;
      padding: 5px 30px;
      color: #16A2D7;
      font-size: 12px;
      border-bottom: 2px solid transparent;

      span {
        color: #000;
      }

      &.is-tab-selected {
        border-bottom-color: #4EBBE4;
      }
    }
  }
</style>
