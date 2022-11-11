<template>
  <div class='movies'>
    <h1>movies</h1>
    
      <MovieCard
      class="d-flex row justify-content-evenly"
      v-for="(movie, index) in movies" 
      :key="index"
      :movie="movie"
      />

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