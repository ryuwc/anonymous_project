<template>
    <div id="card-div" class="card m-3" style="width: 18rem;" data-toggle="tab-hover">
        <img :src="`https://image.tmdb.org/t/p/w185${movie.poster_path}`" class="h-100 mt-2 card-img-top" alt="...">
        <div class="card-body">
          <h5 class="card-title text-truncate">{{ movie.title }}</h5>
          <p class="card-text">평점: {{ movie.vote_average }}</p>
        </div>
    </div>

</template>

<script>
export default {
  name: 'MovieCard',
  props: {
    movie: Object
  }
}
</script>

<style>

</style>