<template>
  <div style="margin-right: 42vw;" class="py-auto">
    <div
    v-for="(item, index) in wantMovieList"
    :key="index"
    :item="item"
    >
      <div class="d-flex my-3">
        <input type="checkbox" @click="clickCheck(item)">
        <p class="my-auto mx-2" :class="{done:item.isCompleted}">{{ item.title }}</p>
      </div>
    </div>
  </div>
</template>

<script>
export default {
  name: 'WatchListItem',
  computed: {
    wantMovieList() {
      return this.$store.state.wantMovies
    }
  },
  methods: {
    clickCheck(item) {
      this.$store.state.wantMovies.forEach((ite) => {
        if (ite === item) {
          ite.isCompleted = !ite.isCompleted
        }
      })
      // console.log(this.$store.state.wantMovies);
    }    
  }

}
</script>

<style>
.done {
  text-decoration: line-through;
  color: gray;
}
</style>