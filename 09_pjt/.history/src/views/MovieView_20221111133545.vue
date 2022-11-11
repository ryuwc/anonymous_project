<template>
  <div class='movies'>
    <h1 class="text-center">Movies</h1>
    <div class="d-flex row justify-content-evenly">
      <MovieCard
      class="col-4"
      v-for="(movie, index) in movies" 
      :key="index"
      :movie="movie"
      />
    </div>
  </div>
</template>

<script>
import MovieCard from '@/components/MovieCard.vue'

export default {
  name: 'MovieView',
  components: {
    MovieCard
  },
  computed: {
    movies() {
      return this.$store.state.movies
  }
}
}
</script>

<style>

</style>