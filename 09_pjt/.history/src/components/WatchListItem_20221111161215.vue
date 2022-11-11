<template>
  <div>

  </div>
</template>

<script>
export default {
  name: 'WatchListItem',
  computed: {
    wantMovieList() {
      return this.$store.state.wantMovies
    }
  }

}
</script>

<style>

</style>