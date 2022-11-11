<template>
  <div>
    <p v-for="(item, index) in wantMovieList"
    :key="index"
    :item="item"
    ></p>
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