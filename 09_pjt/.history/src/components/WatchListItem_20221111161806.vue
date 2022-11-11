<template>
  <div style="margin-right: 580px;">
    <p 
    v-for="(item, index) in wantMovieList"
    :key="index"
    :item="item"
    >{{ item.title }}</p>
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